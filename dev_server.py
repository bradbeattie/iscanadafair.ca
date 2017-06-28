from http.server import test, SimpleHTTPRequestHandler
import os

class SuffixHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.translate_path(self.path)
        if not os.path.exists(path):
            self.path = f"{self.path.rstrip('/')}.html"
        super().do_GET()

test(HandlerClass=SuffixHandler)
