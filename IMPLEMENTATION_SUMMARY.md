# Implementation Summary: Enforcing Document-Driven Development

This document summarizes the safeguards and teaching materials added to ensure students follow the document-driven development methodology, even when AI models change.

---

## Problem Solved

✅ **Before:** Students skip documentation and jump to coding. AI ignores `.github/copilot-instructions.md`. Different models produce different (sometimes bad) outputs.

✅ **After:** 
- Documentation is the gatekeeper (required before code)
- Phase-gating forces incremental development
- Validation scripts catch violations automatically
- Templates work with ANY AI model
- Students learn to ask AI the right questions in the right order

---

## What Was Added

### 1. **Enhanced Documentation**

#### [README.md](README.md) — Explicit Workflow
- 4-component project template
- **Workflow section** showing 3 clear steps (Clarify → Plan → Implement)
- Copy-paste prompt templates for Phase 1, 2, 3
- Rules about what NOT to do

#### [STUDENT_GUIDE.md](STUDENT_GUIDE.md) — Quick Reference
- 3-step workflow summary
- Common AI mistakes + how to reject them
- Validation commands
- Model-agnostic explanation (works with any model)
- PR checklist

#### [PROMPT_TEMPLATES.md](PROMPT_TEMPLATES.md) — Copy-Paste Ready
- 5 templates for different phases
- Rules section to paste into every prompt
- Common mistakes for each phase
- Troubleshooting

#### [docs/exercises.md](docs/exercises.md) — Concrete Examples
- Exercise 1: Single agent with MQTT
- Exercise 2: Multiple agents (distributed)
- Exercise 3: Dashboard with anymap-ts
- Proper notebook structure examples
- Checklist before submitting

#### [docs/INSTRUCTOR_GUIDE.md](docs/INSTRUCTOR_GUIDE.md) — For You
- Why this methodology matters
- How to verify each phase
- Model-agnostic explanation
- Handling model changes (including "auto" selection)
- Assessment rubric
- Common issues and solutions
- FAQ

### 2. **Validation Tools**

#### [scripts/verify_setup.py](scripts/verify_setup.py)
Checks that the environment is correct:
- ✅ Required packages installed
- ✅ anymap-ts present (not folium)
- ✅ No conflicting packages
- Runs independently of the phase

#### [scripts/validate_structure.py](scripts/validate_structure.py)
Checks code structure (prevents bad architecture):
- ❌ No monolithic notebooks (>300 cells, >3000 lines)
- ❌ No folium/matplotlib/plotly for real-time data
- ❌ No `!pip install` inside notebooks
- ❌ No subprocess-based package installation
- ⚠️  Warns if agent notebooks don't use MQTT

**Students run before every commit:**
```bash
python scripts/verify_setup.py
python scripts/validate_structure.py
python -m pytest
```

### 3. **Enhanced Templates**

#### [.github/pull_request_template.md](.github/pull_request_template.md)
New checklist:
- Which phases completed?
- Did you follow the 3-step workflow?
- Did you run validation scripts?
- Which docs updated?
- Tests passing?

#### [.github/copilot-instructions.md](.github/copilot-instructions.md)
Added:
- Model-agnostic approach section
- How to handle model switching
- What to do if AI refuses to follow instructions
- Comprehensive enforcement guide for instructors

### 4. **Enhanced Setup Documentation**

#### [docs/setup.md](docs/setup.md)
Added:
- Verification step with `python scripts/verify_setup.py`
- Troubleshooting section
- Explicit removal of folium
- Explanation of notebook structure

---

## How Students Use This (Workflow)

### Phase 1: Design Clarification (Days 1-2)
1. Fill in README template (4 components)
2. Copy [PROMPT_TEMPLATES.md](PROMPT_TEMPLATES.md) Template 1 into AI chat
3. Iterate until design is clear
4. Save clarified design in README

### Phase 2: Implementation Planning (Day 2-3)
1. Copy Template 2 from [PROMPT_TEMPLATES.md](PROMPT_TEMPLATES.md)
2. Get phased plan from AI (5-6 phases)
3. Review and approve plan

### Phase 3+: Phased Implementation (Week 1-2)
1. Copy Template 3 from [PROMPT_TEMPLATES.md](PROMPT_TEMPLATES.md)
2. Ask for Phase 1 implementation only
3. Run validation:
   ```bash
   python scripts/verify_setup.py
   python scripts/validate_structure.py
   python -m pytest
   python -m jupyterlab  # test the notebook
   ```
4. Understand the code
5. Submit PR with "Phase 1" in description
6. Once approved, ask for Phase 2 (using Template 4)

---

## How You (Instructor) Use This

### Before Class
1. Review [docs/INSTRUCTOR_GUIDE.md](docs/INSTRUCTOR_GUIDE.md)
2. Share [STUDENT_GUIDE.md](STUDENT_GUIDE.md) and [PROMPT_TEMPLATES.md](PROMPT_TEMPLATES.md) with students
3. Show them [docs/exercises.md](docs/exercises.md) for examples

### During Student Work
1. Check Phase 1 submission: Does README have clarified design?
2. Run validation: `python scripts/validate_structure.py`
3. Review code against `.github/copilot-instructions.md`
4. If they violate rules, point them to STUDENT_GUIDE.md
5. If AI violated rules, show them how to reject using PROMPT_TEMPLATES.md

### Model Switching
If your school switches models (or uses "auto"):
- **Nothing changes.** The templates are model-agnostic.
- Validation scripts catch violations no matter which model wrote them.
- If a new model doesn't follow rules, students paste Template 1-5 again with added context.

---

## Key Features

### ✅ Model-Agnostic
- Works with ChatGPT, Claude, Copilot, or any model
- Validation happens locally, not at the model level
- Templates embed constraints, so any model sees the rules

### ✅ Enforced at Multiple Levels
1. **Documentation** — README and approved plan are the source of truth
2. **Prompts** — Templates embed rules
3. **Phase-gating** — One phase at a time
4. **Validation scripts** — Catch violations automatically
5. **Code review** — You verify before merging

### ✅ Student Learning
- Learn to clarify requirements with AI (not just code-gen)
- Learn structured prompting (how to ask the right questions)
- Learn to validate and reject bad output
- Learn distributed architecture (MQTT agents)
- Learn to work with any model

### ✅ Scalable
- Works for 5 students or 500
- Validation runs on each commit
- Templates can be adapted for different projects
- Same approach works for different AI models

---

## Summary Checklist

Add this to your course materials:

### Files to Share with Students
- [ ] [README.md](README.md) — Main workflow
- [ ] [STUDENT_GUIDE.md](STUDENT_GUIDE.md) — Quick reference
- [ ] [PROMPT_TEMPLATES.md](PROMPT_TEMPLATES.md) — Copy-paste prompts
- [ ] [docs/exercises.md](docs/exercises.md) — Concrete examples
- [ ] [docs/setup.md](docs/setup.md) — Environment setup

### Files for You (Instructor)
- [ ] [docs/INSTRUCTOR_GUIDE.md](docs/INSTRUCTOR_GUIDE.md) — Full teaching guide
- [ ] [.github/copilot-instructions.md](.github/copilot-instructions.md) — Rules
- [ ] [.github/pull_request_template.md](.github/pull_request_template.md) — PR checklist

### Validation Tools (Students Run)
- [ ] `python scripts/verify_setup.py` — Check environment
- [ ] `python scripts/validate_structure.py` — Check code structure
- [ ] `python -m pytest` — Run tests

---

## Model Flexibility: A Real Example

**Scenario:** Student uses ChatGPT for Phase 1, Claude for Phase 2, CodePilot for Phase 3

**What happens?**
1. Each AI gets a complete prompt with all rules embedded
2. Each AI produces slightly different outputs
3. **Validation scripts** catch any violations from any model
4. Student tests locally before submitting
5. You review using the same checklist regardless of which AI was used

**Bottom line:** The model doesn't matter. The workflow does.

---

## Questions?

See [docs/INSTRUCTOR_GUIDE.md](docs/INSTRUCTOR_GUIDE.md) FAQ section for detailed answers.

---

## Final Setup

To make this active in your course:

```bash
# Ensure scripts are executable
chmod +x scripts/verify_setup.py scripts/validate_structure.py

# Test them
python scripts/verify_setup.py
python scripts/validate_structure.py

# Commit everything
git add -A
git commit -m "Add document-driven development enforcement: templates, guides, validation scripts"
```

Then share the links with students and start with Phase 1 of your first project!
