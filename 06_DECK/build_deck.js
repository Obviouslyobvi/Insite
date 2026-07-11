const pptxgen = require("pptxgenjs");
const NAVY="153A5B", GREEN="3E7C59", SLATE="6B7280", LIGHT="F5F7FA", INK="26303A", PALE="CFE0EE";
const p = new pptxgen();
p.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
const W=13.33, H=7.5;
const GREENS = new Set(["1,3","2,2","2,3","3,1","3,2"]);
function grid(s, x, y, cell, gap, invert){
  for(let r=0;r<4;r++) for(let c=0;c<4;c++){
    const g = GREENS.has(r+","+c);
    const fill = g ? GREEN : (invert ? "FFFFFF" : NAVY);
    s.addShape("rect",{x:x+c*(cell+gap), y:y+r*(cell+gap), w:cell, h:cell, fill:{color:fill}});
  }
}
function titleBar(s, kicker, title){
  s.addShape("rect",{x:0,y:0,w:W,h:1.02,fill:{color:NAVY}});
  grid(s, 0.42, 0.18, 0.15, 0.04);
  s.addText(kicker,{x:1.35,y:0.10,w:9.4,h:0.32,fontFace:"Arial",fontSize:10.5,color:"9FD0B4",charSpacing:2,bold:true});
  s.addText(title,{x:1.35,y:0.36,w:11.4,h:0.6,fontFace:"Arial",fontSize:22,color:"FFFFFF",bold:true});
  s.addShape("rect",{x:0,y:1.02,w:W,h:0.045,fill:{color:GREEN}});
}
function foot(s,n){
  s.addText("INSITE (TM) Development Impact Fee Financing Program  |  Pre-launch  |  HGF Management Company  |  July 2026",
   {x:0.42,y:H-0.34,w:10.5,h:0.25,fontFace:"Arial",fontSize:8,color:SLATE});
  s.addText(String(n),{x:W-0.7,y:H-0.34,w:0.4,h:0.25,fontFace:"Arial",fontSize:8,color:SLATE,align:"right"});
}
function bullets(s, items, x,y,w,h,size){
  s.addText(items.map((t,i)=>({text:t,options:{bullet:{code:"2022",indent:12},breakLine:i<items.length-1,paraSpaceAfter:8}})),
   {x:x,y:y,w:w,h:h,fontFace:"Arial",fontSize:size||14,color:INK,valign:"top"});
}
function stat(s,x,y,w,num,lab){
  s.addShape("rect",{x:x,y:y,w:w,h:1.9,fill:{color:"FFFFFF"},line:{color:"D3DAE3",width:1}});
  s.addShape("rect",{x:x,y:y,w:w,h:0.07,fill:{color:GREEN}});
  s.addText(num,{x:x+0.15,y:y+0.18,w:w-0.3,h:0.6,fontFace:"Arial",fontSize:26,bold:true,color:NAVY});
  s.addText(lab,{x:x+0.15,y:y+0.82,w:w-0.3,h:1.0,fontFace:"Arial",fontSize:10.5,color:SLATE});
}

// 1 TITLE
let s = p.addSlide(); s.background={color:NAVY};
s.addImage({path:"/home/claude/insite/04_BRAND/INSITE_Logo_Reversed.png", x:2.62, y:2.0, w:8.1, h:2.0});
s.addText("Land-secured financing of development impact fees for small residential subdivisions in California",
 {x:1.8,y:4.25,w:9.7,h:0.7,align:"center",fontFace:"Arial",fontSize:16,color:PALE});
s.addText("Stakeholder overview  |  Pre-launch draft v1.0  |  July 2026  |  Prepared for Dennis Lanni, HGF Management Company",
 {x:1.8,y:5.05,w:9.7,h:0.4,align:"center",fontFace:"Arial",fontSize:11,color:"9FD0B4"});
s.addText("Not an offer of financing, legal advice, or investment advice. Subject to issuer approval and counsel review.",
 {x:1.8,y:6.75,w:9.7,h:0.35,align:"center",fontFace:"Arial",fontSize:9,color:"8AA3BB"});
s.addNotes("Frame: proven 1982 mechanism, new operating model for the small end. Every number in this deck has a cited source in the Claims Register.");

// 2 PROBLEM
s=p.addSlide(); titleBar(s,"THE PROBLEM","The fees are due before the first home sells");
s.addText("Impact fees fund the roads, parks, and utility capacity new residents need. Proposition 13 pushed cities toward charging new construction directly, and the Mitigation Fee Act governs how. The amounts are large, and they land at the building permit, months or years before revenue.",
 {x:0.6,y:1.35,w:12.1,h:0.85,fontFace:"Georgia",fontSize:13.5,color:INK});
stat(s,0.6,2.5,3.9,"$23,455","Average California impact fee per single-family home (2015), nearly 3x the national average. Terner Center, UC Berkeley");
stat(s,4.72,2.5,3.9,"$150,000+","Total development charges per unit in some California cities, before utility fees. Terner Center / HCD study");
stat(s,8.84,2.5,3.9,"$19,806","Average impact fee per unit on 2020-2023 affordable projects; 134 projects paid over $30,000 per unit. Terner Center, 2026");
s.addText("A ten-home project can owe several hundred thousand dollars at the permit counter.",
 {x:0.6,y:4.85,w:12.1,h:0.5,fontFace:"Arial",fontSize:15,bold:true,color:NAVY});
foot(s,2); s.addNotes("All three figures verified to Terner Center publications; URLs in the Claims Register.");

// 3 WHO IT HITS
s=p.addSlide(); titleBar(s,"WHO IT HITS","Small builders pay the most for money");
bullets(s,[
 "Projects of 2 to 50 lots rarely carry institutional credit lines; the fee bill comes from working capital or private lenders",
 "Published 2025-2026 guides price private real estate money at roughly 9.5 to 15 percent, with land at the expensive end",
 "Cash paid at the counter is cash not building homes; expensive money shrinks what small builders can deliver",
 "Large master-planned communities solved this decades ago with land-secured districts; small projects were priced out of the tool"
],0.6,1.5,12.1,3.4,15);
s.addShape("rect",{x:0.6,y:5.2,w:12.1,h:1.15,fill:{color:LIGHT},line:{color:"D3DAE3",width:1}});
s.addText("The gap is not legal capability. It is transaction economics and calendar cadence, and that is an operating-model problem.",
 {x:0.85,y:5.42,w:11.6,h:0.7,fontFace:"Georgia",fontSize:14.5,color:NAVY,italic:true});
foot(s,3); s.addNotes("Positioning: never claim no mechanism exists. The claim is that existing programs are built and priced for larger projects.");

// 4 WHY NOW
s=p.addSlide(); titleBar(s,"WHY NOW","The state is mass-producing exactly these projects");
s.addText("10",{x:0.6,y:1.7,w:2.6,h:1.7,fontFace:"Arial",fontSize:88,bold:true,color:GREEN});
s.addText("lots or fewer,\napproved ministerially",{x:0.65,y:3.35,w:2.9,h:0.8,fontFace:"Arial",fontSize:13,color:NAVY,bold:true});
bullets(s,[
 "Senate Bill 684 (effective July 2024): subdivisions of 10 or fewer lots on multifamily-zoned sites must be approved ministerially, no hearings, no discretionary review, no environmental review, on a 60-day clock",
 "Senate Bill 1123 (effective July 2025): the same fast lane extends to vacant single-family-zoned lots up to 1.5 acres",
 "Cities including Los Angeles have published implementation checklists; the pipeline grows by statute",
 "Every one of these projects meets the fee counter at the building permit"
],3.9,1.5,8.8,4.6,14.5);
foot(s,4); s.addNotes("Sources: Allen Matkins analysis, ABAG technical assistance page, LA City Planning memo.");

// 5 MECHANISM
s=p.addSlide(); titleBar(s,"THE MECHANISM","A 44-year-old law, used as designed");
bullets(s,[
 "The Mello-Roos Community Facilities Act of 1982 (Government Code 53311 and following) lets a public agency levy a voluntary special tax inside a Community Facilities District",
 "On undeveloped land with fewer than 12 registered voters, the landowners are the electors: the developer approves the tax on their own property",
 "The approved tax becomes a recorded lien, billed and collected with the ordinary property tax bill, with a foreclosure remedy behind it",
 "Districts may finance development impact fees themselves, may cover scattered parcels, and may designate a future annexation area new projects join later",
 "Statutory protections: an occupied home's tax cannot rise more than 10 percent because a neighbor went delinquent (53321(d)); the tax can never be based on property value; every owner holds a defined prepayment right"
],0.6,1.4,12.1,5.0,14);
foot(s,5); s.addNotes("Authority chain: CDIAC Debt Financing Guide plus statute sections; PACE is an operating analogy only, never authority.");

// 6 ARCHITECTURE (map)
s=p.addSlide(); titleBar(s,"THE ARCHITECTURE","One district per city. One signature per project.");
s.addImage({path:"/home/claude/insite/00_PLAN/map_embed.png", x:0.75, y:1.25, w:11.83, h:5.45});
s.addText("Numbered flows 1-8: application, appraisal, annexation package, approval, funding, fee payment, annual levy, debt service.",
 {x:0.75,y:6.78,w:11.8,h:0.3,fontFace:"Arial",fontSize:9.5,color:SLATE});
foot(s,6); s.addNotes("Walk the 8 flows left to right; emphasize the annual servicing loop is INSITE's recurring role and revenue.");

// 7 ZONES
s=p.addSlide(); titleBar(s,"ANNEXATION MODEL","Form once. Annex forever. Zones stay separate.");
const cells=8;
for(let i=0;i<cells;i++){
  const on=i<3;
  s.addShape("rect",{x:0.7+i*0.62,y:1.55,w:0.5,h:0.5,fill:{color:on?GREEN:LIGHT},line:{color:on?GREEN:"D3DAE3",width:1.25}});
}
s.addText("Projects annex into the existing district over time; formation cost is paid once per jurisdiction.",
 {x:0.7,y:2.18,w:11.9,h:0.35,fontFace:"Arial",fontSize:11,color:SLATE});
bullets(s,[
 "A Master District is formed with a recorded Future Annexation Area on the boundary map",
 "Each project joins by the landowner's one-page Unanimous Approval, acting as the election; no hearing, no ballot",
 "Each project becomes its own tax zone with its own maximum tax table and its own note; a zone's taxes repay only that zone's debt (53339.3(d))",
 "The pattern operates today in Escondido, Chula Vista, and Roseville; INSITE standardizes and administers it for the small end"
],0.7,2.75,12.0,3.6,14.5);
foot(s,7); s.addNotes("Zone isolation is the purchaser's key comfort: no cross-collateralization between projects.");

// 8 ROLES
s=p.addSlide(); titleBar(s,"ROLES","The issuer owns every approval. INSITE does the work.");
const rows=[
 [{text:"Party",options:{bold:true,color:"FFFFFF",fill:{color:NAVY}}},{text:"Role",options:{bold:true,color:"FFFFFF",fill:{color:NAVY}}}],
 ["Public issuer (city, county, or joint powers authority)","Owns the Master District, adopts policies, approves each annexation, authorizes the special tax and notes"],
 ["INSITE (HGF Management Company)","Program administrator: intake, underwriting, appraisal management, documents and zone exhibits, funding coordination, annual administration and reporting"],
 ["Independent MAI appraiser panel","Values every project to state (CDIAC) standards; supports the value finding; never an INSITE employee"],
 ["Bond counsel, special tax consultant, tax roll administrator","Selection in progress; opinions, tax formula template, annual levy files. Contracted first per the sourcing plan"],
 ["Capital partner","Purchases each privately placed, tax-secured note"],
 ["County tax collector and property owners","Bills with the property tax; owners pay the disclosed, prepayable special tax over the note term"]
];
s.addTable(rows,{x:0.6,y:1.35,w:12.1,fontFace:"Arial",fontSize:11.5,color:INK,border:{color:"D3DAE3",pt:0.75},colW:[3.6,8.5],valign:"top",autoPage:false,rowH:0.52});
foot(s,8); s.addNotes("Credibility answer lives here: every scrutinized seat is filled by a name the audience already knows.");

// 9 UNDERWRITING
s=p.addSlide(); titleBar(s,"UNDERWRITING","Stricter than the statute, by policy");
s.addText("Value-to-lien",{x:0.6,y:1.35,w:4,h:0.35,fontFace:"Arial",fontSize:13,bold:true,color:NAVY});
s.addShape("rect",{x:0.6,y:1.8,w:3.0,h:0.55,fill:{color:"B9C9D8"}});
s.addText("3 : 1  statute (53345.8)",{x:0.7,y:1.87,w:3.4,h:0.4,fontFace:"Arial",fontSize:12,color:NAVY,bold:true});
s.addShape("rect",{x:0.6,y:2.5,w:4.0,h:0.55,fill:{color:GREEN}});
s.addText("4 : 1  INSITE policy (CSCDA precedent)",{x:0.7,y:2.57,w:4.6,h:0.4,fontFace:"Arial",fontSize:12,color:"FFFFFF",bold:true});
bullets(s,[
 "Appraisals by independent MAI professionals under the State Treasurer (CDIAC) standards the statute requires",
 "Total tax burden benchmarked at 2 percent of expected home value, per the adopted policy of the state's largest issuer; each city's own cap confirmed before sizing",
 "Illustrative sizing: 10 lots financing $250,000 over 30 years near 6 percent works out to roughly $2,300 per home per year, including administration and a 10 percent coverage cushion (arithmetic, not a quote)",
 "Inputs arrive on the standard data package (INS-201); appraisal scope per the program manual (INS-101)"
],5.0,1.35,7.7,4.9,13.5);
foot(s,9); s.addNotes("If asked why 4:1: it is CSCDA's own adopted standard; conservatism substitutes for tenure.");

// 10 MARKET
s=p.addSlide(); titleBar(s,"THE MARKET, ARITHMETIC SHOWN","62,372 units in the target segment last year");
s.addChart(p.ChartType.bar, [{
  name:"1-4 unit permits, 2025",
  labels:["Los Angeles","Riverside","Sacramento","San Diego","San Bern.","Orange","Kern","Placer","San Joaquin","Fresno"],
  values:[11422,6235,4762,4385,3771,3106,3013,2690,2522,2068]
}],{x:0.6,y:1.3,w:7.6,h:5.3,barDir:"bar",chartColors:[NAVY],showValue:true,dataLabelPosition:"outEnd",dataLabelColor:SLATE,dataLabelFontSize:9,
 catAxisLabelColor:INK,catAxisLabelFontSize:10,valAxisHidden:true,valGridLine:{style:"none"},catGridLine:{style:"none"},showLegend:false,showTitle:false});
bullets(s,[
 "California permitted 103,856 housing units in 2025; 62,372 (60.1 percent) were in 1-to-4-unit structures. U.S. Census primary files, recomputed",
 "At an assumed $25,000 of financeable public fees per unit, the measured segment is roughly $1.56 billion per year of fee obligations. The assumption is stated wherever the figure appears",
 "Projects of 5 to 50 units are excluded because public data cannot separate them from large complexes: the estimate is deliberately conservative"
],8.45,1.4,4.3,5.0,12.5);
foot(s,10); s.addNotes("If challenged on the $1.56B: show the two factors and the exclusion; the conservatism is the argument.");

// 11 COMPETITIVE
s=p.addSlide(); titleBar(s,"COMPETITIVE LANDSCAPE","Not the first. Built for a different customer.");
const crows=[
 [{text:"",options:{fill:{color:NAVY}}},{text:"SCIP (CSCDA)",options:{bold:true,color:"FFFFFF",fill:{color:NAVY}}},{text:"BOLD (CMFA)",options:{bold:true,color:"FFFFFF",fill:{color:NAVY}}},{text:"INSITE (proposed)",options:{bold:true,color:"FFFFFF",fill:{color:GREEN}}}],
 ["Mechanism","1913/1915 assessments, district option","Mello-Roos districts","Mello-Roos master district + annexation zones"],
 ["Published scale","Typically from $500,000 in fees; pooled sales about 3x per year","About $550 million, 65+ projects, 12,000+ units since 2020 (about 185 units per project)","2 to 50 lots; one small note per project, on the project's schedule"],
 ["Cadence","Pool calendar","Project issuances","Administrative annexation per deal"],
 ["Segment","Mid to large","Large","Small, purpose-built"]
];
s.addTable(crows,{x:0.6,y:1.35,w:12.1,fontFace:"Arial",fontSize:11,color:INK,border:{color:"D3DAE3",pt:0.75},colW:[1.7,3.4,3.7,3.3],valign:"top",autoPage:false});
s.addText("Both programs prove the mechanism and the market. The gap is fixed cost per transaction and calendar, which is what the operating model attacks.",
 {x:0.6,y:5.6,w:12.1,h:0.6,fontFace:"Georgia",fontSize:13.5,italic:true,color:NAVY});
foot(s,11); s.addNotes("Credit them by name, always. The honesty is the differentiator with sophisticated audiences.");

// 12 BUSINESS MODEL
s=p.addSlide(); titleBar(s,"BUSINESS MODEL","An administrator, never a lender");
bullets(s,[
 "Revenue: transaction fees at each funding, plus annual administration fees for the life of every zone (levy, collections reconciliation, delinquency monitoring, investor reporting)",
 "The Act contemplates it: district administrative expenses, including consultants, are recoverable through the special tax (53317(d))",
 "Sourcing: independence functions (counsel, appraisal) stay outside permanently; the tax roll administrator is contracted first with shadow and transition rights, then brought in-house on defined triggers",
 "The document library is the moat: standard checklist, appraisal manual, tax formula template, annexation package, workbook",
 "Every closed deal pays administration for decades; the annual book compounds"
],0.6,1.4,12.1,4.9,14.5);
foot(s,12); s.addNotes("If asked fee levels: being modeled, not quoted; consultant costs pass through the levy by statute.");

// 13 PILOT + RISKS
s=p.addSlide(); titleBar(s,"PILOT, ROLLOUT, AND WHAT COULD KILL IT","Small first, honest throughout");
s.addText("Pilot and rollout",{x:0.6,y:1.3,w:5.9,h:0.35,fontFace:"Arial",fontSize:14,bold:true,color:NAVY});
bullets(s,[
 "Pilot: a small finished-lot subdivision in the Sacramento area, financing eligible permit and impact fees; specifics publish when documents are final",
 "Phase by demand: first city direct, neighboring jurisdictions next, all documents issuer-neutral",
 "A joint powers authority is the end state, not the start: formed or joined at roughly the third jurisdiction when defined triggers fire"
],0.6,1.7,5.9,4.4,12.5);
s.addText("Risk factors, stated plainly",{x:6.9,y:1.3,w:5.8,h:0.35,fontFace:"Arial",fontSize:14,bold:true,color:NAVY});
bullets(s,[
 "Per-deal execution cost is a founder estimate ($5,000 to $30,000) until real quotes exist",
 "No purchaser committed; small-note appetite is what the pilot must prove",
 "City adoption pace; six-plus months to form each district before any JPA exists",
 "Delinquency and foreclosure timelines; trademark clearance pending; school fees excluded at launch",
 "Incumbents could move down-market"
],6.9,1.7,5.8,4.4,12.5);
foot(s,13); s.addNotes("The risk slide is the credibility slide: volunteer the failure modes before anyone hunts for them.");

// 14 STATUS + ASKS
s=p.addSlide(); s.background={color:NAVY};
grid(s,0.5,0.45,0.17,0.05,true);
s.addText("Status and asks",{x:1.5,y:0.5,w:10,h:0.6,fontFace:"Arial",fontSize:26,bold:true,color:"FFFFFF"});
s.addText("Proven today",{x:0.7,y:1.6,w:5.9,h:0.35,fontFace:"Arial",fontSize:14,bold:true,color:"9FD0B4"});
s.addText([
 {text:"The legal mechanism and live annexation precedents",options:{bullet:{code:"2022"},breakLine:true,paraSpaceAfter:6}},
 {text:"Market arithmetic from primary Census data",options:{bullet:{code:"2022"},breakLine:true,paraSpaceAfter:6}},
 {text:"A verified document library: whitepaper, claims register with source URLs, appraisal manual and RFQP, data package checklist, structure map, strategy memos, brand system, website with calculator",options:{bullet:{code:"2022"},breakLine:true,paraSpaceAfter:6}},
 {text:"Underwriting policy stricter than statute, with issuer precedent",options:{bullet:{code:"2022"}}}
],{x:0.7,y:2.0,w:5.9,h:3.6,fontFace:"Arial",fontSize:12.5,color:PALE,valign:"top"});
s.addText("Pending, and asked of this room",{x:6.9,y:1.6,w:5.8,h:0.35,fontFace:"Arial",fontSize:14,bold:true,color:"9FD0B4"});
s.addText([
 {text:"Select bond counsel, the special tax consultant, and the tax roll administrator (criteria prepared)",options:{bullet:{code:"2022"},breakLine:true,paraSpaceAfter:6}},
 {text:"A briefing with the pilot city's finance and community development staff",options:{bullet:{code:"2022"},breakLine:true,paraSpaceAfter:6}},
 {text:"Capital diligence review of the package, toward a term sheet",options:{bullet:{code:"2022"},breakLine:true,paraSpaceAfter:6}},
 {text:"Trademark clearance and the public-name decision before anything external",options:{bullet:{code:"2022"}}}
],{x:6.9,y:2.0,w:5.8,h:3.6,fontFace:"Arial",fontSize:12.5,color:PALE,valign:"top"});
s.addText("INSITE (TM) is a pre-launch program concept administered by HGF Management Company. Not an offer of financing, legal advice, or investment advice. Not an offer to sell, or a solicitation of an offer to buy, any security. Subject to issuer approval and counsel review.",
 {x:0.7,y:6.55,w:12,h:0.6,fontFace:"Arial",fontSize:9,color:"8AA3BB"});
s.addNotes("Close on the asks; the package hands over the evidence.");

p.writeFile({fileName:"INSITE_Overview_Deck.pptx"}).then(()=>console.log("deck written"));
