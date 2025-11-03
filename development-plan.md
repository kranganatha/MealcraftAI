# 🧭 MealCraft AI — Development Plan

## Sprint 0: Foundational Scaffolding (✅ Completed)
**Goal:** Establish environment scaffolding and health-check communication across tiers.

### ✅ Deliverables
- **Backend (FastAPI)**
  - `backend/app/main.py` with `/api/v1/health` endpoint returning `{"status": "ok"}`
  - MongoDB Atlas connection module (`app/core/database.py`) with startup/shutdown events.
  - Deployment-ready with `Procfile` and `render.yaml`.
- **Frontend (Flask)**
  - `frontend/app.py` serves UI and calls backend health API.
  - `frontend/templates/index.html` displays backend connection status.
- **Shared Configuration**
  - `.env` defines `MONGODB_URI`, `MONGO_DB_NAME`, `BACKEND_API_BASE`.
- **Environment**
  - Backend: `uvicorn app.main:app --reload`
  - Frontend: `python3 app.py`
  - Both run concurrently for local development.

### ✅ Verification
- End-to-end flow confirmed: **Browser → Flask → FastAPI → MongoDB → FastAPI → Flask**
- Health check returned `{"status":"ok"}` successfully.

---

## Next Sprint: Sprint 1 — Authentication Layer
**Goal:** Implement user registration and login using JWT-based authentication with MongoDB persistence.

### Planned Tasks
1. Create `User` model and repository.
2. Hash passwords using bcrypt.
3. Add `/register` and `/login` endpoints.
4. Implement JWT authentication middleware.
5. Integrate with frontend sign-in form.

---

**Status:** Sprint 0 verified ✅ \
**Next Step:** Prepare Sprint 1 authentication implementation and begin API development.
