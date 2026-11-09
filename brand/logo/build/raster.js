const { chromium } = require('playwright'); const fs=require('fs'); const path=require('path');
(async()=>{ const dir=process.argv[2]; const b=await chromium.launch(); const p=await b.newPage();
 const jobs=[
  ['pipewright-logo-light.svg','pipewright-logo-light.png',2400],
  ['pipewright-logo-dark.svg','pipewright-logo-dark.png',2400],
  ['pipewright-logo-brass.svg','pipewright-logo-brass.png',2400],
  ['pipewright-mark-light.svg','pipewright-mark-light-1024.png',1024],
  ['pipewright-mark-dark.svg','pipewright-mark-dark-1024.png',1024],
  ['pipewright-mark-brass.svg','pipewright-mark-brass-1024.png',1024],
  ['pipewright-mark-light.svg','favicon-32.png',32],
  ['pipewright-mark-light.svg','apple-touch-icon-180.png',180],
 ];
 for (const [src,out,w] of jobs){
  const svg=fs.readFileSync(path.join(dir,src),'utf8');
  const vb=svg.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/); const h=Math.round(w*vb[2]/vb[1]);
  await p.setViewportSize({width:w,height:h});
  await p.setContent(`<html><body style="margin:0;background:transparent">${svg.replace(/width="[\d.]+" height="[\d.]+"/,`width="${w}" height="${h}"`)}</body></html>`);
  await p.screenshot({path:path.join(dir,out),omitBackground:true,clip:{x:0,y:0,width:w,height:h}});
 }
 // preview sheet
 const img=f=>'data:image/svg+xml;base64,'+fs.readFileSync(path.join(dir,f)).toString('base64');
 await p.setViewportSize({width:1200,height:600});
 await p.setContent(`<html><body style="margin:0;font-family:sans-serif">
 <div style="display:grid;grid-template-columns:1fr 1fr;">
 <div style="background:#EDF0EE;padding:50px;height:200px;display:grid;place-items:center"><img src="${img('pipewright-logo-light.svg')}" style="width:480px"></div>
 <div style="background:#0E1415;padding:50px;height:200px;display:grid;place-items:center"><img src="${img('pipewright-logo-dark.svg')}" style="width:480px"></div>
 <div style="background:#6e2208;padding:50px;height:200px;display:grid;place-items:center"><img src="${img('pipewright-logo-brass.svg')}" style="width:480px"></div>
 <div style="background:#fff;padding:50px;height:200px;display:flex;gap:40px;align-items:center;justify-content:center">
  <img src="${img('pipewright-mark-light.svg')}" style="width:110px"><img src="${img('pipewright-mark-dark.svg')}" style="width:110px;background:#0E1415;border-radius:14px;padding:8px"><img src="${img('pipewright-mark-brass.svg')}" style="width:110px;background:#6e2208;border-radius:14px;padding:8px"></div>
 </div></body></html>`);
 await p.waitForTimeout(300); await p.screenshot({path:path.join(dir,'../logo-sheet.png')});
 await b.close(); })();
