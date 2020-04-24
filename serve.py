import http.server
import socketserver
import sys, os, random, string, signal, subprocess
import time, random, string
import asyncio
from pyppeteer import launch


p = subprocess.Popen("python python_server_test.py".split(" "))
print("hello")

async def screen():
    browser = await launch(headless=True)
    page = await browser.newPage()

   # arg = sys.argv[1]

    await page.goto("http://localhost:8888/map.html", {'waitUntil': 'networkidle2'})
    await page.screenshot({'path': 'screenshot.png', 'fullPage': True})
    #await page.pdf({'path': 'screenshot.pdf', 'landscape' : True,  'format': 'A4'});
    #await browser.close()
    print("hello there")



asyncio.get_event_loop().run_until_complete(screen())

p.terminate()

'''
p2 = subprocess.Popen("python take_screenshot.py".split(" "))
p2.wait()
print("brave new world")
time.sleep(10)
p.terminate()
#os.kill(p.pid, signal.SIGTERM)
'''