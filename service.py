from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse
import subprocess

import config

class LogTail_RequestHandler(BaseHTTPRequestHandler):

  def do_GET(self):
        # exract query params to dict
        params = dict(parse_qsl(urlparse(self.path).query))

        # nope
        if params.get('secret') != config.secret:
            self.send_response(400)
            self.wfile.write(bytes("fork you\n", "utf8"))
            return

        # what kind of logs?
        if params.get('type')=='':
            self.send_response(400)
            self.wfile.write(bytes("`type` is required (access|error)\n", "utf8"))
            return

        logfile = None;

        if params.get('type')=='access':
            logfile = config.access_log

        if params.get('type')=='error':
            logfile = config.error_log

        num=100
        if params.get('num'):
            num = params.get('num')

        # run the tail
        proc = subprocess.Popen([
            "tail",
            "-n{num}".format(num=num),
            logfile], stdout=subprocess.PIPE)
        output = proc.stdout.read()

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Write content as utf-8 data
        self.wfile.write(output)
        return

def run():
  server_address = (config.host, int(config.port))
  httpd = HTTPServer(server_address, LogTail_RequestHandler)
  print('* server running at {host}:{port}'.format(
    host=config.host,port=config.port))
  httpd.serve_forever()

if __name__ == '__main__':
    run()
