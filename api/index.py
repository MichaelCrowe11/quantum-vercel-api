"""
Quantum Coding API - Vercel Serverless
"""
from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        response = {
            "name": "Quantum Coding Assistant API",
            "version": "1.0.0",
            "quantum_enabled": True,
            "endpoints": [
                "GET /api - This info",
                "GET /api/health - Health check",
                "POST /api/similarity - Compare code",
                "POST /api/bugs - Detect bugs"
            ]
        }

        self.wfile.write(json.dumps(response).encode())
