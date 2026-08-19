// Loads each page in a real DOM and reports uncaught errors plus what rendered.
const { JSDOM, VirtualConsole } = require('jsdom');
const fs = require('fs');
const path = require('path');

const dir = process.argv[2] || '/home/claude/hub';
const files = process.argv[3] ? [process.argv[3]] : fs.readdirSync(dir).filter(f => f.endsWith('.html'));

(async () => {
  let bad = 0;
  for (const f of files) {
    const errors = [];
    const vc = new VirtualConsole();
    vc.on('jsdomError', e => errors.push(e.message.split('\n')[0]));
    vc.on('error', (...a) => errors.push('console.error: ' + a.join(' ')));

    const dom = new JSDOM(fs.readFileSync(path.join(dir, f), 'utf8'), {
      runScripts: 'dangerously',
      pretendToBeVisual: true,
      url: 'https://example.org/' + f,
      virtualConsole: vc,
    });
    // let async boot + storage promises settle
    await new Promise(r => setTimeout(r, 400));

    const d = dom.window.document;
    const counts = {
      cards: d.querySelectorAll('.card').length,
      chips: d.querySelectorAll('.chip').length,
      rungs: d.querySelectorAll('.rung').length,
      sheets: d.querySelectorAll('.sheet').length,
      videos: d.querySelectorAll('.vid').length,
      lessons: d.querySelectorAll('.lesson').length,
      qcards: d.querySelectorAll('.qcard').length,
      broken: [...d.querySelectorAll('a[href]')]
        .map(a => a.getAttribute('href'))
        .filter(h => h && !h.startsWith('#') && !h.startsWith('http'))
        .filter(h => !fs.existsSync(path.join(dir, h))),
    };
    const summary = Object.entries(counts)
      .filter(([k, v]) => (Array.isArray(v) ? v.length : v))
      .map(([k, v]) => `${k}=${Array.isArray(v) ? v.join(',') : v}`)
      .join(' ');

    if (errors.length) bad++;
    console.log(`${errors.length ? 'FAIL' : 'ok  '}  ${f.padEnd(20)} ${summary}`);
    errors.slice(0, 3).forEach(e => console.log('        ! ' + e));
    dom.window.close();
  }
  process.exit(bad ? 1 : 0);
})();
