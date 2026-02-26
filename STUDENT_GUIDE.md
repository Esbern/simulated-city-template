# Student Quick Reference: Document-Driven AI Development

## The Workflow (3 Steps)

### Step 1: Clarify (AI helps write docs, not code)
Copy this prompt into your AI chat:
```
I want to build a simulated city based on this outline. 
Please help me clarify it before I code.

[Paste your Project from README]

Please:
1. Rewrite the 4 components using clear technical language
2. Identify MQTT topics each agent will publish/subscribe to
3. List configuration parameters (MQTT broker, locations, thresholds)
4. Point out any ambiguities

Do NOT write code.
```

### Step 2: Plan (AI proposes phases, you approve)
```
Based on the design we just clarified:
[Paste clarified design]

Please propose phased implementation:
- Phase 1: Single basic agent
- Phase 2: Add config file
- Phase 3: Add MQTT publishing
- Phase 4: Add second agent with MQTT subscription
- Phase 5: Add dashboard

For each, list new files, tests, and what you should investigate first.

Do NOT write code.
```

### Step 3: Implement (ONE phase at a time)
```
Implement ONLY Phase 1:
[Paste Phase 1]

Rules (from .github/copilot-instructions.md):
- Use anymap-ts (NOT folium)
- Each notebook = ONE agent (NOT monolithic)
- Load config via simulated_city.config.load_config()
- Use mqtt.publish_json_checked() for publishing
- Add all dependencies to pyproject.toml

Only Phase 1. Do NOT jump to Phase 2.
```

After code: Test it, understand it, then ask for Phase 2.

---

## Common AI Mistakes (And How to Fix Them)

### ❌ AI tries to code without clarifying design
You: "No code yet. Use Phase 1 prompt from README.md to clarify the design first."

### ❌ AI proposes all 5 phases at once
You: "We'll implement one at a time. Give me only Phase 1 implementation."

### ❌ AI uses folium instead of anymap-ts
You: "No, use anymap-ts. Check .github/copilot-instructions.md for the rules."

### ❌ AI creates one big notebook instead of agent notebooks
You: "Split into separate notebooks. Each agent publishes/subscribes via MQTT. See docs/exercises.md."

### ❌ AI uses !pip install in notebook
You: "Don't install in notebooks. Add to pyproject.toml and run: pip install -e '.[notebooks]'"

---

## Validation Commands

```bash
# Check dependencies are correct
python scripts/verify_setup.py

# Check code structure (no monolithic notebooks, no folium)
python scripts/validate_structure.py

# Run tests
python -m pytest

# Open notebooks and test manually
python -m jupyterlab
```

---

## If Your Model Switches (Auto Mode)

The workflow is **model-agnostic**. It works with any AI because:
1. You write artifacts (README clarification, approved design)
2. Each prompt is self-contained with full rules embedded
3. You validate output locally before moving forward

If a new model doesn't follow rules, respond with the "Common AI Mistakes" section above.

---

## PR Checklist Before Submitting

- [ ] README filled in with 4-component template
- [ ] AI clarified design (saved in docs or PR description)
- [ ] You approved implementation plan
- [ ] Only ONE phase implemented in this PR
- [ ] Tests passing: `python scripts/verify_setup.py && python -m pytest`
- [ ] Structure valid: `python scripts/validate_structure.py`
- [ ] PR description says which phase(s) included
