# DEVELOPMENT PLAN — Sprint N+1: Beverage Pairing Suggestion Feature

## 1. Overview
This sprint focuses on extending the AI-driven recipe generation feature by adding a **Beverage Pairing Suggestion Button**. The new feature enhances user experience by generating beverage pairing suggestions for the displayed recipe using MealcraftAI’s existing AI backend.

---

## 2. Technology Stack

| Component | Technology | Version | Notes |
|------------|-------------|----------|-------|
| **Frontend** | Next.js | Latest (v15.x) | React-based full-stack rendering framework |
| **UI Components** | shadcn/ui | Latest (v0.9.x) | Modern, accessible UI component system |
| **Backend** | FastAPI | Latest (v0.116.x) | High-performance Python web framework |
| **Runtime** | Python | LTS (3.12.x) | Compatible with FastAPI & Pydantic |
| **Database** | MongoDB Atlas | Latest Stable | Managed NoSQL service for persistence |
| **AI Adapter** | OpenAI-compatible API | - | Reused from existing `/api/v1/ai/respond` logic |

---

## 3. Architecture Pattern

**Pattern**: Modular Monolith  
**Justification**:  
This extension integrates tightly with the existing MealcraftAI application. Since the AI-based response and frontend rendering are already established in the monolithic structure (FastAPI backend, Next.js frontend communicating via REST), continuing under the Modular Monolith architecture minimizes overhead.  
**Benefits**:
- Maintains cohesive communication across modules.
- Avoids unnecessary service segregation delays.
- Enables vertical feature slicing for simpler testing and deployment.

---

## 4. Domain-Driven Module Design (New Additions)

| Module | Domain Responsibility | Key Changes |
|---------|------------------------|--------------|
| **AI Module (Backend)** | Handles AI calls, prompt augmentation, and text formatting. | Extend `/api/v1/ai/respond` or create `/api/v1/ai/beverage-pairings` endpoint. |
| **Frontend RecipePage Module** | UI for recipe output and user interactions. | Add new Beverage Pairing Button & output box below AI response area. |
| **Shared Components** | Markdown renderer, API client utilities. | Reuse existing `marked.js` + DOMPurify renderer. Add styling extensions. |

---

## 5. THE SPRINT PLAN — Sprint N+1: Beverage Pairing Suggestion Feature

### Sprint ID
**SN+1: Beverage Pairing Suggestion Button**

### Project Context
MealcraftAI currently allows users to generate recipe-based outputs from AI. This sprint enhances the user journey by adding beverage pairing suggestions for each recipe.

### Previous Sprint’s Accomplishments
The prior sprint delivered the core recipe generation and AI integration framework.

### Goal
Add a one-click button that returns beverage pairing suggestions formatted as Markdown and displayed below the existing recipe output.

### Relevant Requirements & User Stories
- *As a user, I want to request beverage pairings for a recipe so I can choose complementary drinks.*
- *As a user, I want the response displayed below the recipe output in formatted Markdown.*

---

### Tasks

#### 1. Database Model & Schema Design
- No new persistent schema required.  
- Validate existing data structures ensure compatibility with `recipe_name` context storage.  
- **USER INPUT REQUIRED**:
  - **WHY**: Verify if future beverage pairing caching is desired.
  - **FORMAT**: Boolean confirmation (Yes/No)
  - **ACTION**: Confirm if pairing responses should be persisted in MongoDB for history.

---

#### 2. Backend: Beverage Pairing Logic
- **Extension Option 1:** Extend existing FastAPI route `/api/v1/ai/respond`.
- **Option 2:** Create dedicated `/api/v1/ai/beverage-pairings` endpoint.
- Parse POST JSON:
  ```json
  {"recipe_name": "Spaghetti Carbonara"}
  ```
- Append `"For this recipe, suggest top 3 beverage pairings."` to AI prompt.
- Ensure returned content is Markdown formatted (use existing output formatting flow).
- **USER INPUT REQUIRED**:
  - **WHY**: Confirm preferred route naming convention.
  - **FORMAT**: Choose between `/api/v1/ai/respond` extension or new `/api/v1/ai/beverage-pairings`
  - **ACTION**: Developer implements based on confirmation.
- Add backend unit tests verifying:
  - Prompt construction includes “top 3 beverage pairings.”
  - Proper JSON response with Markdown text.

---

#### 3. Frontend: UI & State
- Add a **"Give me beverage pairings for this recipe"** button beneath the current recipe output.
- On click:
  1. Extract current recipe name from page state.
  2. POST request to backend AI endpoint.
  3. Display Markdown response below existing output area using `marked.js` and DOMPurify.
- Add a distinct style for beverage pairing section (e.g., border-top, soft background).
- **USER INPUT REQUIRED**:
  - **WHY**: Confirm button label styling and placement preference.
  - **FORMAT**: Example: ("Primary" button next to Save button / full width below text)
  - **ACTION**: Adjust button placement during implementation.

---

#### 4. Frontend: End-to-End Flow
- Ensure seamless data flow:
  - Button click → Backend request → AI response → Rendered output.
- Implement visual feedback (spinner/loading state) during AI response fetch.
- Perform manual testing with sample recipe “Spaghetti Carbonara.”
- **USER INPUT REQUIRED**:
  - **WHY**: To confirm Markdown response visually renders correctly.
  - **FORMAT**: User reports text and formatting correctness.
  - **ACTION**: Validate output box renders 3 beverage options in Markdown.

---

#### 5. Sprint Branch, Commit & Deployment
- Create branch:
  ```bash
  git checkout -b sprint-n+1-beverage-pairing
  ```
- **Commit Format Example**:
  ```
  feat(sprint-n+1): add beverage pairing suggestion feature

  Sprint N+1 Accomplishments:
  - Added 'Give me beverage pairings' button in frontend
  - Implemented backend AI route for beverage pairings
  - Integrated Markdown rendering in frontend output box
  - Updated styling for beverage section UI
  - Added unit tests for backend AI prompt augmentation
  - Validated end-to-end flow with sample recipe
  ```
- Push branch and deploy to staging:
  - **Vercel (Frontend)**: Deploy `sprint-n+1-beverage-pairing`
  - **Render (Backend)**: Deploy same branch build
- **USER INPUT REQUIRED**:
  - **WHY**: Confirm deployed URLs (frontend and backend) respond correctly.
  - **FORMAT**: Provide confirmation that both deployments display correct data.
  - **ACTION**: Tester validates functionality and approves PR merge.
- Create Pull Request:
  - **Title**: `Sprint N+1: Beverage Pairing Suggestion Feature`
  - **PR Description** includes accomplishment list, URLs, and testing notes.

---

### Verification Criteria
- Frontend shows pairing suggestions in Markdown format for any recipe.
- Backend logs show successful AI call including `"top 3 beverage pairings"` phrase.
- Manual testing confirms content visibility and correctness.
- Deployment to both Vercel and Render verified by user.

---

## 6. Deployment & User Input Requirements

| Task | User Input Required | Description |
|------|----------------------|--------------|
| Repository Confirmation | ✅ | Confirm GitHub repository branch for sprint deployment |
| Backend Route Decision | ✅ | Decide between extending existing `/respond` vs. new route |
| UI Placement Confirmation | ✅ | Confirm button style and placement |
| Visual Render Confirmation | ✅ | Verify Markdown output correctness |
| Deployment Verification | ✅ | Validate success URLs post-deployment |

---

## 7. Commit and Deployment Validations
- Ensure **semantic commit formatting** follows feature-based convention (`feat(sprint-n+1):` ...)
- Validate **Vercel ↔ Render synchronization**
- Require **manual test confirmation** before PR merge

---

## 8. Testing Plan
- **Backend Unit Test**: Verify AI prompt construction.
- **Frontend Integration Test**: Simulate click → API call → render flow.
- **Manual Testing**: Validate real output for “Spaghetti Carbonara”.

---

## 9. Deliverables
- Extended FastAPI backend with beverage pairing logic
- Updated frontend with new button and markdown-rendered section
- Confirmed working API response in Markdown
- Reviewed commit, deployment, and user confirmation flow
- Merged PR after successful deployment test approvals

---

## 10. Validation Checklist
- [x] Complete Sprint N+1 breakdown
- [x] Defined backend and frontend tasks clearly
- [x] Included all `USER INPUT REQUIRED` sections with WHY, FORMAT, ACTION
- [x] Added commit and deployment detailing
- [x] Covered full feature testing plan
- [x] Confirmed alignment with architecture and DDD principles


## 🚀 Sprint N+1 Progress Update — Beverage Pairing Suggestion Feature

**Status:** In Progress  
**Date:** 2025-11-05  
**Implemented Components:**
- ✅ Added new backend endpoint `/api/v1/ai/beverage-pairings` to generate beverage pairing suggestions using OpenAI.  
- ✅ Integrated frontend button “Give me beverage pairings for this recipe.”  
- ✅ Configured Markdown rendering for beverage pairing output using existing `marked.js` and `DOMPurify`.  
- ✅ Validated response flow: user request → AI backend → Markdown-rendered beverage suggestions appear below recipe.  
- ✅ Local testing passed for both recipe and beverage pairing flows.

**Next Steps:**
- Continue enhancing UI styling for beverage pairings section.

---

## 🚀 Sprint N+2 Progress Update — Dish Pairing Suggestion Feature

**Status:** Completed  
**Date:** 2025-11-05  
**Implemented Components:**
- ✅ Added new backend endpoint `/api/v1/ai/dish-pairings` to generate complementary dish suggestions (appetizer, entrée, main course, dessert) intelligently based on recipe type.  
- ✅ Integrated new frontend button “Give me dish pairings for this recipe.”  
- ✅ Created frontend UI element and JavaScript logic using `fetch()` to call the backend API.  
- ✅ Implemented Markdown rendering and sanitization using `marked.js` and `DOMPurify`.  
- ✅ Verified local response and display accuracy for all dish types.  
- ✅ End-to-end testing passed successfully: recipe → AI dish pairing response → visual Markdown rendering.  

**Next Steps:**
- Coordinate with Infra Architect for deployment to Vercel (frontend) and Render (backend).  
- Confirm dish pairing latency benchmarks and AI response consistency post-deployment.  
- Prepare for final review and deployment to production in collaboration with Infra Architect.
