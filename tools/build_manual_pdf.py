#!/usr/bin/env python3
"""build_manual_pdf.py - renders 05_WEBSITE/manual.html to manual.pdf in the INS publication
layout: bare white title page, then interior pages carrying the running header band (horizontal
logo, hairline rule, DEVELOPER MANUAL label) and a numbered footer, per INS-001 header/footer
design. Run after build_manual.py."""
import os, re, base64, io, http.server, socketserver, threading, functools, time
from PIL import Image
from playwright.sync_api import sync_playwright
try: import fitz
except ImportError: raise SystemExit("pymupdf required")

HERE=os.path.dirname(os.path.abspath(__file__)); SITE=os.path.join(os.path.dirname(HERE),'05_WEBSITE')
src=open(os.path.join(SITE,'manual.html'),encoding='utf8').read()

im=Image.open(os.path.join(os.path.dirname(HERE),'04_BRAND','INSITE_Logo_Horizontal.png')).convert('RGB')
im.thumbnail((400,92),Image.LANCZOS); buf=io.BytesIO(); im.save(buf,'PNG')
LOGO="data:image/png;base64,"+base64.b64encode(buf.getvalue()).decode()

title_only=re.sub(r"<div class='mwrap'>.*</div>\s*</body>","</body>",src,flags=re.S)
title_only=title_only.replace("<div class='printbar'><button class='printbtn' onclick='window.print()'>Print / Save as PDF</button></div>","")
body_only=re.sub(r"<div class='titlepage'>.*?</div>\n<div class='mwrap'>","<div class='mwrap'>",src,flags=re.S)
body_only=body_only.replace("<div class='printbar'><button class='printbtn' onclick='window.print()'>Print / Save as PDF</button></div>","")
open(os.path.join(SITE,'_m_title.html'),'w',encoding='utf8').write(title_only)
open(os.path.join(SITE,'_m_body.html'),'w',encoding='utf8').write(body_only)

HEADER=("<div style='width:100%;font-size:8px;padding:0 14mm;'>"
        "<div style='display:flex;justify-content:space-between;align-items:center;"
        "border-bottom:1.4px solid #153A5B;padding:4px 0 5px;'>"
        f"<img src='{LOGO}' style='height:22px'/>"
        "<span style='font-family:Helvetica,Arial,sans-serif;color:#153A5B;font-size:8.5px;"
        "letter-spacing:1.5px;font-weight:bold'>DEVELOPER MANUAL</span></div></div>")
FOOTER=("<div style='width:100%;font-size:8px;padding:0 14mm;font-family:Helvetica,Arial,sans-serif;color:#6B7280;'>"
        "<div style='display:flex;justify-content:space-between;border-top:1px solid #d3dae3;padding-top:4px;'>"
        "<span>HGF MANAGEMENT COMPANY</span>"
        "<span>PAGE <span class='pageNumber'></span></span></div></div>")

H=functools.partial(http.server.SimpleHTTPRequestHandler,directory=SITE)
httpd=socketserver.TCPServer(("127.0.0.1",0),H); port=httpd.server_address[1]
threading.Thread(target=httpd.serve_forever,daemon=True).start(); time.sleep(0.3)
with sync_playwright() as pl:
    b=pl.chromium.launch()
    pg=b.new_page(); pg.goto(f"http://127.0.0.1:{port}/_m_title.html",wait_until="networkidle"); pg.wait_for_timeout(250)
    pg.pdf(path="/tmp/_m_title.pdf",format="Letter",print_background=True)
    pg.goto(f"http://127.0.0.1:{port}/_m_body.html",wait_until="networkidle"); pg.wait_for_timeout(400)
    pg.pdf(path="/tmp/_m_body.pdf",format="Letter",print_background=True,
           display_header_footer=True, header_template=HEADER, footer_template=FOOTER,
           margin={"top":"24mm","bottom":"18mm","left":"14mm","right":"14mm"})
    pg.close(); b.close()
httpd.shutdown()
doc=fitz.open("/tmp/_m_title.pdf"); doc.insert_pdf(fitz.open("/tmp/_m_body.pdf"))
out=os.path.join(SITE,'manual.pdf'); doc.save(out)
os.remove(os.path.join(SITE,'_m_title.html')); os.remove(os.path.join(SITE,'_m_body.html'))
print(f"manual.pdf written: {doc.page_count} pages, {os.path.getsize(out):,} bytes")
