import http.server
import socketserver
import os
import mimetypes

PORT = 4000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class SPAHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Clean path
        req_path = self.path.split('?')[0].split('#')[0]
        full_path = os.path.join(DIRECTORY, req_path.lstrip('/'))

        # If file exists on disk, let SimpleHTTPRequestHandler serve it
        if os.path.isfile(full_path):
            return super().do_GET()

        # If it's a directory with index.html, let SimpleHTTPRequestHandler serve it
        if os.path.isdir(full_path) and os.path.isfile(os.path.join(full_path, 'index.html')):
            return super().do_GET()

        # For SPA routes (like /screen-dashboard, /screen-*, /dashboard, or 404s), serve index.html directly
        index_file = os.path.join(DIRECTORY, 'index.html')
        if os.path.isfile(index_file):
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            with open(index_file, 'rb') as f:
                content = f.read()
            self.send_header('Content-Length', str(len(content)))
            self.send_header('Cache-Control', 'no-cache')
            self.end_headers()
            self.wfile.write(content)
            return

        return super().do_GET()

class ReusableTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

if __name__ == '__main__':
    with ReusableTCPServer(("", PORT), SPAHandler) as httpd:
        print(f"Serving Leadirftex Interchain SPA at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
