const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({headless:false});
  const page = await browser.newPage();
  await page.goto('file://A:/Github/d3-flex-map/examples/hello_world.html', {waitUntil: 'networkidle2'});
  await page.screenshot({path: 'example.png', fullPage:true});
  await browser.close();
})();