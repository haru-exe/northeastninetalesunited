"""Check one topic fragment for the Elasticity notes.

Usage (from any folder):
    python -I notes-build/scripts/check_fragment.py notes-build/fragments/t4.html

Prints ERRORS (must fix) and WARNINGS (read and decide). Exit code 1 if any error.
It does not render KaTeX; the coordinator does a browser render check afterwards.
"""
import re
import sys
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr",
        "path", "circle", "line", "rect", "polyline", "polygon", "ellipse", "stop", "use"}
UNICODE_MATH = set("×÷±²³¹⁰⁴⁵⁶⁷⁸⁹⁻⁺₀₁₂₃₄₅₆₇₈₉≈≤≥≠∂∇√∫∑∏∞′″∈∉⊂∪∩∝∘⋅")
ARROWS = set("→⇒⇔↔←")
BANNED = [r"\bsimilarly\b", r"\bas before\b", r"\bas in (section|topic|example)\b", r"\bby the same method\b",
          r"\bit can be shown\b", r"\bcan easily be shown\b", r"\bit is easily (shown|seen|verified)\b",
          r"\bthe rest follows\b", r"\band so on\b", r"\bclearly\b", r"\bobviously\b", r"\btrivially\b",
          r"\bin a similar (way|fashion|manner)\b", r"\bleft as an exercise\b"]
BAD_TEX = [r"\\tag\b", r"\\label\b", r"\\eqref\b", r"\\begin\{equation", r"\\begin\{align\*?\}", r"\\begin\{eqnarray",
           r"\\over\b", r"\\bm\b", r"\\require\b", r"\\newcommand\b", r"\\def\b"]


class Structure(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack, self.errors = [], []
        self.sections, self.classes = [], []
        self.turn_depth, self.turn_summaries, self.turns = None, [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "") or ""
        if tag == "section":
            self.sections.append((a.get("id"), cls))
        if cls:
            self.classes.append((tag, cls))
        if tag == "div" and "box" in cls.split() and "turn" in cls.split():
            self.turn_depth = len(self.stack)
            self.turn_summaries = []
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append(f"line {self.getpos()[0]}: closing </{tag}> with nothing open")
            return
        open_tag, pos = self.stack[-1]
        if open_tag != tag:
            self.errors.append(f"line {self.getpos()[0]}: </{tag}> closes <{open_tag}> opened at line {pos[0]}")
            # try to recover
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    del self.stack[i:]
                    break
        else:
            self.stack.pop()
        if self.turn_depth is not None and len(self.stack) == self.turn_depth:
            self.turns.append(list(self.turn_summaries))
            self.turn_depth = None

    def handle_data(self, data):
        if self.turn_depth is not None and self.stack and self.stack[-1][0] == "summary":
            self.turn_summaries.append(data.strip())


def strip_regions(src):
    """Remove comments, svg, script and style blocks (replace with spaces to keep line numbers)."""
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    src = re.sub(r"<!--.*?-->", blank, src, flags=re.S)
    src = re.sub(r"<(svg|script|style)\b.*?</\1>", blank, src, flags=re.S | re.I)
    return src


def line_of(src, idx):
    return src.count("\n", 0, idx) + 1


def main(path):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    raw = open(path, encoding="utf-8").read()
    errors, warnings = [], []
    m = re.search(r"t(\d)\.html$", path.replace("\\", "/"))
    topic = int(m.group(1)) if m else None

    # HTML structure
    p = Structure()
    p.feed(raw)
    p.close()
    errors += p.errors
    for tag, pos in p.stack:
        errors.append(f"line {pos[0]}: <{tag}> is never closed")
    topic_sections = [s for s in p.sections if "topic" in (s[1] or "")]
    if len(topic_sections) != 1:
        errors.append(f"expected exactly one <section class=\"topic\">, found {len(topic_sections)}")
    elif topic is not None and topic_sections[0][0] != f"t{topic}":
        errors.append(f"section id is {topic_sections[0][0]!r}, expected 't{topic}'")

    def count(cls_words):
        return sum(1 for tag, c in p.classes if all(w in c.split() for w in cls_words))
    concepts = sum(1 for tag, c in p.classes if tag == "h3" and "concept" in c.split())
    n_ex, n_turn = count(["box", "ex"]), count(["box", "turn"])
    if concepts == 0:
        errors.append("no <h3 class=\"concept\"> headings found")
    if n_ex < concepts:
        errors.append(f"{concepts} concepts but only {n_ex} worked-example boxes")
    if n_turn != concepts:
        errors.append(f"{concepts} concepts but {n_turn} 'Your turn' boxes (need exactly one per concept)")
    for i, summaries in enumerate(p.turns, 1):
        joined = " | ".join(summaries)
        if not any(s.lower().startswith("hint") for s in summaries) or not any(s.lower().startswith("answer") for s in summaries):
            errors.append(f"'Your turn' box {i}: needs a <details> 'Hint' and a <details> 'Answer and key steps' (found: {joined or 'none'})")
    if count(["box", "recap"]) < 2:
        errors.append("need two recap boxes: 'Where we are' and 'What you need from earlier'")
    if count(["box", "sym"]) < 1:
        errors.append("missing the 'Symbols in this topic' box")
    if count(["box", "key"]) < 1:
        errors.append("missing the 'Key results' box")
    if not any(tag == "p" and "next" in c.split() for tag, c in p.classes):
        errors.append("missing <p class=\"next\"> 'What comes next'")
    n_ahead = count(["box", "ahead"])
    if topic is not None and topic >= 4 and n_ahead != 1:
        errors.append("Topics 4 to 9 need exactly one 'Looking ahead · Ch 5–8' box")
    if topic is not None and topic <= 3 and n_ahead:
        errors.append("Chapter 1 topics must not have a 'Looking ahead' box (excluded by the student)")

    # Maths checks on text outside svg/script/style/comments
    src = strip_regions(raw)
    disp = list(re.finditer(r"\$\$(.+?)\$\$", src, flags=re.S))
    no_disp = re.sub(r"\$\$(.+?)\$\$", lambda mm: " " * len(mm.group(0)), src, flags=re.S)
    singles = [mm.start() for mm in re.finditer(r"(?<!\\)\$", no_disp)]
    if len(singles) % 2:
        errors.append(f"odd number of single $ delimiters ({len(singles)}); first one near line {line_of(src, singles[0])}")
    inline = []
    for a, b in zip(singles[0::2], singles[1::2]):
        inline.append((a, src[a + 1:b]))
        if "\n\n" in src[a:b]:
            errors.append(f"line {line_of(src, a)}: inline $...$ spans a blank line; probably a missing $")
    segments = [(mm.start(), mm.group(1)) for mm in disp] + inline
    for start, tex in segments:
        ln = line_of(src, start)
        if "<" in tex or ">" in tex:
            errors.append(f"line {ln}: '<' or '>' inside maths (use \\lt, \\gt, \\le, \\ge; never HTML tags inside $...$)")
        if "&lt;" in tex or "&gt;" in tex:
            warnings.append(f"line {ln}: &lt;/&gt; inside maths; prefer \\lt / \\gt")
        for pat in BAD_TEX:
            if re.search(pat, tex):
                errors.append(f"line {ln}: {pat.replace(chr(92) * 2, chr(92))} is not allowed in these notes")
        if re.search(r"\S&\S", tex.replace("\\&", "")):
            warnings.append(f"line {ln}: put spaces around & in matrices/aligned blocks (a & b)")
        if tex.count("{") != tex.count("}"):
            errors.append(f"line {ln}: unbalanced braces in maths: {tex[:60]!r}")
        if any(ch in UNICODE_MATH or 0x0370 <= ord(ch) <= 0x03FF for ch in tex):
            errors.append(f"line {ln}: Unicode symbol inside maths; use LaTeX commands")

    # Prose checks (maths removed)
    prose = src
    for start, tex in sorted(segments, key=lambda s: -s[0]):
        pass
    prose = re.sub(r"\$\$(.+?)\$\$", lambda mm: " " * len(mm.group(0)), prose, flags=re.S)
    prose = re.sub(r"(?<!\\)\$(.+?)(?<!\\)\$", lambda mm: " " * len(mm.group(0)), prose, flags=re.S)
    text = re.sub(r"<[^>]+>", lambda mm: " " * len(mm.group(0)), prose)
    for i, ch in enumerate(text):
        if ch in UNICODE_MATH or 0x0370 <= ord(ch) <= 0x03FF:
            errors.append(f"line {line_of(text, i)}: Unicode maths character {ch!r} in prose; write it in LaTeX")
        elif ch in ARROWS:
            warnings.append(f"line {line_of(text, i)}: arrow {ch!r} in prose; prefer words or $\\to$")
    for pat in BANNED:
        for mm in re.finditer(pat, text, flags=re.I):
            errors.append(f"line {line_of(text, mm.start())}: shortcut phrase '{mm.group(0)}': write out the working instead")
    for mm in re.finditer(r"\.\.\.|\u2026", text):
        errors.append(f"line {line_of(text, mm.start())}: dots in prose; write the steps or the full list")
    for mm in re.finditer(r"\\[a-zA-Z]+", text):
        warnings.append(f"line {line_of(text, mm.start())}: LaTeX command {mm.group(0)} outside $...$ (will show as raw text)")

    print(f"Checked {path}: {concepts} concepts, {n_ex} worked examples, {n_turn} your-turn boxes, "
          f"{len(disp)} display and {len(inline)} inline maths segments.")
    for e in errors:
        print("ERROR  ", e)
    for w in warnings[:40]:
        print("WARNING", w)
    if len(warnings) > 40:
        print(f"WARNING ... and {len(warnings) - 40} more warnings")
    print("RESULT:", "FAIL" if errors else "PASS")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
