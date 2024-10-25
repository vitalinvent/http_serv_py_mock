from http.server import SimpleHTTPRequestHandler, HTTPServer
# http//:localhost:8090/api
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        if self.path == 'api':
            self.wfile.write(
                b"""
                {"statusCodeValue":200,"statusCode":"OK"}
                """
            )
        if self.path == 'realms':
            self.wfile.write(
                b"""
                {"statusCodeValue":200,"statusCode":"OK"}
                """
            )

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        # self.wfile.write(self._html("POST!"))
        if self.path == 'api':
            self.wfile.write(
                b"""
                {"statusCodeValue":200,"statusCode":"OK"}
                """
            )
        if self.path == 'realms':
            self.wfile.write(
                b"""
                {"statusCodeValue":200,"statusCode":"OK"}
                """
            )
server_address = ('', 8850)
httpd = HTTPServer(server_address, MyHandler)

print("Starting server on port {}...",str(server_address))
httpd.serve_forever()