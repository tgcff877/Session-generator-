
import os
import sys
import time
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from http.server import BaseHTTPRequestHandler, HTTPServer

# Configuration settings
API_ID = int(os.environ.get('API_ID', ''))
API_HASH = os.environ.get('API_HASH', '')
PORT = int(os.environ.get('PORT', 8080))

class SessionGenerator(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Session Generator is running...')

def generate_session(api_id, api_hash):
    client = TelegramClient(StringSession(), api_id, api_hash)
    client.start()
    session_string = client.session.save()
    client.stop()
    return session_string

def main():
    # Create an HTTP server
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, SessionGenerator)
    print(f'Starting HTTP server on port {PORT}...')
    httpd.serve_forever()

if __name__ == '__main__':
    # Generate session strings
    session_string_v1 = generate_session(API_ID, API_HASH)
    session_string_v2 = generate_session(API_ID, API_HASH)
    print(f'Pyrogram v1 session string: {session_string_v1}')
    print(f'Pyrogram v2 session string: {session_string_v2}')

    # Start the HTTP server
    main()
