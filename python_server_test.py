import http.server
import socketserver
import sys, os, random, string, signal, subprocess
import time, random, string
import asyncio


Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", 8888), Handler)
print("Creating server at port", 8888)
httpd.serve_forever()