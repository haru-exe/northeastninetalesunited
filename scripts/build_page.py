import sys
shell_path, css_path, out_path, preview_path = sys.argv[1:5]
shell = open(shell_path, encoding='utf-8').read()
css = open(css_path, encoding='utf-8').read()
assert shell.count('/*KATEX_CSS*/') == 1
page = shell.replace('/*KATEX_CSS*/', css)
open(out_path, 'w', encoding='utf-8', newline='\n').write(page)
preview = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
           '<style>:root{padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}body{margin:0}</style>'
           '</head><body>' + page + '</body></html>')
open(preview_path, 'w', encoding='utf-8', newline='\n').write(preview)
print('page KB:', round(len(page.encode('utf-8'))/1024), '| title in first 8KB:', '<title>' in page[:8192])
