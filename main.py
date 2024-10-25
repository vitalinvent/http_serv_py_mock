import cgi
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()
        self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}))

    # GET sends back a Hello world message
    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps(self.getDict()).encode('utf-8'))

    # POST echoes the message adding a JSON field
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        # read the message and convert it into a python dictionary
        length = int(self.headers.getheader('content-length'))
        message = json.loads(self.rfile.read(length))

        # add a property to the object, just to mess with data
        message['received'] = 'ok'

        # send the message back
        self._set_headers()
        self.wfile.write(json.dumps(message))

    def getDict(self):
        fileName = 'D:\dev\py\http_serv\dict.txt'
        # with open() as f:
        # f = io.open(fileName, mode="r", encoding="utf-8")
        # lines = f.readlines()
        with open(fileName, 'r', encoding="utf-8") as file:
            lines = json.load(file)

        return lines  # .encode('utf-8')


def run(server_class=HTTPServer, handler_class=Server, port=8850):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    print
    'Starting httpd on port %d...' % port
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
