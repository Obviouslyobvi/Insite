#!/usr/bin/env python3
"""build_manual.py - compiles the developer-facing pages into 05_WEBSITE/manual.html.
Paginated for print (Letter), with the application form printed on the page itself.
Run after ANY edit to builders/qualify/fee_estimator. Never edit manual.html by hand."""
import re, datetime, os
from zoneinfo import ZoneInfo
HERE=os.path.dirname(os.path.abspath(__file__))
SITE=os.path.join(os.path.dirname(HERE),'05_WEBSITE')

def body_of(name):
    t=open(os.path.join(SITE,name),encoding='utf8').read()
    b=t[t.index('<body'):]; b=b[b.index('>')+1:]; b=b[:b.rindex('</body>')]
    b=re.sub(r"<div class=['\"]prelaunch['\"]>.*?</div>","",b,flags=re.S)
    b=re.sub(r"<header.*?</header>","",b,flags=re.S)
    b=re.sub(r"<footer.*?</footer>","",b,flags=re.S)
    b=re.sub(r"<script.*?</script>","",b,flags=re.S)
    # an interactive calculator is meaningless on paper: drop the whole section
    b=re.sub(r'<section id="calc">.*?</section>',"",b,flags=re.S)
    i=b.find("<div class='dis'")
    if i<0: i=b.find('<div class="dis"')
    if i>=0:
        tail=b[i:]; opens=0; j=None; k=0
        for m in re.finditer(r"</?div", tail):
            opens += 1 if m.group(0)=="<div" else -1
            if opens==0: j=tail.index(">",m.start())+1; break
        b=b[:i]+(tail[j:] if j else "")
    # page-local disclaimer removed; the manual carries its own
    b=re.sub(r"<iframe.*?</iframe>","",b,flags=re.S)
    # a printable manual carries the form itself; strip every button/link to forms or pages
    b=re.sub(r"<a class=['\"]btn[^>]*>.*?</a>","",b,flags=re.S)
    b=re.sub(r"<p[^>]*>[ \n\t]*</p>","",b)
    # self-balance: strip surplus closing divs, add missing ones, so no body can break the page container
    surplus=len(re.findall(r"</div>",b))-len(re.findall(r"<div[ >]",b))
    while surplus>0 and b.rstrip().endswith("</div>"):
        b=b.rstrip()[:-6]; surplus-=1
    if surplus>0:
        parts=b.rsplit("</div>",surplus); b="".join(parts)
    elif surplus<0:
        b=b+"</div>"*(-surplus)
    b=re.sub(r"<a href=['\"][^'\"]*['\"][^>]*>(.*?)</a>",r"\1",b,flags=re.S)
    return b


MARK_PATTERN = ["NNNNNN", "NNNGGG", "NGNNGG", "NNNNOO"]
MARK_NAVY   = "#1A3E6C"
MARK_GREEN  = "#8DB87A"
MARK_OUTLINE_STROKE = "#6A727D"
MARK_OUTLINE_FILL   = "#ECF4FC"
TAGLINE_GRAY = "#6B7280"


def title_logo_svg():
    """Stacked primary logo: 24-cell mark (6 across, 4 down) over INSITE over the
    two-line tagline. Grid, colours and cell order measured from the founder's
    reference artwork, August 13, 2026. Tagline is Slate Gray per INS-001."""
    cells=[]
    for r,row in enumerate(MARK_PATTERN):
        for c,ch in enumerate(row):
            x,y=c*58,r*58
            if ch=='O':
                cells.append(f"<rect x='{x+3}' y='{y+3}' width='44' height='44' fill='{MARK_OUTLINE_FILL}' stroke='{MARK_OUTLINE_STROKE}' stroke-width='6'/>")
            else:
                fill=MARK_GREEN if ch=='G' else MARK_NAVY
                cells.append(f"<rect x='{x}' y='{y}' width='50' height='50' fill='{fill}'/>")
    return ("<svg width='268' height='300' viewBox='0 0 340 372' xmlns='http://www.w3.org/2000/svg' aria-label='INSITE'>"
            +"".join(cells)
            +f"<text x='170' y='300' text-anchor='middle' font-family='Helvetica,Arial,sans-serif' font-weight='bold' font-size='64' letter-spacing='6' fill='{MARK_NAVY}'>INSITE</text>"
            +f"<text x='295' y='252' font-family='Helvetica,Arial,sans-serif' font-size='18' fill='{MARK_NAVY}'>&#8482;</text>"
            +f"<text x='170' y='334' text-anchor='middle' font-family='Helvetica,Arial,sans-serif' font-size='15' letter-spacing='1.5' fill='{TAGLINE_GRAY}'>DEVELOPMENT IMPACT &amp;</text>"
            +f"<text x='170' y='356' text-anchor='middle' font-family='Helvetica,Arial,sans-serif' font-size='15' letter-spacing='1.5' fill='{TAGLINE_GRAY}'>SCHOOL FEE FINANCING PROGRAM</text>"
            +"</svg>")

def field(label, note=""):
    n=f"<div class='fnote'>{note}</div>" if note else ""
    return f"<div class='pf'><div class='flabel'>{label}</div>{n}<div class='fline'></div></div>"

def check(label):
    return f"<div class='pchk'><span class='box'></span>{label}</div>"


NAV_SVG = """<svg width='179' height='46' viewBox='-26 -18 906 220' xmlns='http://www.w3.org/2000/svg' aria-label='INSITE'><rect x="0" y="0" width="40" height="40" fill="#1A3E6C"/><rect x="48" y="0" width="40" height="40" fill="#1A3E6C"/><rect x="96" y="0" width="40" height="40" fill="#1A3E6C"/><rect x="144" y="0" width="40" height="40" fill="#1A3E6C"/><rect x="192" y="0" width="40" height="40" fill="#1A3E6C"/><rect x="240" y="0" width="40" height="40" fill="#1A3E6C"/><rect x="0" y="48" width="40" height="40" fill="#1A3E6C"/><rect x="48" y="48" width="40" height="40" fill="#1A3E6C"/><rect x="96" y="48" width="40" height="40" fill="#1A3E6C"/><rect x="144" y="48" width="40" height="40" fill="#8DB87A"/><rect x="192" y="48" width="40" height="40" fill="#8DB87A"/><rect x="240" y="48" width="40" height="40" fill="#8DB87A"/><rect x="0" y="96" width="40" height="40" fill="#1A3E6C"/><rect x="48" y="96" width="40" height="40" fill="#8DB87A"/><rect x="96" y="96" width="40" height="40" fill="#1A3E6C"/><rect x="144" y="96" width="40" height="40" fill="#1A3E6C"/><rect x="192" y="96" width="40" height="40" fill="#8DB87A"/><rect x="240" y="96" width="40" height="40" fill="#8DB87A"/><rect x="0" y="144" width="40" height="40" fill="#1A3E6C"/><rect x="48" y="144" width="40" height="40" fill="#1A3E6C"/><rect x="96" y="144" width="40" height="40" fill="#1A3E6C"/><rect x="144" y="144" width="40" height="40" fill="#1A3E6C"/><rect x="194" y="146" width="36" height="36" fill="#ECF4FC" stroke="#1A3E6C" stroke-width="4"/><rect x="242" y="146" width="36" height="36" fill="#ECF4FC" stroke="#1A3E6C" stroke-width="4"/><text x='314' y='138' font-family='Helvetica,Arial,sans-serif' font-weight='bold' font-size='120' letter-spacing='8' fill='#1A3E6C'>INSITE</text><text x='782' y='44' font-family='Helvetica,Arial,sans-serif' font-size='36' fill='#1A3E6C'>&#8482;</text></svg>"""

NAV_LINKS=[("index.html","Home"),
           ("developers.html","Developers"),
           ("qualify.html","Do I Qualify?"),
           ("fee_estimator.html","Fee Estimator"),
           ("developer_application.html","Apply"),
           ("manual.html","Manual")]

def site_nav():
    """On-screen navigation back to the site. Hidden in print: see @media print .mnav."""
    links="".join(
        (f"<a href='{h}' style='color:#3E7C59;font-weight:bold'>{x}</a>" if h=="manual.html"
         else f"<a href='{h}'>{x}</a>")
        for h,x in NAV_LINKS)
    return ("<div class='mnav'><div class='mnavin'>"
            f"<a href='index.html' style='display:flex;align-items:center;gap:12px'>{NAV_SVG}</a>"
            f"<div class='mnavlinks'>{links}</div></div></div>")

FORM = f"""
<p>Complete and return to HGF Management Company, or apply online through the program website.</p>
<div class='pfgrid'>
{field('Applicant name')}
{field('Development entity')}
{field('Email')}
{field('Phone')}
{field('Project name')}
{field('Jurisdiction','Name the city OR the county, e.g. Sacramento City, or Sacramento County unincorporated')}
{field('Number of lots')}
{field('Lot status','Raw land, tentative map, final map, entitled, or permits in hand')}
{field('Estimated public impact fees ($)')}
</div>
<h3 style='margin-top:18px'>Check what you can attach today</h3>
<p style='margin:4px 0 10px'>Missing items don't stop the application; the rest is collected during underwriting.</p>
{check('Preliminary title report')}
{check('Tract or parcel map')}
{check('Project budget')}
{check("Jurisdiction fee schedule")}
{check('Entitlement status documentation')}
{check('Entity formation documents')}
<div class='pfgrid' style='margin-top:22px'>
{field('Notes')}
{field('Signature and date')}
</div>
"""

page=f"""<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
<title>INSITE Developer Manual</title><style>
:root{{--navy:#153A5B;--green:#3E7C59;--line:#d3dae3;--light:#F5F7FA;--slate:#6B7280;--ink:#26303a}}
*{{box-sizing:border-box}}body{{margin:0;font-family:Helvetica,Arial,sans-serif;color:var(--ink);line-height:1.5}}
.titlepage{{min-height:92vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:10px;background:#fff;position:relative}}
.tnotice{{position:absolute;left:0;right:0;bottom:0.5in;margin:0 auto;max-width:5.6in;color:var(--slate);font-size:11px;line-height:1.5;text-align:center}}
.ttitle{{font-size:34px;font-weight:bold;color:var(--navy);letter-spacing:6px;margin-top:26px}}
.tsub{{font-size:14px;color:var(--slate)}}
.tdate{{font-size:13px;color:var(--slate)}}
.mwrap{{max-width:900px;margin:0 auto;padding:10px 22px 60px}}
h1{{font-size:28px;color:var(--navy)}}h2,h3{{color:var(--navy)}}
.wrap{{max-width:900px;margin:0 auto;padding:0}}
section{{padding:22px 0;border-bottom:1px solid var(--line)}}
.mnav{{background:#fff;border-bottom:2px solid var(--navy);position:sticky;top:0;z-index:20}}
.mnavin{{max-width:1120px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:12px 22px;flex-wrap:wrap;gap:10px}}
.mnavlinks{{display:flex;flex-wrap:wrap;gap:4px 18px;padding:14px 0}}
.mnavlinks a{{color:var(--navy);text-decoration:none;font-size:14px;letter-spacing:.3px}}
.mnavlinks a:hover{{color:var(--green)}}
.printbar{{text-align:right;padding:14px 22px;max-width:900px;margin:0 auto}}
.printbtn{{background:var(--green);color:#fff;border:0;padding:10px 18px;font-size:15px;cursor:pointer}}
img{{max-width:100%;height:auto}} a{{color:var(--green)}}
.partcap{{background:var(--light);border-left:5px solid var(--green);padding:10px 16px;margin:30px 0 8px;font-weight:bold;color:var(--navy);letter-spacing:1px}}
.pf{{margin:0 0 20px}}
.flabel{{font-weight:bold;font-size:13.5px;color:var(--navy)}}
.fnote{{font-size:11.5px;color:var(--slate);margin-top:1px}}
.fline{{border-bottom:1.4px solid var(--ink);height:26px}}
.pfgrid{{display:grid;grid-template-columns:1fr 1fr;gap:6px 34px}}
.pchk{{font-size:14px;margin:7px 0;display:flex;align-items:center;gap:10px}}
.pchk .box{{display:inline-block;width:15px;height:15px;border:1.6px solid var(--ink);flex:0 0 15px}}
@media(max-width:640px){{.pfgrid{{grid-template-columns:1fr}}}}
@page{{size:Letter;margin:14mm 14mm 16mm}}
@media print{{
 .mnav{{display:none}}
 .printbar{{display:none}}
 .titlepage{{height:8.6in;min-height:0;page-break-after:always;break-after:page}}
 .partcap{{page-break-before:always;break-before:page;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
 section,.pf,.pchk,img,.stat,.honest,.note,.ex,.exgrid{{page-break-inside:avoid;break-inside:avoid}}
 h1,h2,h3{{page-break-after:avoid;break-after:avoid}}
 .pf{{margin:0 0 13px}}
 .pchk{{margin:5px 0}}
 .pfgrid{{gap:4px 34px}}
 a{{color:var(--ink);text-decoration:none}}
}}
</style></head><body>
{site_nav()}
<div class='printbar'><button class='printbtn' onclick='window.print()'>Print / Save as PDF</button></div>
<div class='titlepage'>
{title_logo_svg()}
<div class='ttitle'>DEVELOPER MANUAL</div>
<div class='tsub'>Prepared by HGF Management Company, Program Administrator</div>
<div class='tdate'>{datetime.datetime.now(ZoneInfo('America/Los_Angeles')).strftime('%B %d, %Y')}</div>
<div class='tnotice'>INSITE&#8482; is a pre-launch program concept administered by HGF Management Company. This manual is compiled from the program website for reference and is not an offer of financing, legal advice, or investment advice. Program structure, eligibility, costs, and pricing are subject to issuer approval, bond counsel review, and program underwriting.</div>
</div>
<div class='mwrap'>
<div class='partcap'>PART 1 &middot; THE PROGRAM IN THREE QUESTIONS</div>
{body_of('builders.html')}
<div class='partcap'>PART 2 &middot; QUALIFICATION</div>
{body_of('qualify.html')}
<div class='partcap'>PART 3 &middot; YOUR FEES, THE COMPARISON</div>
{body_of('fee_estimator.html')}
<div class='partcap'>PART 4 &middot; APPLICATION</div>
{FORM}
</div></body></html>"""
open(os.path.join(SITE,'manual.html'),'w',encoding='utf8').write(page)
print("manual.html regenerated (paginated, printable form included),",len(page),"chars")
