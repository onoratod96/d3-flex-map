# Run python server on a different thread
import http.server
import socketserver
import sys, os, random, string, signal, subprocess
import time, random, string
import asyncio
from pyppeteer import launch

# run a subprocess to create server
def random_string(n=50):
    return ''.join(random.choice(string.ascii_lowercase+string.digits) for _ in range(n))

def main():
    arg = sys.argv[1]

    if arg == "open":
        run_local_server()
    else:
        open_webpage(arg)

def run_local_server(port = 8888):
    socketserver.TCPServer.allow_reuse_address = True # required for fast reuse ! 
    """
    Check out :
    https://stackoverflow.com/questions/15260558/python-tcpserver-address-already-in-use-but-i-close-the-server-and-i-use-allow
    """
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), Handler)
    print("Creating server at port", port)
    httpd.serve_forever()

def open_webpage(page):
    html_page = "index.html"

    # Runs other process in the background
    p = subprocess.Popen('python server_test.py open'.split(" "))

    time.sleep(0.5) # wait for server to launch
    url = "http://localhost:8888/examples/" + page
   
    # here you would call the puppeteer JS!
    #os.system('start %s'%url)
    subprocess.call(["python", "take_screenshot.py", url])
    os.kill(p.pid, signal.SIGTERM)

if __name__ == "__main__":
    main()