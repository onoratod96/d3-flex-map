# Run python server on a different thread
import http.server
import socketserver
import sys, os, random, string, signal, subprocess
import time, random, string
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()

   # arg = sys.argv[1]

    await page.goto("http://localhost:8888/map.html", {'waitUntil': 'networkidle2'})
    await page.screenshot({'path': 'screenshot.png', 'fullPage': True})
    #await page.pdf({'path': 'screenshot.pdf', 'landscape' : True,  'format': 'A4'});
    #await browser.close()



asyncio.get_event_loop().run_until_complete(main())
