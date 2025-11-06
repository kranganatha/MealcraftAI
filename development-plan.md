# Development & Debugging Plan

## Issue Tracked
**FastAPI backend failed to start due to missing Uvicorn module.**

### Observed Behavior
Running:
```bash
python3 -m uvicorn backend.app.main:app --reload
```
produced:
```
/usr/local/bin/python3: No module named uvicorn
```
Exit code: 1.

### Root Cause
`uvicorn` is specified in [`backend/requirements.txt`](backend/requirements.txt:2):
```
uvicorn==0.30.1
```
but not installed in the active Python environment.  
This indicates a **local environment misconfiguration**, not a missing dependency in the codebase.

### Resolution Options
1. **Install dependencies before running:**
   ```bash
   pip install -r backend/requirements.txt
   ```
2. Alternatively, **run the app** with a virtual environment where Uvicorn is already available:
   ```bash
   python3 -m uvicorn backend.app.main:app --reload
   ```

### Status
- Code: ✅ healthy
- Environment: ❌ missing `uvicorn`
- Server: not running

### Next Step
Install dependencies (particularly Uvicorn) before retrying runtime launch.
