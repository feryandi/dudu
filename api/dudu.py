import json
import util.sheet

from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    rows = util.sheet.read_rows()
    rows.reverse()
    
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps(rows).encode())
    return

  def do_POST(self):
    content_len = int(self.headers.get('Content-Length'))
    post_body = self.rfile.read(content_len)

    content_type = str(self.headers.get('Content-Type'))
    if content_type == "application/json":
      post_body = json.loads(post_body)

    print(post_body)
    d = ['=IF(ISNUMBER(INDIRECT(ADDRESS(ROW()-1;COLUMN()))); INDIRECT(ADDRESS(ROW()-1;COLUMN()))+1; 1)']
    d += post_body
    util.sheet.write_row(d)

    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(str("{\"status\":\"success\"}").encode())
