import http.server as srv

# print(dir(srv.HTTPServer))

def run(server_class=srv.HTTPServer, handler_class=srv.BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()