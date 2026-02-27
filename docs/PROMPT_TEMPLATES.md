# Prompt Templates for AI-Assisted Development

Copy-paste these into your AI chat. Don't modify them unless your instructor approves.

---

## Understanding AI Modes

**CRITICAL:** Always tell the AI which mode to operate in. Include this at the start of every prompt:

### Three Operating Modes

1. **ASK MODE** - AI asks clarifying questions, validates assumptions, does NOT design or implement
   - Use when: You have a vague idea and need help refining it through conversation
   - AI behavior: Asks questions, points out gaps, does NOT propose solutions yet
   - Output: Questions and clarifications (no files created)

2. **PLAN MODE** - AI writes documentation (markdown files), does NOT implement code
   - Use when: Requirements are clear and you need structured documentation
   - AI behavior: Creates markdown files (concepts.md, implementationplan.md), does NOT write code
   - Output: Documentation files that can be reviewed and versioned
   - **Used in Steps 1 and 2 of the workflow**

3. **AGENT MODE** - AI implements code based on approved documentation
   - Use when: Design is approved and you're ready for one specific phase
   - AI behavior: Writes code, creates notebooks, implements exactly what was approved
   - Output: Python files, notebooks, code
   - **Used in Step 3+ of the workflow**

### Why This Matters

Without explicit mode instructions, the AI may:
- Write code when you only wanted documentation (wrong mode)
- Ask questions when you're ready to create documentation (wrong mode)
- Implement multiple phases at once (wrong scope)

**Solution:** Every prompt below starts with "MODE: [ASK/PLAN/AGENT]" — copy it exactly.

### Documentation-First Workflow

```
Step 1 (PLAN mode) → docs/concepts.md
Step 2 (PLAN mode) → docs/implementationplan.md
Step 3+ (AGENT mode) → Code (one phase at a time)
```

Both documentation files are committed to git BEFORE any code is written.

---

## Template 1: Design Clarification → `docs/concepts.md`

**Use this when:** You have a rough idea and want AI to create a design document.

```
MODE: PLAN

I want to build a simulated city. Please create a design document that clarifies the architecture BEFORE I write any code.

You are operating in PLAN mode:
- Create a file: docs/concepts.md
- Write structured documentation in markdown
- Do NOT write any code
- Do NOT ask me questions (make reasonable assumptions)

## My Project Idea
[Copy the 4-component template from README.md and fill it in]

Please create docs/concepts.md with these sections:

### 1. System Overview
Rewrite my 4 components (Trigger, Observer, Control, Response) using clear technical language.

### 2. MQTT Architecture
- List all MQTT topics
- For each topic, specify:
  * Which agent publishes to it
  * Which agents subscribe to it
  * Message schema (JSON structure)

### 3. Configuration Parameters
List all parameters that should go in config.yaml:
- MQTT broker settings (host, port, username, password)
- GPS coordinates (if applicable)
- Thresholds and limits
- Timing parameters
- Suggest realistic default values

### 4. Architecture Decisions

#### Notebooks to Create
List each notebook file and its purpose (one notebook per agent).

#### Library Code (src/simulated_city/)
Identify reusable components that should go in library code:
- Data models (dataclasses)
- Utility functions
- Calculation helpers

#### Classes vs Functions
- What should be modeled as classes (agents with state, data models)
- What should be simple functions (calculations, transformations)

### 5. Open Questions
List any ambiguities or assumptions you made that I should validate.

---

Create the docs/concepts.md file now. Use markdown formatting with proper headings and bullet points.

When you're done, I'll review and edit it before moving to the implementation plan.
```

---

## Template 2: Implementation Planning → `docs/implementationplan.md`

**Use this when:** Design (concepts.md) is approved and you're ready for a phased implementation plan.

```
MODE: PLAN

Great! The design in docs/concepts.md is approved. Now please create an implementation plan.

You are operating in PLAN mode:
- Create a file: docs/implementationplan.md
- Describe phases and structure
- Do NOT write any code yet
- Do NOT implement anything yet

Please create docs/implementationplan.md based on the approved design:
[Attach or reference docs/concepts.md]

Structure the plan with these phases:
- Phase 1: Minimal working example (one agent, basic logic, no MQTT yet)
- Phase 2: Add configuration file (config.yaml with MQTT and simulation parameters)
- Phase 3: Add MQTT publishing (agent publishes to topics)
- Phase 4: Add second agent with MQTT subscription (agents communicate)
- Phase 5: Add dashboard visualization (anymap-ts)
- Phase 6+: [Additional phases if needed]

For EACH phase, provide:

### Phase X: [Title]

**Goal:** [One sentence describing what this phase achieves]

**New Files:**
- List files to create or modify
- Specify whether it's a notebook, library module, or config file

**Implementation Details:**
- Key classes or functions to implement
- MQTT topics involved (if applicable)
- Configuration parameters needed

**Dependencies:**
- Any new packages to add to pyproject.toml

**Verification:**
- Commands to run: `python scripts/verify_setup.py`, `python -m pytest`, etc.
- What to test manually (e.g., "Open notebook, run cells, check output")

**Investigation:**
- What should I understand or explore before moving to the next phase?

---

Create the docs/implementationplan.md file now. Use markdown with clear phase headings.

When you're done, I'll review it with my instructor before starting Phase 1 implementation.
```

---

## Template 3: Phase 1 Implementation (Step 3+)

**Use this when:** You've approved docs/implementationplan.md and are ready for Phase 1 code.

```
MODE: AGENT

Good! I approve the implementation plan. Now implement ONLY Phase 1:

You are operating in AGENT mode:
- Write code and create files
- Implement only what's described in Phase 1
- Do NOT ask permission
- Do NOT plan other phases
- Do NOT jump ahead to Phase 2+

## Phase 1 (from docs/implementationplan.md)
[Copy and paste ONLY the Phase 1 section from docs/implementationplan.md]

## Rules (from .github/copilot-instructions.md)
These are non-negotiable:
1. Use anymap-ts for mapping (NEVER folium, matplotlib, or plotly for real-time data)
2. Each notebook represents ONE agent (NEVER combine multiple agents in one notebook)
3. Load configuration via simulated_city.config.load_config() (never hardcode values)
4. Use mqtt.publish_json_checked(client, topic, data) for verified publishing
5. Use mqtt.connect_mqtt(mqtt_config) to connect
6. Add all dependencies to pyproject.toml FIRST, run: pip install -e ".[notebooks]"
   (NEVER use !pip install inside notebooks)
7. Start with comments explaining each cell's purpose

DO NOT:
- Create a monolithic notebook
- Ask for phases 2-6 yet
- Suggest installing folium or matplotlib for real-time data
- Hardcode MQTT settings or coordinates
- Suggest !pip install inside the notebook code

Only implement Phase 1. Stop here.

Create a new cell with the code, or create a new notebook file. Include comments.
```

---

## Template 4: Next Phase Implementation

**Use this when:** Phase N is working and you're ready for Phase N+1.

```
MODE: AGENT

Good! Phase [N] works. Now implement ONLY Phase [N+1]:

You are operating in AGENT mode:
- Write code for Phase [N+1] only
- Do NOT modify previous phase code unless necessary
- Do NOT ask permission
- Do NOT jump to Phase [N+2]+

## Phase [N+1] (from docs/implementationplan.md)
[Copy and paste ONLY the Phase N+1 section from docs/implementationplan.md]

## Previous Phase Artifacts
These were created in previous phases:
[List the notebooks/files created - e.g., notebooks/agent_transport.ipynb, config.yaml]

Do NOT modify previous phase code unless absolutely necessary.

Remember the rules from Template 3.

Only implement Phase [N+1]. Stop here.
```

---

## Template 5: Bug Fix or Clarification

**Use this when:** Code from previous phase has an error.

```
MODE: AGENT

The code from [Phase X] has a problem:

[Describe the error or unexpected behavior]

Please fix it while keeping the same overall structure.

Remember:
- Don't change the design (that was already approved)
- Don't jump to other phases
- Don't add new features
- Just fix the specific issue

[Paste the problematic code]
```

---

## Rules to Paste Into Every Prompt

If the AI ever ignores the templates above, paste this:

```
RULES from .github/copilot-instructions.md:
❌ DO NOT:
- Install folium, plotly, or matplotlib for real-time maps (use anymap-ts)
- Create one big notebook with all agents (split into separate notebooks)
- Hardcode MQTT settings (use config.yaml)
- Use !pip install inside notebooks (add to pyproject.toml)
- Call subprocess.run(["pip", "install", ...])

✅ DO:
- Use anymap-ts[all] from pyproject.toml for mapping
- Split simulations into agent notebooks (each publishes/subscribes via MQTT)
- Load config via: simulated_city.config.load_config()
- Use: mqtt.publish_json_checked(client, topic, data)
- Add dependencies to pyproject.toml, then: pip install -e ".[notebooks]"
```

---

## After AI Creates Documentation or Code

### After Steps 1-2 (Documentation)

1. **Review the markdown file** (concepts.md or implementationplan.md)
2. **Edit it if needed** - you can ask AI to refine specific sections:
   - "Expand the MQTT Architecture section with message schemas"
   - "Add more detail to Phase 3 verification steps"
3. **Commit to git:**
   ```bash
   git add docs/concepts.md
   git commit -m "Add design clarification"
   ```
4. **Get instructor review** before moving forward

### After Step 3+ (Code)

1. **Copy the code into your notebook or create a new file**
2. **Run validation:**
   ```bash
   python scripts/verify_setup.py
   python scripts/validate_structure.py
   python -m pytest
   ```
3. **Test manually:**
   ```bash
   python -m jupyterlab
   # Open the notebook, run all cells, verify it works
   ```
4. **Understand the code:**
   - Can you explain what each cell does?
   - Does it match the design in docs/concepts.md?
   - Does it match the phase description in docs/implementationplan.md?

5. **If it works:** Commit, create PR, move to next phase after approval
6. **If it doesn't work:** Use Template 5 to ask for fixes

---

## Common Mistakes During Each Phase

### Mode Violations (Most Common Error)
- ❌ AI writes code in ASK mode → **Reject:** "You're in ASK mode. Do NOT write code. Just ask questions."
- ❌ AI asks questions in PLAN mode → **Reject:** "You're in PLAN mode. Create the documentation file, don't ask me questions."
- ❌ AI asks permission in AGENT mode → **Reject:** "You're in AGENT mode. Implement it, don't ask."
- ❌ AI implements in PLAN mode → **Reject:** "You're in PLAN mode. Create markdown docs, don't implement code."

### Step 1: Design Clarification (PLAN Mode → docs/concepts.md)
- ❌ AI writes code → **Reject:** "You're in PLAN mode. Create docs/concepts.md documentation, not code."
- ❌ AI asks questions instead of creating file → **Reject:** "You're in PLAN mode. Create the file with reasonable assumptions. I'll edit it later."
- ❌ AI creates incomplete concepts.md → **Ask:** "Add missing sections: MQTT Architecture, Configuration Parameters, Architecture Decisions."

### Step 2: Planning (PLAN Mode → docs/implementationplan.md)
- ❌ AI writes code → **Reject:** "You're in PLAN mode. Create docs/implementationplan.md, don't implement."
- ❌ AI skips a phase → **Ask:** "Can you add a phase for X?"
- ❌ Phase descriptions are vague → **Reject:** "More specific. What files? What tests? What verification commands?"
- ❌ AI doesn't reference concepts.md → **Reject:** "Base the plan on the approved design in docs/concepts.md."

### Step 3+: Implementation (AGENT Mode)
- ❌ AI asks "Should I implement this?" → **Reject:** "You're in AGENT mode. Implement it now."
- ❌ AI uses folium → **Reject:** "Use anymap-ts. Rewrite it."
- ❌ AI creates one giant notebook → **Reject:** "Split this into separate agent notebooks."
- ❌ AI suggests `!pip install` → **Reject:** "Add to pyproject.toml instead."
- ❌ AI hardcodes MQTT settings → **Reject:** "Use config.yaml and config.load_config()."
- ❌ AI implements Phase 2 when asked for Phase 1 → **Reject:** "Only Phase 1 from docs/implementationplan.md. Stop here."
- ❌ AI deviates from implementationplan.md → **Reject:** "Follow the approved plan in docs/implementationplan.md exactly."

---

## Troubleshooting

**Q: AI operates in wrong mode (writes code when I want questions, or asks when I want code)**  
A: Paste this: "You are in [ASK/PLAN/AGENT] mode. Re-read the mode instructions in my prompt."

**Q: AI says "I don't see the copilot-instructions file"**  
A: Paste the Rules section above into your next message.

**Q: Validation scripts fail**  
A: Ask AI to fix the specific error using Template 5.

**Q: Code runs but seems wrong**  
A: Ask your instructor or re-read docs/exercises.md for examples.

**Q: Can I skip phases?**  
A: No (unless instructor approves). Each phase teaches something. Skipping breaks the learning.

---

## When the AI Model Changes (Auto Selection)

If your school switches models, use the **same templates**. The workflow is model-agnostic.

The validation scripts will catch violations no matter which model wrote the code.
