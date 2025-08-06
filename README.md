# Legacy-AMA (v1 • Archived)

[![CI](…badge…)](…)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)

> **Offline, local-first AI memory assistant prototype.**  
> Parsed 400+ personal journals into structured JSON and routed context to multiple LLMs on an 8 GB GPU — fully air-gapped.

## 📦 Repo layout
| Path | Purpose |
|------|---------|
| **src/** | Core code – current parsers, watchers, Gradio UI |
| **api_clients/** | FastAPI wrappers for local LLMs (Capy, Hermes, MythoMax…) |
| **demo/** | Minimal demo pipeline for first-time users |
| **docs/images** | Diagrams, screenshots |
| **docs/troubleshooting** | Legacy debug shots |
| **docs/versions** | Early parser/watcher iterations |
| **workflows/** | Step-by-step execution guides |
| **archive/mini_projects** | Old learning scripts (kept for transparency) |

## 🚀 Python Quickstart
```bash
git clone https://github.com/Mugiwara555343/Legacy-AMA.git
cd Legacy-AMA
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/demo_run.py  # parses demo logs & returns a Q&A
```
