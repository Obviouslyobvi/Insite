#!/usr/bin/env python3
"""build_manual.py - compiles the developer-facing pages into 05_WEBSITE/manual.html.
Run after ANY edit to builders/qualify/fee_estimator. Never edit manual.html by hand."""
import re, datetime, os
HERE=os.path.dirname(os.path.abspath(__file__))
SITE=os.path.join(os.path.dirname(HERE),'05_WEBSITE')
def body_of(name):
    t=open(os.path.join(SITE,name),encoding='utf8').read()
    b=t[t.index('<body'):]; b=b[b.index('>')+1:]; b=b[:b.rindex('</body>')]
    b=re.sub(r"<div class=['\"]prelaunch['\"]>.*?</div>","",b,flags=re.S)
    b=re.sub(r"<header.*?</header>","",b,flags=re.S)
    b=re.sub(r"<footer.*?</footer>","",b,flags=re.S)
    b=re.sub(r"<script.*?</script>","",b,flags=re.S)
    b=re.sub(r"<iframe.*?</iframe>","<p><i>The application form lives on the website's Apply page.</i></p>",b,flags=re.S)
    return b
page=f"""<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
<title>INSITE Developer Manual</title><style>
:root{{--navy:#153A5B;--green:#3E7C59;--line:#d3dae3;--light:#F5F7FA;--slate:#6B7280;--ink:#26303a}}
*{{box-sizing:border-box}}body{{margin:0;font-family:Helvetica,Arial,sans-serif;color:var(--ink);line-height:1.55}}
.mhead{{background:var(--navy);color:#fff;padding:26px 22px}}
.mhead .in{{max-width:900px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}}
.mwrap{{max-width:900px;margin:0 auto;padding:10px 22px 60px}}
h1{{font-size:30px;color:var(--navy)}}h2,h3{{color:var(--navy)}}
.wrap{{max-width:900px;margin:0 auto;padding:0}}
section{{padding:26px 0;border-bottom:1px solid var(--line)}}
.printbar{{text-align:right;padding:14px 22px;max-width:900px;margin:0 auto}}
.printbtn{{background:var(--green);color:#fff;border:0;padding:10px 18px;font-size:15px;cursor:pointer}}
img{{max-width:100%;height:auto}} a{{color:var(--green)}}
.partcap{{background:var(--light);border-left:5px solid var(--green);padding:10px 16px;margin:34px 0 8px;font-weight:bold;color:var(--navy);letter-spacing:1px}}
@media print{{.printbar{{display:none}}.partcap{{page-break-before:always}}a{{color:var(--ink);text-decoration:none}}.mhead{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}}}
</style></head><body>
<div class='mhead'><div class='in'><div style='font-weight:bold;font-size:22px;letter-spacing:2px'>INSITE&#8482; DEVELOPER MANUAL</div><div style='font-size:13px;color:#9fb6cd'>Compiled from the program website &middot; {datetime.date.today().strftime('%B %d, %Y')}</div></div></div>
<div class='printbar'><button class='printbtn' onclick='window.print()'>Print / Save as PDF</button></div>
<div class='mwrap'>
<div class='partcap'>PART 1 &middot; THE PROGRAM IN THREE QUESTIONS</div>
{body_of('builders.html')}
<div class='partcap'>PART 2 &middot; QUALIFICATION</div>
{body_of('qualify.html')}
<div class='partcap'>PART 3 &middot; YOUR FEES, THE COMPARISON</div>
{body_of('fee_estimator.html')}
<p style='color:var(--slate);font-size:12.5px;margin-top:40px'>INSITE&#8482; is a pre-launch program concept administered by HGF Management Company. This manual is compiled from the program website for reference and is not an offer of financing, legal advice, or investment advice. Program structure, eligibility, costs, and pricing are subject to issuer approval, bond counsel review, and program underwriting.</p>
</div></body></html>"""
open(os.path.join(SITE,'manual.html'),'w',encoding='utf8').write(page)
print("manual.html regenerated,",len(page),"chars")
