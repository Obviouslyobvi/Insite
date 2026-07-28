#!/usr/bin/env python3
"""Build the investor portal (encrypted) and the INS-303 public edition from section tags.
Usage: build_portal.py <password>
Reads 02_PROGRAM/INS-303_Investor_Guide.md. Sections whose tag begins PORTAL go behind
the login; the public edition replaces them with a pointer. Password is never written
to the repo; only ciphertext is emitted."""
import re, sys, json, os, base64, hashlib, secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

SRC='02_PROGRAM/INS-303_Investor_Guide.md'
PORTAL_HTML='05_WEBSITE/portal.html'
PUB_MD='02_PROGRAM/INS-303_Investor_Guide_PUBLIC_EDITION.md'

def split_sections(text):
    """Return list of (kind, content). kind: 'head' for chapter/part headings, 'sec' for **N.N ...** blocks."""
    lines=text.split('\n')
    out=[]; buf=[]
    for ln in lines:
        if re.match(r'\*\*\d+\.\d+ ', ln) or ln.startswith('#'):
            if buf: out.append(buf); buf=[]
        buf.append(ln)
    if buf: out.append(buf)
    return ['\n'.join(b) for b in out]

def is_portal(block):
    m=re.match(r'\*\*(\d+\.\d+)([^*]*)\*\*\s*(PORTAL)', block)
    return bool(m)

def sec_id(block):
    m=re.match(r'\*\*(\d+\.\d+)\s+([^.*]+)', block)
    return (m.group(1), m.group(2).strip()) if m else (None,None)

def md_to_html(md):
    h=md
    h=re.sub(r'^### (.*)$', r'<h3>\1</h3>', h, flags=re.M)
    h=re.sub(r'^## (.*)$', r'<h2>\1</h2>', h, flags=re.M)
    h=re.sub(r'^# (.*)$', r'<h1>\1</h1>', h, flags=re.M)
    h=re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', h)
    h=re.sub(r'^\| (.*) \|$', lambda m:'<div class="tr">'+m.group(1).replace(' | ',' &middot; ')+'</div>', h, flags=re.M)
    paras=[p.strip() for p in h.split('\n\n') if p.strip()]
    return '\n'.join(p if p.startswith('<h') or p.startswith('<div') else '<p>'+p+'</p>' for p in paras)

def main():
    pw=sys.argv[1]
    text=open(SRC).read()
    blocks=split_sections(text)
    portal_blocks=[]; public_blocks=[]
    for b in blocks:
        if is_portal(b):
            num,title=sec_id(b)
            portal_blocks.append(b)
            public_blocks.append(f'**{num} {title}.** This section is available in the investor portal. Access is provided to qualified capital partners under review by HGF Management Company.')
        else:
            public_blocks.append(b)
    # public edition markdown
    pub='\n\n'.join(public_blocks)
    pub=pub.replace('# INS-303: Investor Guide','# INS-303: Investor Guide, Public Edition')
    open(PUB_MD,'w').write(pub)

    # portal payload html
    inner=md_to_html('\n\n'.join(portal_blocks))
    payload=('<div class="kicker">INVESTOR PORTAL &middot; CONFIDENTIAL &middot; PRE-LAUNCH</div>'
             '<h1>INS-303: the portal sections</h1>'
             '<p class="lede">The sections below are the portal-designated portions of the Investor Guide, per the founder\'s approved split of July 24, 2026. Sections marked as bond counsel gates remain reserved and fill in on counsel\'s determinations. Provided for diligence under review; not an offer.</p>'
             +inner+
             '<p style="font-style:italic;margin-top:26px">INSITE(TM) is a pre-launch program concept administered by HGF Management Company. This material is not an offer of financing, legal advice, or investment advice. Program structure, eligibility, costs, and pricing are subject to issuer approval, bond counsel review, and program underwriting. Figures identified as targets or estimates are the founder\'s working numbers, not commitments. This page is not an offer to sell, or a solicitation of an offer to buy, any security.</p>')

    salt=secrets.token_bytes(16); iv=secrets.token_bytes(12)
    key=hashlib.pbkdf2_hmac('sha256', pw.encode(), salt, 200000, dklen=32)
    ct=AESGCM(key).encrypt(iv, payload.encode(), None)
    b64=lambda x: base64.b64encode(x).decode()

    page=f"""<!doctype html><html lang='en'><head><meta charset='utf-8'>
<meta name='viewport' content='width=device-width,initial-scale=1'><meta name='robots' content='noindex'>
<title>INSITE Investor Portal</title><style>
:root{{--navy:#153A5B;--green:#2E7D4F;--light:#f4f7f9;--line:#d9e2e8;--ink:#26303a}}
body{{margin:0;font-family:Helvetica,Arial,sans-serif;color:var(--ink);background:var(--light)}}
.top{{background:var(--navy);color:#fff;padding:20px 24px;font-size:18px;letter-spacing:1px;font-weight:bold}}
.gate{{max-width:420px;margin:9vh auto;background:#fff;border:1px solid var(--line);padding:30px}}
.gate h1{{color:var(--navy);font-size:22px;margin:0 0 6px}}
.gate p{{font-size:14px;line-height:1.5}}
input{{width:100%;padding:11px;border:1px solid var(--line);font-size:16px;box-sizing:border-box;margin:12px 0 4px}}
button{{width:100%;padding:12px;background:var(--navy);color:#fff;border:0;font-size:15px;cursor:pointer;margin-top:10px}}
#err{{color:#a33;font-size:13px;min-height:18px}}
#content{{display:none;max-width:820px;margin:26px auto;background:#fff;border:1px solid var(--line);padding:34px 38px;line-height:1.6}}
#content h1{{color:var(--navy)}} #content h2,#content h3{{color:var(--navy);border-bottom:2px solid var(--green);padding-bottom:4px}}
.kicker{{color:var(--green);font-weight:bold;letter-spacing:2px;font-size:12px}}
.lede{{font-size:16px;color:#44515c}} .tr{{font-size:13px;padding:4px 0;border-bottom:1px solid var(--line)}}
small.foot{{display:block;text-align:center;color:#666;margin:20px}}
</style></head><body>
<div class='top'>INSITE&#8482; INVESTOR PORTAL</div>
<div class='gate' id='gate'>
<h1>Access for capital partners under review</h1>
<p>This area holds the portal-designated sections of the Investor Guide. Access credentials are provided by HGF Management Company. Nothing here is an offer of financing or securities.</p>
<input type='password' id='pw' placeholder='Access phrase' autocomplete='off'>
<div id='err'></div><button id='go'>Enter</button>
</div>
<div id='content'></div>
<small class='foot'>INSITE&#8482; is a pre-launch program concept administered by HGF Management Company.</small>
<script>
const SALT='{b64(salt)}', IV='{b64(iv)}', CT='{b64(ct)}';
function b2a(b64){{const s=atob(b64);const a=new Uint8Array(s.length);for(let i=0;i<s.length;i++)a[i]=s.charCodeAt(i);return a}}
async function unlock(){{
 const pw=document.getElementById('pw').value;
 document.getElementById('err').textContent='';
 try{{
  const km=await crypto.subtle.importKey('raw',new TextEncoder().encode(pw),'PBKDF2',false,['deriveKey']);
  const key=await crypto.subtle.deriveKey({{name:'PBKDF2',salt:b2a(SALT),iterations:200000,hash:'SHA-256'}},km,{{name:'AES-GCM',length:256}},false,['decrypt']);
  const pt=await crypto.subtle.decrypt({{name:'AES-GCM',iv:b2a(IV)}},key,b2a(CT));
  document.getElementById('content').innerHTML=new TextDecoder().decode(pt);
  document.getElementById('content').style.display='block';
  document.getElementById('gate').style.display='none';
 }}catch(e){{document.getElementById('err').textContent='That phrase does not unlock this portal.';}}
}}
document.getElementById('go').addEventListener('click',unlock);
document.getElementById('pw').addEventListener('keydown',e=>{{if(e.key==='Enter')unlock()}});
</script></body></html>"""
    open(PORTAL_HTML,'w').write(page)
    print(f"portal sections: {len(portal_blocks)} | public edition written | portal.html {os.path.getsize(PORTAL_HTML)} bytes")

if __name__=='__main__': main()
