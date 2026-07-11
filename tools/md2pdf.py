#!/usr/bin/env python3
"""INSITE branded markdown -> PDF converter. Usage: md2pdf.py in.md out.pdf "BAND TITLE" "Band subtitle" [serif|sans]"""
import re, sys, subprocess, tempfile, os

def inline(s):
    s = s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<i>\1</i>', s)
    s = s.replace('(TM)','&trade;').replace('->','&rarr;')
    s = re.sub(r'(https?://[^\s,)]+)', r'<span class="url">\1</span>', s)
    return s

def convert(md):
    lines = md.split('\n'); out=[]; i=0
    NUM = re.compile(r'^\d+\. ')
    while i < len(lines):
        ln = lines[i]
        if ln.startswith('|') and i+1 < len(lines) and re.match(r'^\|[\s\-|]+\|$', lines[i+1] or ''):
            hdr=[c.strip() for c in ln.strip('|').split('|')]
            out.append('<table><thead><tr>'+''.join(f'<th>{inline(h)}</th>' for h in hdr)+'</tr></thead><tbody>')
            i+=2
            while i < len(lines) and lines[i].startswith('|'):
                cells=[c.strip() for c in lines[i].strip('|').split('|')]
                out.append('<tr>'+''.join(f'<td>{inline(c)}</td>' for c in cells)+'</tr>'); i+=1
            out.append('</tbody></table>'); continue
        if ln.startswith('# PART'): out.append(f'<h1 class="part">{inline(ln[2:])}</h1>')
        elif ln.startswith('# '): pass
        elif ln.startswith('## '): out.append(f'<h2>{inline(ln[3:])}</h2>')
        elif NUM.match(ln):
            out.append('<ol>')
            while i < len(lines) and NUM.match(lines[i]):
                out.append(f'<li>{inline(NUM.sub("",lines[i]))}</li>'); i+=1
            out.append('</ol>'); continue
        elif ln.startswith('- '):
            out.append('<ul>')
            while i < len(lines) and lines[i].startswith('- '):
                out.append(f'<li>{inline(lines[i][2:])}</li>'); i+=1
            out.append('</ul>'); continue
        elif ln.startswith('!IMG '):
            parts=ln.split(); src=parts[1]; w=parts[2] if len(parts)>2 else '100%'
            out.append(f'<div style="text-align:center;margin:10px 0"><img src="file://{src}" style="width:{w};max-width:100%"/></div>')
        elif ln.strip()=='---': out.append('<hr/>')
        elif ln.strip()=='': pass
        else: out.append(f'<p>{inline(ln)}</p>')
        i+=1
    return '\n'.join(out)

def main():
    src, dst, title, sub = sys.argv[1:5]
    serif = len(sys.argv)>5 and sys.argv[5]=='serif'
    font = "Georgia, 'Times New Roman', serif" if serif else "Helvetica, Arial, sans-serif"
    fs = '10.8pt' if serif else '10.2pt'
    body = convert(open(src).read())
    page=f"""<!doctype html><html><head><meta charset='utf-8'><style>
@page {{ margin:0; }}
body {{ font-family: {font}; color:#26303a; font-size:{fs}; line-height:1.58; margin:0; }}
.band {{ background:#153A5B; color:#fff; padding:28px 52px 22px 52px; font-family:Helvetica,Arial,sans-serif; }}
.band h1 {{ margin:0; font-size:21pt; letter-spacing:1.5px; }}
.band p {{ margin:7px 0 0 0; color:#cfe0ee; font-size:10.5pt; }}
.wrap {{ padding:20px 52px 44px 52px; }}
h1.part {{ font-family:Helvetica,Arial,sans-serif; color:#fff; background:#153A5B; font-size:13pt; letter-spacing:1px; padding:8px 14px; margin:26px 0 10px 0; page-break-after:avoid; }}
h2 {{ font-family:Helvetica,Arial,sans-serif; color:#153A5B; font-size:12pt; margin:18px 0 6px 0; border-bottom:2px solid #3E7C59; padding-bottom:2px; page-break-after:avoid; }}
p {{ margin:7px 0; }} b {{ color:#153A5B; }}
table {{ border-collapse:collapse; width:100%; margin:9px 0 13px 0; font-size:9.6pt; font-family:Helvetica,Arial,sans-serif; page-break-inside:avoid; }}
th {{ background:#153A5B; color:#fff; text-align:left; padding:5px 8px; }}
td {{ border:1px solid #d3dae3; padding:5px 8px; vertical-align:top; }}
tr:nth-child(even) td {{ background:#F5F7FA; }}
ul,ol {{ margin:6px 0 11px 26px; padding:0; }} li {{ margin-bottom:5px; }}
hr {{ border:none; border-top:1px solid #d3dae3; margin:14px 0; }}
.url {{ font-family:Helvetica,Arial,sans-serif; font-size:8.4pt; color:#3E7C59; word-break:break-all; }}
</style></head><body>
<div class='band'><h1>{title}</h1><p>{sub}</p></div>
<div class='wrap'>{body}</div></body></html>"""
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as f:
        f.write(page); tmp=f.name
    subprocess.run(['wkhtmltopdf','-q','--enable-local-file-access','--margin-top','0','--margin-bottom','13mm','--margin-left','0','--margin-right','0',tmp,dst],check=True)
    os.unlink(tmp)
    print('wrote', dst)

if __name__=='__main__': main()
