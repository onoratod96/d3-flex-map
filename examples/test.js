const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({headless:false});
  const page = await browser.newPage();
  await page.goto('http://localhost:8888/map.html', {waitUntil: 'networkidle2'});
  await page.screenshot({path: 'example.png', fullPage:true});
  await browser.close();
})();