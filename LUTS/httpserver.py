import os, sys

from http.server import  HTTPServer, CGIHTTPRequestHandler

# webdir = os.getcwd()
port = 8011

# os.chdir(webdir)
srvaddr = ('', port)
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvobj.serve_forever()