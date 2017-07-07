#!/usr/bin/env python
from http.server import test as run_dev_server, SimpleHTTPRequestHandler
import os

class SuffixHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.translate_path(self.path)
        if not os.path.exists(path):
            self.path = f"{self.path.rstrip('/')}.html"
        super().do_GET()

run_dev_server(HandlerClass=SuffixHandler)
