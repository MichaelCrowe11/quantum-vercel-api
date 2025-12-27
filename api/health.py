"""Health check endpoint"""
from http.server import BaseHTTPRequestHandler
import json
import time

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        response = {
            "status": "healthy",
            "quantum_available": True,
            "platform": "vercel",
            "timestamp": time.time()
        }

        self.wfile.write(json.dumps(response).encode())
