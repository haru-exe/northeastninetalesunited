import re, base64, sys, os
src_dir, out_path = sys.argv[1], sys.argv[2]
css = open(os.path.join(src_dir, 'katex.min.css'), encoding='utf-8').read()
def repl(m):
    name = m.group(1)
    data = open(os.path.join(src_dir, 'fonts', name + '.woff2'), 'rb').read()
    return 'src:url(data:font/woff2;base64,' + base64.b64encode(data).decode('ascii') + ') format("woff2")'
css2, n = re.subn(r'src:url\(fonts/(KaTeX_[A-Za-z0-9_-]+)\.woff2\) format\("woff2"\)(?:,url\([^)]*\) format\("[a-z]+"\))*', repl, css)
open(out_path, 'w', encoding='utf-8').write(css2)
print('font-faces replaced:', n, '| remaining relative urls:', len(re.findall(r'url\(fonts/', css2)), '| size KB:', round(len(css2)/1024))
