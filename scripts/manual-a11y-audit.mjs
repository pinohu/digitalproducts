import { chromium } from 'playwright';
import axe from 'axe-core';
import fs from 'node:fs/promises';
import path from 'node:path';

const url = process.argv[2] || 'http://127.0.0.1:4173/index.html';
const outDir = path.resolve('audit-output/suitedash-preview');
await fs.mkdir(outDir, { recursive: true });

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
const consoleMessages = [];
page.on('console', msg => consoleMessages.push({ type: msg.type(), text: msg.text() }));
page.on('pageerror', err => consoleMessages.push({ type: 'pageerror', text: err.message }));

await page.goto(url, { waitUntil: 'networkidle' });
await page.screenshot({ path: path.join(outDir, 'desktop-1280x900.png'), fullPage: true });

const axeDesktop = await page.evaluate(async (axeSource) => {
  const script = document.createElement('script');
  script.textContent = axeSource;
  document.head.appendChild(script);
  return await window.axe.run(document, { resultTypes: ['violations', 'incomplete'] });
}, axe.source);

const headings = await page.evaluate(() => [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].map(h => ({ level: Number(h.tagName[1]), text: h.textContent.trim() })));
const landmarks = await page.evaluate(() => [...document.querySelectorAll('header,main,nav,footer,section,article')].map(el => ({ tag: el.tagName.toLowerCase(), id: el.id || null, label: el.getAttribute('aria-label') || el.getAttribute('aria-labelledby') || null })));
const links = await page.evaluate(() => [...document.querySelectorAll('a,button,[role="button"], [tabindex]')].map(el => ({ tag: el.tagName.toLowerCase(), text: el.textContent.trim(), href: el.getAttribute('href'), role: el.getAttribute('role'), ariaDisabled: el.getAttribute('aria-disabled'), tabIndex: el.tabIndex })));

const focusSequence = [];
for (let i = 0; i < 8; i += 1) {
  await page.keyboard.press('Tab');
  await page.waitForTimeout(220);
  focusSequence.push(await page.evaluate(() => {
    const el = document.activeElement;
    const r = el.getBoundingClientRect();
    const styles = getComputedStyle(el);
    return { tag: el.tagName.toLowerCase(), text: el.textContent.trim(), href: el.getAttribute('href'), id: el.id || null, className: el.className || null, x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height), outlineStyle: styles.outlineStyle, outlineWidth: styles.outlineWidth };
  }));
}

await page.goto(url, { waitUntil: 'networkidle' });
await page.keyboard.press('Tab');
await page.waitForTimeout(220);
const skipLinkFocus = await page.evaluate(() => {
  const el = document.activeElement;
  const r = el.getBoundingClientRect();
  return { text: el.textContent.trim(), x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
});
await page.keyboard.press('Enter');
await page.waitForTimeout(320);
const skipLinkResult = await page.evaluate(() => ({ hash: location.hash, activeTag: document.activeElement.tagName.toLowerCase(), activeId: document.activeElement.id || null, scrollY: Math.round(scrollY) }));

await page.setViewportSize({ width: 390, height: 844 });
await page.goto(url, { waitUntil: 'networkidle' });
await page.evaluate(() => scrollTo(0, 0));
await page.screenshot({ path: path.join(outDir, 'mobile-390x844.png'), fullPage: true });
const mobileMetrics = await page.evaluate(() => ({
  clientWidth: document.documentElement.clientWidth,
  scrollWidth: document.documentElement.scrollWidth,
  bodyScrollWidth: document.body.scrollWidth,
  h1Text: document.querySelector('h1')?.textContent.trim(),
  h1Rect: (() => { const r = document.querySelector('h1').getBoundingClientRect(); return { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) }; })(),
  buttons: [...document.querySelectorAll('.button')].map(el => { const r = el.getBoundingClientRect(); return { text: el.textContent.trim(), tag: el.tagName.toLowerCase(), w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y) }; }),
  minTapHeight: Math.min(...[...document.querySelectorAll('a.button')].map(el => el.getBoundingClientRect().height)),
}));

const axeMobile = await page.evaluate(async (axeSource) => {
  const script = document.createElement('script');
  script.textContent = axeSource;
  document.head.appendChild(script);
  return await window.axe.run(document, { resultTypes: ['violations', 'incomplete'] });
}, axe.source);

const report = {
  url,
  screenshots: {
    desktop: path.join(outDir, 'desktop-1280x900.png'),
    mobile: path.join(outDir, 'mobile-390x844.png'),
  },
  consoleMessages,
  headings,
  landmarks,
  links,
  focusSequence,
  skipLinkFocus,
  skipLinkResult,
  mobileMetrics,
  axe: {
    desktop: {
      violations: axeDesktop.violations.map(v => ({ id: v.id, impact: v.impact, description: v.description, nodes: v.nodes.map(n => ({ target: n.target, summary: n.failureSummary })) })),
      incomplete: axeDesktop.incomplete.map(v => ({ id: v.id, impact: v.impact, description: v.description, nodes: v.nodes.map(n => ({ target: n.target })) })),
    },
    mobile: {
      violations: axeMobile.violations.map(v => ({ id: v.id, impact: v.impact, description: v.description, nodes: v.nodes.map(n => ({ target: n.target, summary: n.failureSummary })) })),
      incomplete: axeMobile.incomplete.map(v => ({ id: v.id, impact: v.impact, description: v.description, nodes: v.nodes.map(n => ({ target: n.target })) })),
    }
  }
};
await fs.writeFile(path.join(outDir, 'manual-a11y-runtime-report.json'), JSON.stringify(report, null, 2));
console.log(JSON.stringify(report, null, 2));
await browser.close();
