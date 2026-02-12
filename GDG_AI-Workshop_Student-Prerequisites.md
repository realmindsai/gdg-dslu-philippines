# GDG AI Workshop — Student Prerequisites

**Event:** Saturday 14 February 2026 | Globe BGC, Manila
**Presenter:** Dr Dennis Wollersheim, Real Minds AI

---

## Before the Workshop

Please complete these steps **before arriving** so we can maximise hands-on time.

### Bring Your Laptop

- Fully charged (power outlets may be limited)
- Any operating system (Windows, Mac, Linux, ChromeOS)
- At least 4GB RAM recommended

All tools below are **optional** — we'll work with whatever you have. More tools = more options to explore.

---

## 1. Package Managers (Recommended)

Modern package managers make installing AI tools painless. Also, you want to make your AI tools useful. Pick **one** for each language.

### Python: uv (Preferred)

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Verify:** `uv --version`

**Already have Python?** Any Python 3.10+ works (pyenv, conda, homebrew) — just not system Python.

---

### Node.js: Bun (Preferred)

**macOS/Linux:**
```bash
curl -fsSL https://bun.sh/install | bash
```

**Windows:**
```powershell
powershell -c "irm bun.sh/install.ps1 | iex"
```

**Verify:** `bun --version`

**Already have Node?** Any Node 18+ works (nvm, fnm, volta).

---

## 2. AI Model Access

Pick **at least one**. Subscription access works — no API key required for basic use.

### Antigravity IDE

https://antigravity.google/

---

### Google Gemini Command Line (CLI)

https://github.com/google-gemini/gemini-cli

---

### Anthropic Claude Code CLI

https://code.claude.com/docs/en/setup

Requires subscription or API key from [console.anthropic.com](https://console.anthropic.com)

---

### OpenAI Codex CLI

https://developers.openai.com/codex/cli/ 

Requires subscription or API key from [platform.openai.com](https://platform.openai.com)

---

## Pre-Workshop Checklist

| Priority | Tool | How to Check |
|----------|------|--------------|
| High | uv or Python 3.10+ | `uv --version` or `python --version` |
| High | Bun or Node 18+ | `bun --version` or `node --version` |
| High | Gemini access | gemini --version |
| Medium | Antigravity | `antigravity --version` |
| Medium | Claude access | claude --version |
| Low | OpenAI access | codex --version |

---

## Troubleshooting

**"Command not found"** — Restart terminal after installation

**Windows path issues** — Use Windows Terminal, or add to PATH manually

**No API key?** — Subscription/browser access works fine for the workshop

---

**Questions?** We'll do a setup check at the start of the workshop.

---

**Real Minds Artificial Intelligence** | wisdom, amplified
[realmindsai.au](https://realmindsai.au)
