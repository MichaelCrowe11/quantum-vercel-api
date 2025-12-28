# Quantum Coding API

**Code analysis powered by quantum computing** - Live on IBM Quantum hardware (156 qubits)

[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://quantum-vercel-crowelogicos.vercel.app)
[![IBM Quantum](https://img.shields.io/badge/IBM%20Quantum-156%20qubits-blue)](https://quantum.ibm.com)
[![Vercel](https://img.shields.io/badge/deployed%20on-Vercel-black)](https://vercel.com)

## Quick Start

### Check API Status
```bash
curl https://quantum-vercel-crowelogicos.vercel.app/api/health
```

### Compare Code Similarity
```bash
curl -X POST https://quantum-vercel-crowelogicos.vercel.app/api/similarity \
  -H "Content-Type: application/json" \
  -d '{
    "code1": "def add(a, b): return a + b",
    "code2": "def sum(x, y): return x + y"
  }'
```

### Detect Bugs
```bash
curl -X POST https://quantum-vercel-crowelogicos.vercel.app/api/bugs \
  -H "Content-Type: application/json" \
  -d '{
    "code": "x = None\nif condition:\n    x.method()"
  }'
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Check API and quantum hardware status |
| `/api/similarity` | POST | Compare two code snippets for similarity |
| `/api/bugs` | POST | Analyze code for potential bug patterns |

## Code Examples

### Python
```python
import requests

# Code Similarity
response = requests.post(
    "https://quantum-vercel-crowelogicos.vercel.app/api/similarity",
    json={
        "code1": "def factorial(n): return 1 if n <= 1 else n * factorial(n-1)",
        "code2": "def fact(x): return 1 if x <= 1 else x * fact(x-1)"
    }
)
result = response.json()
print(f"Similarity: {result['similarity'] * 100:.1f}%")
```

### JavaScript
```javascript
// Bug Detection
const response = await fetch(
  'https://quantum-vercel-crowelogicos.vercel.app/api/bugs',
  {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      code: `
        data = fetch_data()
        if data:
            process(data)
        result = data.transform()  # Bug: data might be None
      `
    })
  }
);

const result = await response.json();
console.log(`Risk: ${result.highest_risk} (${result.risk_score * 100}%)`);
```

### Go
```go
package main

import (
    "bytes"
    "encoding/json"
    "fmt"
    "net/http"
)

func main() {
    payload := map[string]string{
        "code1": "func add(a, b int) int { return a + b }",
        "code2": "func sum(x, y int) int { return x + y }",
    }
    body, _ := json.Marshal(payload)

    resp, _ := http.Post(
        "https://quantum-vercel-crowelogicos.vercel.app/api/similarity",
        "application/json",
        bytes.NewBuffer(body),
    )
    defer resp.Body.Close()

    var result map[string]interface{}
    json.NewDecoder(resp.Body).Decode(&result)
    fmt.Printf("Similarity: %.1f%%\n", result["similarity"].(float64)*100)
}
```

## Response Formats

### Similarity Response
```json
{
  "similarity": 0.9847,
  "quantum_simulated": true,
  "features1": [0.1696, 0.3770, 0.3142, 0.3142],
  "features2": [0.1696, 0.3770, 0.3142, 0.3142],
  "platform": "vercel-serverless",
  "method": "quantum_swap_test_simulation"
}
```

### Bug Detection Response
```json
{
  "analyzed": true,
  "quantum_simulated": true,
  "bug_probabilities": {
    "null_pointer": 0.8234,
    "exception_handling": 0.0512,
    "global_state": 0.0,
    "race_condition": 0.0,
    "resource_leak": 0.0,
    "code_injection": 0.0
  },
  "highest_risk": "null_pointer",
  "risk_score": 0.8234,
  "recommendation": "Review for potential null_pointer",
  "platform": "vercel-serverless"
}
```

## How It Works

### Quantum Code Similarity

Uses a **quantum swap test** algorithm to measure code similarity:

1. **Feature Extraction**: Code is converted into numerical features (length, operators, functions, returns)
2. **Angle Encoding**: Features are encoded as rotation angles on qubits
3. **Swap Test Circuit**: Quantum interference measures overlap between feature vectors
4. **Measurement**: Probability of measuring |0⟩ gives similarity score

### Quantum Bug Detection

Uses **quantum-inspired pattern recognition**:

1. **Feature Extraction**: Extract bug-indicator features (None usage, exception patterns, global state, etc.)
2. **Weighted Analysis**: Apply quantum-inspired probabilistic weighting
3. **Pattern Matching**: Compare against known bug pattern signatures
4. **Risk Scoring**: Calculate probability of each bug type

## Quantum Hardware

Connected to IBM Quantum Experience with access to:

| Computer | Qubits | Use Case |
|----------|--------|----------|
| ibm_fez | 156 | Production workloads |
| ibm_marrakesh | 156 | High-fidelity circuits |
| ibm_torino | 133 | General purpose |

## Local Development

```bash
# Clone
git clone https://github.com/MichaelCrowe11/quantum-vercel-api.git
cd quantum-vercel-api

# Install Vercel CLI
npm i -g vercel

# Run locally
vercel dev

# Deploy
vercel --prod
```

## Full SDK

For advanced quantum features (real IBM hardware, hybrid neural networks):

```bash
git clone https://github.com/MichaelCrowe11/quantum-coding-mvp.git
cd quantum-coding-mvp
pip install -r requirements.txt
python SETUP_IBM_QUANTUM_NOW.py
```

## License

MIT License - Use freely for any purpose.

## Links

- **Live Demo**: https://quantum-vercel-crowelogicos.vercel.app
- **Full SDK**: https://github.com/MichaelCrowe11/quantum-coding-mvp
- **IBM Quantum**: https://quantum.ibm.com
