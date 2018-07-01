#!/usr/bin/env python3
"""
Very simple HTTP server in python3.

Usage::
    ./dummy-web-server.py [<port>]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "green=on/off&red=on/off" http://localhost
    curl -d "" http://localhost  - is the same "green=off&red=off"


"""
#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from http.server import BaseHTTPRequestHandler, HTTPServer
#import SocketServer
import socketserver
import re
import OPi.GPIO as GPIO

class HTTP_GPIOCtrl(BaseHTTPRequestHandler):

  _unknown = """
<html><body><h4>unknown page</h4></body></html>
"""

  _form = """
<html>
<body>
<h4>GPIO LED control</h4>
<div>
<form method="post">
<div>
<input type="checkbox" name="green" value="on">green LED
</div>
<div>
<input type="checkbox" name="red" value="on">red LED
</div>
<div>
<input type="submit" value="Submit">
</div>
</form>
</div>
</body>
</html>
"""

  def __init__(self, request, client_address, server):
    BaseHTTPRequestHandler.__init__(self, request, client_address, server)

  def _set_headers(self, code=200):
    if code == 200:
      self.send_response(code)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
    else:
      self.send_error(code)
      self.send_header('Content-type', 'text/html')
      self.end_headers()

  def do_GET(self):
    print('GET:->'+self.path+'<-')
    if self.path == '/':
      self._set_headers()
      self.wfile.write(bytes(self._form, "utf-8"))
      print("form")
    elif self.path == '/favicon.ico':
      self._set_headers(200)
      self.wfile.write(bytes("<html><body></body></html>", "utf-8"))
      print("favicon")
#    self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
    else:
      self._set_headers(404)
      self.wfile.write(bytes(self._unknown,"utf-8"))
      print("unknown")

  def do_HEAD(self):
    self._set_headers()

  def do_POST(self):
    content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
    post_data = self.rfile.read(content_length) # <--- Gets the data itself
    print (str(content_length) +' '+ str(post_data)) # <-- Print post data
    self._set_headers()
    self.wfile.write(bytes("<html><body><h1>POST!</h1></body></html>", "utf-8"))
    gpio24 = GPIO.LOW
    gpio26 = GPIO.LOW
    if content_length > 0:
      m = re.search('green=on', str(post_data))
      if m:
        gpio24 = GPIO.HIGH
      m = re.search('red=on', str(post_data))
      if m:
        gpio26 = GPIO.HIGH 
    GPIO.output(24, gpio24)
    GPIO.output(26, gpio26)

#<- class HTTP_GPIOCtrl
        
        
def run(server_class=HTTPServer, handler_class=HTTP_GPIOCtrl, port=80):
  server_address = ('', port)
  httpd = server_class(server_address, handler_class)
  print('Starting httpd...')
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    return httpd

if __name__ == "__main__":
  from sys import argv, exit

  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(24, GPIO.OUT)
  GPIO.setup(26, GPIO.OUT)

  GPIO.output(24, GPIO.LOW)
  GPIO.output(26, GPIO.LOW)

  if len(argv) == 2:
      run(port=int(argv[1]))
  else:
      run().server_close()

  GPIO.cleanup()
  print('httpd exited')

  exit(0)
