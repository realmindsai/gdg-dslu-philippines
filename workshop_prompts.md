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
    color: #E8E8EC !important;
  }
  pre code span {
    color: #E8E8EC !important;
  }
  table {
    background: #1a1e38 !important;
    color: #E8E8EC !important;
    border-collapse: collapse !important;
    width: 100%;
  }
  th {
    background: #E76F51 !important;
    color: white !important;
    padding: 10px 16px !important;
    text-align: left;
    border: none !important;
  }
  td {
    padding: 10px 16px !important;
    border-bottom: 1px solid #2a2e48 !important;
    border-top: none !important;
    border-left: none !important;
    border-right: none !important;
    color: #E8E8EC !important;
    background: #1a1e38 !important;
  }
  tr:nth-child(even) td {
    background: #151935 !important;
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

# <span class="exercise-num">1</span> Task vs. Outcome Live Build

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

# <span class="exercise-num">2</span> Debug Like Pike

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

# <span class="exercise-num">3</span> Spec-Driven Build

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

# <span class="exercise-num">4</span> Build a Custom Agent

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

# <span class="exercise-num">5</span> Cross the Divide

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

<!-- _class: title-slide -->

# Mini Hackathon Projects

**4:00 PM — Choose one and build it in 45 minutes**

Review these options during the break. Come back with a team and a pick.

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

**Help:** Raise your hand, mentors are circulating

---

<!-- _class: title-slide -->

# Code is now free.

## Your value is in everything code can't do.

14 February 2026

---

# Connect With Us

**Dr Dennis Wollersheim** — Co-Founder & CTO
linkedin.com/in/dennis-wollersheim

**Tracy Anthony** — Co-Founder & CEO
linkedin.com/in/tracyanthony

**Real Minds AI** | wisdom, amplified
realmindsai.au

---

# Enjoyed Today?

## Leave us a Google review

![w:300](qr_google_review.png)

Scan to leave a review — it really helps us bring workshops like this to more communities.

**★ ★ ★ ★ ★**
