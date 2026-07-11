#!/usr/bin/env python3
"""Contrast agent: renders an HTML file with injected ES5 JS that computes WCAG
contrast for every text-bearing element against its effective background, then
parses the report. Flags ratios below 3.0. Usage: contrast_check.py file.html"""
import sys, subprocess, tempfile, os, re

JS = """
<script>
function lum(c){function f(v){v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4);}
 return 0.2126*f(c[0])+0.7152*f(c[1])+0.0722*f(c[2]);}
function parseC(s){var m=/rgba?\\(([^)]+)\\)/.exec(s);if(!m)return null;
 var p=m[1].split(',');var a=p.length>3?parseFloat(p[3]):1;
 return {c:[parseFloat(p[0]),parseFloat(p[1]),parseFloat(p[2])],a:a};}
function effBg(el){var e=el;while(e&&e!==document.documentElement){
 var b=parseC(window.getComputedStyle(e).backgroundColor);
 if(b&&b.a>0.5)return b.c;e=e.parentNode;}return [255,255,255];}
function ratio(f,b){var l1=lum(f),l2=lum(b);var hi=Math.max(l1,l2),lo=Math.min(l1,l2);
 return (hi+0.05)/(lo+0.05);}
window.setTimeout(function(){
 var out=[],all=document.getElementsByTagName('*');
 for(var i=0;i<all.length;i++){var el=all[i];
  if(el.tagName==='SCRIPT'||el.tagName==='STYLE')continue;
  var txt='';for(var j=0;j<el.childNodes.length;j++){var n=el.childNodes[j];
   if(n.nodeType===3)txt+=n.nodeValue;}
  txt=txt.replace(/\\s+/g,' ').replace(/^ | $/g,'');
  if(txt.length<4)continue;
  var st=window.getComputedStyle(el);
  if(st.display==='none'||st.visibility==='hidden')continue;
  var fg=parseC(st.color);if(!fg)continue;
  var r=ratio(fg.c,effBg(el));
  var id=el.tagName.toLowerCase()+(el.className?'.'+String(el.className).split(' ')[0]:'');
  out.push(r.toFixed(2)+'|'+id+'|'+txt.substring(0,50));}
 out.sort(function(a,b){return parseFloat(a)-parseFloat(b);});
 document.body.innerHTML='<pre>CONTRAST_REPORT_V1\\n'+out.slice(0,60).join('\\n')+'</pre>';
 document.body.setAttribute('style','background:#fff;color:#000');
},400);
</script>
"""

def check(path, threshold=3.0):
    html = open(path).read()
    inj = html.replace('</body>', JS + '</body>') if '</body>' in html else html + JS
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, dir=os.path.dirname(os.path.abspath(path))) as f:
        f.write(inj); tmp = f.name
    pdf = tmp + '.pdf'
    subprocess.run(['wkhtmltopdf','-q','--enable-local-file-access','--enable-javascript',
                    '--javascript-delay','1400', tmp, pdf], check=True)
    txt = subprocess.run(['pdftotext', pdf, '-'], capture_output=True, text=True).stdout
    os.unlink(tmp); os.unlink(pdf)
    if 'CONTRAST_REPORT_V1' not in txt:
        print(f'{path}: REPORT FAILED TO GENERATE'); return 1
    fails = []
    for line in txt.splitlines():
        m = re.match(r'^(\d+\.\d+)\|([^|]+)\|(.*)$', line.strip())
        if m and float(m.group(1)) < threshold:
            fails.append(f'  ratio {m.group(1)}  <{m.group(2)}>  "{m.group(3).strip()}"')
    name = os.path.basename(path)
    if fails:
        print(f'{name}: {len(fails)} LOW-CONTRAST FAILURES (< {threshold}:1)')
        for f_ in fails[:12]: print(f_)
        return 1
    print(f'{name}: CONTRAST CLEAN (all text >= {threshold}:1)')
    return 0

if __name__ == '__main__':
    sys.exit(check(sys.argv[1]))
