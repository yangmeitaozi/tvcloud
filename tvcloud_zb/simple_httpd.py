
from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler

port = 8080

httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()

