#!/usr/bin/python3


import warnings
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading


#IP address to listen on
hostName = "0.0.0.0"
#Port
serverPort = 80
cmd = "#"


class MyServer(BaseHTTPRequestHandler):


def do_GET(self):
global cmd
self.send_response(200)
self.send_header("Content-type", "text/html; charset=utf-8")
self.end_headers()
self.wfile.write(bytes(cmd, "utf-8"))
cmd = "#"


def do_POST(self):
if True:
self.send_response(200)
self.send_header("Content-type", "text/html; charset=utf-8")
self.end_headers()
content = self.rfile.read(int(self.headers["content-length"]))
try:
content = content.decode('ascii')
print(content)
except:
print("Error parsing response.")


self.wfile.write(bytes("", "utf-8"))
def log_message(self, format, *args):
return


def cmdFunc():
global cmd
while True:
cmd = input("")


if __name__ == "__main__":
webServer = HTTPServer((hostName, serverPort), MyServer)


print("Server started http://%s:%s" % (hostName, serverPort))


try:
th = threading.Thread(target=cmdFunc)
th.start()
webServer.serve_forever()
except KeyboardInterrupt:
pass
th.join()
webServer.server_close()
print("Server stopped.")
