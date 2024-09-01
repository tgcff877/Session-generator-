
import http.server
import socketserver

PORT = 8000

class SessionGeneratorHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"SessionGenerator is running!")

def run_server():
    with socketserver.TCPServer(("", PORT), SessionGeneratorHandler) as httpd:
        print(f"SessionGenerator is running on port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
