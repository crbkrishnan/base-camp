// Drives each IOQM page's two machines in jsdom: poses every puzzle, solves it through the UI, checks S.puzzles rises.
// Usage: node tools/legacy/ioqm/test_tools.js [page.html]   (from the repo root)
const path = require('path');
const { JSDOM, VirtualConsole } = require('jsdom');
const fs = require('fs');
const dir = path.resolve(__dirname, '..', '..', '..');

const TESTS = {
 'ioqm-divisors.html': `
   const out=[];
   for(let r=0;r<12;r++){
     document.getElementById('benchPuzzle').click();
     const T=benchTarget; let done=false;
     for(let d=0; d<10 && !done; d++){
       const s=T.p.replace('*',d); if(s[0]==='0') continue;
       if(T.by.every(k=>BigInt(s)%BigInt(k)===0n)){ const i=document.getElementById('dnum'); i.value=s; i.dispatchEvent(new Event('input')); done=true; }
     }
     out.push(benchTarget===null);
   }
   for(let r=0;r<12;r++){
     document.getElementById('gridPuzzle').click();
     const T=gridTarget; let best=null,bp=null;
     for(let a=0;a<=5;a++)for(let b=0;b<=4;b++)for(let c=0;c<=2;c++) if((a+1)*(b+1)*(c+1)===T){const n=2**a*3**b*5**c; if(best===null||n<best){best=n;bp=[a,b,c];}}
     ['ga','gb','gc'].forEach((id,k)=>{const e=document.getElementById(id); e.value=bp[k]; e.dispatchEvent(new Event('input'));});
     out.push(gridTarget===null);
   }
   [out.every(Boolean), S.puzzles];`,
 'ioqm-remainders.html': `
   const out=[];
   const setv=(id,v,ev)=>{const e=document.getElementById(id); e.value=v; e.dispatchEvent(new Event(ev||'input'));};
   for(let r=0;r<12;r++){
     document.getElementById('clockPuzzle').click();
     const T=clockTarget; let n=T.lo; while(!T.c.every(([m,q])=>n%m===q)) n++;
     setv('ca', n); out.push(clockTarget===null);
   }
   for(let r=0;r<12;r++){
     document.getElementById('cycPuzzle').click();
     const T=cycTarget; setv('yb',T.b); setv('ym',T.m,'change');
     let n=T.lo; while(powMod(T.b,n,T.m)!==T.want) n++;
     setv('yn', n); out.push(cycTarget===null);
   }
   [out.every(Boolean), S.puzzles];`,
 'ioqm-identities.html': `
   const out=[];
   const setv=(id,v)=>{const e=document.getElementById(id); e.value=v; e.dispatchEvent(new Event('input'));};
   for(let r=0;r<12;r++){
     document.getElementById('sqPuzzle').click();
     const P=sqTarget; let found=null;
     for(let a=1;a<=12&&!found;a++) for(let b=1;b<=12&&!found;b++){
       if(P.mode==='diff' && a>b && a*a-b*b===P.t) found=[a,b];
       if(P.mode==='sq' && a+b===P.s && a*b===P.p) found=[a,b];
     }
     document.getElementById(P.mode==='diff'?'modeDiff':'modeSq').click();
     setv('sa',found[0]); setv('sb',found[1]); out.push(sqTarget===null);
   }
   for(let r=0;r<12;r++){
     document.getElementById('bPuzzle').click();
     const T=bTarget; let f=null;
     for(let x=1;x<=15&&!f;x++) for(let y=1;y<=15&&!f;y++) if(x*y+x+y===T.t) f=[x,y];
     setv('bx',f[0]); setv('by',f[1]); out.push(bTarget===null);
   }
   [out.every(Boolean), S.puzzles];`,
 'ioqm-sequences.html': `
   const out=[];
   const setv=(id,v)=>{const e=document.getElementById(id); e.value=v; e.dispatchEvent(new Event('input'));};
   for(let r=0;r<12;r++){
     document.getElementById('stPuzzle').click();
     const T=stTarget; let f=null;
     for(let a=1;a<=30&&!f;a++) for(let d=1;d<=5&&!f;d++) for(let n=1;n<=30&&!f;n++){
       const ok=Object.keys(T.fix).every(k=>({a,d,n})[k]===T.fix[k]);
       if(ok && n*(2*a+(n-1)*d)===2*T.sum) f=[a,d,n];
     }
     setv('sta',f[0]); setv('std',f[1]); setv('stn',f[2]); out.push(stTarget===null);
   }
   for(let r=0;r<12;r++){
     document.getElementById('fPuzzle').click();
     const T=fTarget; setv('fs',T.s);
     const want=T.area==='max'?T.s*T.s/4:T.area; let x=0; while(x*(T.s-x)!==want) x++;
     setv('fx',x); out.push(fTarget===null);
   }
   [out.every(Boolean), S.puzzles];`,
 'ioqm-angles.html': `
   const out=[];
   const setv=(id,v)=>{const e=document.getElementById(id); e.value=v; e.dispatchEvent(new Event('input'));};
   for(let r=0;r<12;r++){
     document.getElementById('tPuzzle').click();
     const T=tTarget; let f=null;
     for(let A=5;A<=170&&!f;A+=5) for(let B=5;B<=170&&!f;B+=5){ if(A+B<180 && T.check(A,B,180-A-B)) f=[A,B]; }
     setv('tA',f[0]); setv('tB',f[1]); out.push(tTarget===null);
   }
   for(let r=0;r<12;r++){
     document.getElementById('pPuzzle').click();
     setv('pn',pTarget.n); out.push(pTarget===null);
   }
   [out.every(Boolean), S.puzzles];`,
 'ioqm-areas.html': `
   const out=[];
   const setv=(id,v)=>{const e=document.getElementById(id); e.value=v; e.dispatchEvent(new Event('input'));};
   for(let r=0;r<12;r++){
     document.getElementById('aPuzzle').click();
     const T=aTarget; let f=null;
     for(let b=2;b<=12&&!f;b++) for(let h=1;h<=10&&!f;h++) for(let o=-6;o<=18&&!f;o++) if(T.check(b,h,o)) f=[b,h,o];
     setv('ab',f[0]); setv('ao',f[2]); setv('ah',f[1]); out.push(aTarget===null);
   }
   for(let r=0;r<12;r++){
     document.getElementById('p2Puzzle').click();
     const T=pyTarget; let f=null;
     for(let a=1;a<=20&&!f;a++) for(let b=1;b<=20&&!f;b++) if(T.check(a,b,Math.sqrt(a*a+b*b))) f=[a,b];
     setv('pa',f[0]); setv('pb',f[1]); out.push(pyTarget===null);
   }
   [out.every(Boolean), S.puzzles];`,
 'ioqm-counting.html': `
   const out=[];
   const setv=(id,v)=>{const e=document.getElementById(id); e.value=v; e.dispatchEvent(new Event('input'));};
   for(let r=0;r<12;r++){
     document.getElementById('gPuzzle').click();
     const T=gTarget;
     if(T.grid){
       setv('gw',T.grid[0]); setv('gh',T.grid[1]);
       let done=false;
       for(let i=0;i<=T.grid[0]&&!done;i++) for(let j=0;j<=T.grid[1]&&!done;j++){
         const k=i+','+j; if(k==='0,0'||k===T.grid.join(',')) continue;
         const N=pathCounts(T.grid[0],T.grid[1],new Set([k]));
         if(N[T.grid[0]][T.grid[1]]===T.count){ document.querySelector('[data-n="'+k+'"]').dispatchEvent(new MouseEvent('click',{bubbles:true})); done=true; }
       }
     }else{
       let f=null; for(let w=1;w<=8&&!f;w++) for(let h=1;h<=6&&!f;h++) if(C(w+h,h)===T.count) f=[w,h];
       setv('gw',f[0]); setv('gh',f[1]);
     }
     out.push(gTarget===null);
   }
   for(let r=0;r<12;r++){
     document.getElementById('cPuzzle').click();
     const T=cTarget;
     if(T.kind!=='diag') document.getElementById(T.kind==='pairs'?'cPairs':'cTrips').click();
     let n=2; const f=n=>T.kind==='pairs'?n*(n-1)/2:T.kind==='trips'?n*(n-1)*(n-2)/6:n*(n-1)/2-n;
     while(f(n)!==T.v) n++;
     setv('cn',n); out.push(cTarget===null);
   }
   [out.every(Boolean), S.puzzles];`,
 'ioqm-logic.html': `
   const out=[];
   const setv=(id,v,ev)=>{const e=document.getElementById(id); e.value=v; e.dispatchEvent(new Event(ev||'input'));};
   for(let r=0;r<12;r++){
     document.getElementById('hPuzzle').click();
     const T=hTarget; setv('hn',T.n); setv('hk',T.n*(T.t-1)+1); out.push(hTarget===null);
   }
   const clickSq=k=>document.querySelector('[data-k="'+k+'"]').dispatchEvent(new MouseEvent('click',{bubbles:true}));
   for(let r=0;r<12;r++){
     document.getElementById('blPuzzle').click();
     const T=blTarget; setv('bsz',T.n,'change');
     const n=T.n, all=[]; for(let a=0;a<n;a++) for(let b=0;b<n;b++) all.push(a+','+b);
     const sizes={2:2,1:1,4:4}; let want = T.txt.includes('exactly 4')?4: T.txt.includes('exactly 1')?1:2;
     let found=null;
     const tryset=ks=>{ const R=new Set(ks); let d=0,l=0; for(let a=0;a<n;a++) for(let b=0;b<n;b++){ if(R.has(a+','+b)) continue; ((a+b)%2===0)?d++:l++; } return T.check(R,d,l,tilingExists(n,R)); };
     if(want===1){ for(const k of all){ if(tryset([k])){found=[k];break;} } }
     else if(want===2){ outer: for(let i=0;i<all.length;i++) for(let j=i+1;j<all.length;j++){ if(tryset([all[i],all[j]])){found=[all[i],all[j]];break outer;} } }
     else { found=['0,1','1,0','2,2','3,3'].filter(()=>true); if(!tryset(found)) found=null; }
     found.forEach(clickSq); out.push(blTarget===null);
   }
   [out.every(Boolean), S.puzzles];`,
};

(async () => {
  let bad = 0;
  const only = process.argv[2];
  for (const [f, code] of Object.entries(TESTS)) {
    if (only && f !== only) continue;
    const errors = [];
    const vc = new VirtualConsole();
    vc.on('jsdomError', e => errors.push(e.message.split('\n')[0]));
    const dom = new JSDOM(fs.readFileSync(dir + '/' + f, 'utf8'), { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://example.org/' + f, virtualConsole: vc });
    await new Promise(r => setTimeout(r, 400));
    dom.window.confirm = () => true;
    let res;
    try { res = dom.window.eval(code); } catch (e) { errors.push('test: ' + e.message); }
    const okAll = res && res[0] && !errors.length;
    if (!okAll) bad++;
    console.log((okAll ? 'ok  ' : 'FAIL') + '  ' + f.padEnd(24) + ' puzzles solved=' + (res ? res[1] : '?'));
    errors.slice(0, 4).forEach(e => console.log('     ! ' + e));
    dom.window.close();
  }
  process.exit(bad ? 1 : 0);
})();
