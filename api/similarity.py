"""
Quantum Code Similarity - Vercel Serverless Function
"""
from http.server import BaseHTTPRequestHandler
import json
import numpy as np

def extract_features(code: str, n_features: int = 4) -> list:
    """Extract quantum-compatible features from code"""
    features = []
    features.append(min(len(code) / 500, 1.0))

    operators = ['+', '-', '*', '/', '=', '==', '!=', '<', '>']
    op_count = sum(code.count(op) for op in operators)
    features.append(min(op_count / 50, 1.0))

    features.append(min(code.count('def ') / 10, 1.0))
    features.append(min(code.count('return ') / 20, 1.0))

    return [f * np.pi for f in features[:n_features]]

def quantum_similarity(features1: list, features2: list) -> float:
    """
    Compute quantum-inspired similarity using simulated swap test
    """
    f1 = np.array(features1)
    f2 = np.array(features2)

    # Normalize
    norm1 = np.linalg.norm(f1)
    norm2 = np.linalg.norm(f2)

    if norm1 == 0 or norm2 == 0:
        return 0.0

    # Compute overlap (simulated quantum measurement)
    overlap = np.dot(f1, f2) / (norm1 * norm2)

    # Add quantum noise simulation
    noise = np.random.normal(0, 0.02)
    similarity = max(0, min(1, (overlap + 1) / 2 + noise))

    return float(similarity)

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            code1 = data.get('code1', '')
            code2 = data.get('code2', '')

            if not code1 or not code2:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "error": "Missing code1 or code2"
                }).encode())
                return

            # Extract features
            features1 = extract_features(code1)
            features2 = extract_features(code2)

            # Compute quantum similarity
            similarity = quantum_similarity(features1, features2)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            response = {
                "similarity": round(similarity, 4),
                "quantum_simulated": True,
                "features1": [round(f, 4) for f in features1],
                "features2": [round(f, 4) for f in features2],
                "platform": "vercel-serverless",
                "method": "quantum_swap_test_simulation"
            }

            self.wfile.write(json.dumps(response).encode())

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                "error": str(e)
            }).encode())
