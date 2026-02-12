---
marp: true
theme: default
paginate: true
backgroundColor: #0F1229
color: #E8E8EC
style: |
  section {
    font-family: 'Calibri', 'Segoe UI', sans-serif;
  }
  h1 {
    color: #FFFFFF;
    font-family: 'Georgia', serif;
    border-bottom: 3px solid #E8873A;
    padding-bottom: 12px;
  }
  h2 {
    color: #E8873A;
    font-family: 'Georgia', serif;
  }
  code {
    background: #1a1e38;
    color: #E8873A;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.85em;
  }
  pre {
    background: #1a1e38 !important;
    border-left: 4px solid #E76F51;
    padding: 16px !important;
    border-radius: 8px;
    font-size: 0.75em;
  }
  pre code {
    background: transparent;
    color: #E8E8EC;
  }
  .exercise-num {
    display: inline-block;
    background: #E76F51;
    color: white;
    padding: 4px 12px;
    border-radius: 16px;
    font-weight: bold;
    font-size: 0.9em;
  }
  strong {
    color: #E8873A;
  }
  a {
    color: #E8873A;
  }
  section.title-slide h1 {
    font-size: 2.5em;
    border-bottom: none;
  }
---

<!-- _class: title-slide -->

# Gemini CLI Workshop Prompts

## GDG Philippines AI Workshop
**14 February 2026** | Globe Tower, BGC

Copy-paste ready CLI prompts for every exercise

---

# Get the Workshop Prompts

## Scan to open on your phone

![w:300 center](qr_code.png)

**realmindsai.github.io/gdg-dslu-philippines**

All exercises, prompts, and hackathon options in one place.
Browse on your phone while you code on your laptop.

---

# Setup (1/2) - Package Managers

You need **one** package manager for each language.

## Python: uv (Recommended)

Install: **https://docs.astral.sh/uv/getting-started/installation/**

Verify: `uv --version`

## JavaScript: Bun (Recommended)

Install: **https://bun.sh/**

Verify: `bun --version`

---

# Setup (2/2) - AI Coding Tools

Install **at least one**. Subscription access works for all of these.

| Tool | Install Page |
|------|-------------|
| **Gemini CLI** (primary) | https://github.com/google-gemini/gemini-cli |
| **Antigravity IDE** | https://antigravity.google/ |
| **Claude Code** | https://docs.anthropic.com/en/docs/claude-code |
| **Codex CLI** | https://github.com/openai/codex |

Verify: `gemini --version`

---

# <span class="exercise-num">1</span> AI Market Research Sprint

**Segment: The Code Was Already Your Enemy**

Pick a local app idea, then run:

```bash
gemini "Generate 10 interview questions to validate demand
for [your app]. Include 3 questions about willingness to
pay. Format as a survey."
```

**App ideas:** jeepney route finder, sari-sari tracker, barangay complaints

**Your job:** Edit the output to add local context Gemini missed.

---

# <span class="exercise-num">2</span> Scaffold Showdown

**Segment: Operators vs. Engineers**

### The operator way:

```bash
gemini "Create a React app with Tailwind for a campus food tracker"
```

### The engineer way:

```bash
gemini "Build a campus food tracker. Students check what canteens
are open. Staff update menus daily. Use whatever stack makes sense."
```

**Compare:** What did Gemini choose vs. what you prescribed?

---

# <span class="exercise-num">3</span> Task vs. Outcome Live Build

**Segment: Outcome-Based Prompting**

### Task-based:

```bash
gemini "Create a Python Flask app with SQLite. Table called
complaints with id, barangay, description, status.
Add CRUD endpoints."
```

### Outcome-based:

```bash
gemini "Build a barangay complaint system. Residents submit
complaints, officials track and resolve them. Simple enough
for a barangay captain."
```

**Run both.** Which one would the barangay captain actually use?

---

# <span class="exercise-num">4</span> Debug Like Pike

**Segment: Direct the AI**

### Download the broken app:

```bash
curl -O https://raw.githubusercontent.com/realmindsai/gdg-dslu-philippines/main/broken_app.py
python3 broken_app.py
```

### Passive prompt:

```bash
gemini "Fix this code" < broken_app.py
```

### Directed prompt:

```bash
gemini "This app is slow rendering the dashboard. I suspect
database queries but it might be template rendering. Profile
the bottleneck first, then fix only that." < broken_app.py
```

---

# <span class="exercise-num">5</span> Build a Test Harness

**Segment: Feedback Loops**

```bash
gemini "Write a Python function that calculates jeepney fare:
13 pesos minimum for first 4km, then 1.80/km after.
Include a CLI test harness that takes distance as input
and prints expected vs actual fare.
Add edge cases: 0km, negative, exactly 4km, 100km."
```

### When a test fails, feed it back:

```bash
gemini "The fare function returns [X] for 0km but should
return [Y]. Fix it and re-run all tests."
```

---

# <span class="exercise-num">6</span> Spec-Driven Build

**Segment: Software Factory**

### Step 1: Write the spec

```bash
gemini "Help me write a spec for a class schedule manager
for Filipino college students. Include inputs, outputs,
edge cases, and 5 end-to-end scenarios." > my_spec.md
```

### Step 2: Build from spec

```bash
gemini "Build this app from the following spec.
Do not deviate." < my_spec.md
```

**Do NOT read the code.** Only test: do your 5 scenarios pass?

---

# <span class="exercise-num">7</span> Build a Custom Agent

**Segment: Agent Orchestration**

### Step 1: Create a system prompt file

Write 3-4 sentences in `agent_prompt.md` describing your agent.
Ideas: JobStreet assistant, GCash budget tracker, LTO scheduler.

### Step 2: Test it

```bash
gemini --system-instruction agent_prompt.md \
  "Find entry-level Python developer jobs in Makati
   with remote options"
```

### Step 3: Break it

Give it an out-of-scope task. Add a "never do" rule. Retry.

---

# <span class="exercise-num">8</span> Build the Agent Layer

**Segment: Three Layers of a Tech Business**

```bash
gemini "Build a CLI tool that queries a university student
database - enrollment status, grades, financial holds.
Use SQLite with 20 sample Filipino students.
Skip the dashboard - direct CLI access."
```

### Try it:

```
> Is Juan dela Cruz enrolled?
> What's Maria Santos' GPA?
```

You just replaced a dashboard with an agent.

---

# <span class="exercise-num">9</span> Cross the Divide

**Segment: The Capability Overhang**

### Casual way (5 min):

Ask ChatGPT: "Top 10 companies by revenue in the Philippines 2024?"

### Power user way (10 min):

```bash
gemini "Top 10 Philippine companies by revenue 2024.
Write a Python script - ranked bar chart, export PNG and CSV.
Use peso sign for currency."
```

**Compare:** Which output is usable in a report? Which could you extend?

---

# <span class="exercise-num">10</span> Your 30-Day CLI Challenge

**Segment: Your Career From Here**

```bash
gemini "Design a 30-day learning plan for a Filipino CS
graduate entering [industry]. Each week should have one
project buildable with Gemini CLI. Include specific
Philippine context - companies, regulations, pain points."
```

### Then start right now:

```bash
gemini "Build [Week 1 project description]"
```

**Industries:** BPO, fintech, healthcare, agriculture, media, education, logistics

---

<!-- _class: title-slide -->

# Mini Hackathon Projects

**Choose one and build it in 45 minutes**

---

# Hackathon Option A

## Barangay Service Portal

Build a complaint tracking system for a local barangay.

```bash
gemini "Build a web app for barangay complaint tracking.
Residents submit complaints with category and location.
Officials can update status and add notes.
Include a public dashboard showing resolution rates.
Use Python with SQLite. Deploy-ready."
```

**Judging:** Does it actually work for a barangay captain?

---

# Hackathon Option B

## Campus Schedule AI

Build a class schedule manager for Filipino college students.

```bash
gemini "Build a schedule management tool for Filipino
college students. Import class schedules, detect conflicts,
suggest optimal arrangements considering commute time
between buildings. Include a 'free time finder' for
study groups. Web UI with Python backend."
```

**Judging:** Would students at your university use this?

---

# Hackathon Option C

## Philippine Market Intelligence

Build a business research tool with real data visualization.

```bash
gemini "Build a CLI tool that generates Philippine business
reports. Given an industry name, it should: research top
companies, create revenue comparison charts, export a
professional PDF report with peso-formatted numbers.
Use Python with matplotlib."
```

**Judging:** Could you hand this report to a real investor?

---

# Hackathon Option D

## Your Own Idea

Build something that solves a real problem you've experienced.

**Requirements:**
- Must use Gemini CLI to build
- Must be testable in the demo
- Must address a Filipino context

```bash
gemini "Build [your idea]. [describe the users].
[describe the core workflow]. Keep it simple enough
to demo in 5 minutes."
```

**Judging:** Is it real? Would someone pay for it?

---

<!-- _class: title-slide -->

# Tips for Success

- **Be specific** about your users and their context
- **Iterate** - your first prompt won't be perfect
- **Test outcomes**, not code
- **Add local knowledge** the AI doesn't have

**WiFi:** GDG-Workshop
**Help:** Raise your hand, mentors are circulating

---

<!-- _class: title-slide -->

# Code is now free.

## Your value is in everything code can't do.

Dr Dennis Wollersheim | Real Minds AI
14 February 2026
