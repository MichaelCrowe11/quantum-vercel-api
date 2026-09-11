# quantum-vercel-api

quantum-vercel-api is three small Python functions written for Vercel that score code similarity and bug risk from token counts plus random noise; the Vercel deployment is disabled.

## Status

experimental

Development stopped on 2025-12-27 (two commits, both that day; last f77adce). The code is kept for reference. The handlers run locally under Python's `http.server`. These do not work or do not exist:

- Both Vercel URLs return HTTP 402 `DEPLOYMENT_DISABLED`: `quantum-vercel-crowelogicos.vercel.app` (used throughout the previous README) and `quantum-vercel.vercel.app` (the repository homepage). Checked 2026-09-10.
- There is no quantum circuit, simulator or IBM connection anywhere in the code. `requirements.txt` lists numpy only. The landing page and the previous README said the API ran on 156-qubit IBM hardware; nothing in this repository does that.
- `vercel dev` and `vercel --prod` were not run.

## Install and first run

Run on 2026-09-10 with Python 3.13.14 on macOS, using uv for the virtual environment. Vercel invokes each file's `handler` class itself; locally I served one with the standard library.

```
git clone https://github.com/MichaelCrowe11/quantum-vercel-api
cd quantum-vercel-api
uv venv --python 3.13 .venv
VIRTUAL_ENV=.venv uv pip install -r requirements.txt
.venv/bin/python -c "
import importlib.util
from http.server import HTTPServer
spec = importlib.util.spec_from_file_location('similarity', 'api/similarity.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
HTTPServer(('127.0.0.1', 8094), m.handler).serve_forever()" &
curl -s -X POST http://127.0.0.1:8094/ -H 'Content-Type: application/json' \
  -d '{"code1": "def add(a, b): return a + b", "code2": "def sum(x, y): return x + y"}'
```

Output of the same request sent twice (two constant keys cut from each line):

```
{"similarity": 0.9952, "quantum_simulated": true, "features1": [0.1696, 0.0628, 0.3142, 0.1571], "features2": [0.1696, 0.0628, 0.3142, 0.1571], ...}
{"similarity": 0.9857, "quantum_simulated": true, "features1": [0.1696, 0.0628, 0.3142, 0.1571], "features2": [0.1696, 0.0628, 0.3142, 0.1571], ...}
```

The same harness served `api/bugs.py` and `api/health.py`. The previous README's own bug example, `x = None\nif condition:\n    x.method()`, came back with `"null_pointer": 0`, `"highest_risk": "none"` and `"risk_score": 0.0503`. The health handler returned `"status": "healthy"` and `"quantum_available": true`, both constants in the source.

Not run: `vercel dev`, `vercel --prod`, `api/index.py`.

## What runs today

- `api/similarity.py`: `extract_features` takes `len(code)/500`, a count of nine operator strings over 50, `def ` over 10 and `return ` over 20, each capped at 1 and multiplied by pi. `quantum_similarity` is the cosine of the two four-number vectors mapped to `(cos + 1) / 2`, plus `numpy.random.normal(0, 0.02)`, clipped to `[0, 1]`.
- `api/bugs.py`: eight counts (`None`, `except`, `global `, `thread`, `open(`, `eval(`, length, lines) turned into six weighted scores, each plus `numpy.random.normal(0, 0.05)`, clipped.
- `api/health.py` and `api/index.py`: fixed JSON.
- `index.html`: static landing page routed for every other path by `vercel.json`.

## Limits

- No qubits are simulated and no swap test is computed. The `method` field says `quantum_swap_test_simulation` and `quantum_simulated` is always `true`; both are literal strings in the source. The score is a cosine similarity of four counts.
- The noise term makes the same input return different scores on each call (0.9952 and 0.9857 above).
- Snippets with similar counts score high regardless of meaning. `def add(a, b): return a + b` against a six-line `UserAuthentication` class scored 0.8864.
- `index.html` states live IBM hardware, 156 qubits, named machines and a 99.7% figure. No code or data in this repository supports any of it. Redeploying the page as is would republish those statements.
- The bug scores are keyword counts with weights. This is not a bug detector, a code review tool or a vulnerability scanner.

## License and contact

No license file. The previous README said MIT, but there is no `LICENSE` file in the repository.

Contact: michael@crowelogic.com
