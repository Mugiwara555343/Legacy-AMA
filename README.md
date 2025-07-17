# AI Memory Architecture

> A modular AI system that reflects, summarizes, and stylizes your memory — using local language models chained together in a persistent, privacy-first pipeline.

Built as a **personal cognitive architecture**, this project processes Obsidian-style `.md` logs and transforms them into structured `.json` snapshots and stylized `.md` narratives. All locally, no cloud required using LLMs to get to enriched AI output.

👉 [Try my custom GPT assistant](https://chatgpt.com/g/g-686d56d1a8048191bd32fdb5704d2eb4-memoryarchitect-gpt?model=o4-mini)
It helps coordinate the models and memory flow behind this repo.

---

## 🔍 What It Does

* Watches `.md` logs for changes and parses them into structured `.json`
* Routes parsed memory through a **multi-model LLM chain**:

  * 🤍 Capybara → tags & emotions
  * 🧠 Hermes → summary metadata
  * 🎭 MythoMax → Markdown stylization
* Optionally pipes output into TTS (e.g., ElevenLabs) or future dashboards

---

## 📊Visual Flow

[![Memory Architecture Simple Diagram](./docs/memory_flow_diagram_dark(2).png)](./docs/memory_flow_diagram_dark(2).png)
[![First Draft Diagram](./docs/memory_flow_diagram_dark.png)](./docs/memory_flow_diagram_dark.png)
*A visual of the full offline memory chain — from raw journal to reflective output*

---

## 🧠 AI Memory Workflow Showcase

This section visually documents the real-time behavior of the local AI memory system — from journal creation to model parsing and multi-step inference. Each screenshot shows a critical step in how memory is detected, routed, and transformed by local language models in a modular chain.

---

### 1. ✍️ Memory Entry Logged

![Memory Entry](./docs/images/Screenshot-2025-07-12-035005.png)  
A journal entry (`.md`) is created in `memory_core/02_Training_&_Discipline`. This triggers the `memory_watcher.py`, which detects file changes automatically.

---

### 2. 🔁 Watcher + Parser Activated

![Watcher Trigger](./docs/images/Screenshot-2025-07-12-040512.png)  
The file watcher logs activity: detecting the new `.md` file, parsing it, and routing it through the `router_sequence.json`. Parsed `.json` and `.parsed.md` files are generated and stored.

---

### 3. 🧠 Multi-Model Inference Begins

![Model Chaining](./docs/images/Screenshot-2025-07-12-114321.png)  
The pipeline routes the parsed memory through 3 local LLMs:
- **Capybara** extracts emotions + tags  
- **Hermes** generates semantic summaries  
- **MythoMax** stylizes and enhances the final `.md` narrative  

Each model runs in its own session with detailed log output.

---

### 4. 📄 Structured Output Produced

![Parsed JSON Output](./docs/images/Screenshot-2025-07-12-202332.png)  
A `.parsed.json` is created with tags, tone, meaning, and quotes — plus a stylized Markdown file showing the enhanced narrative. This allows both human and machine-readable outputs to coexist.

---

### 5. ⚠️ Error Handling (Capybara Timeout)

![Model Error & Fallback](./docs/images/Screenshot-2025-07-12-213427.png)  
If a model fails (e.g., no valid JSON from MythoMax), the system logs a warning and continues with a fallback. This ensures resilience and recovery without manual intervention.

---

> This memory pipeline is fully offline and modular — a living architecture that turns raw thought into structured cognition. Built entirely with local tools.

---

## 📂 Folder Overview

```
memory/                # Human logs + parsed memory snapshots
scripts/               # Core processors(parser.py and watcher.py) + routers
n8n-workflows/         # Workflow automation (optional)
docs/                  # Progress reports, brainstorming, anything really
```

---

## ⚙️ How to Run

```bash
git clone https://github.com/Mugiwara555343/ai-memory-architecture.git
WORKING ON IT
```

✅ Markdown gets parsed
🧠 Models run in sequence
📄 Output: `.parsed.json` + stylized `.md` in terminal

---

## 📆 Example Output

```json
{
  "title": "First Encounter with Memory Core",
  "summary": "Reflective log capturing emotional tension and resolve.",
  "tags": ["memory", "emotion", "introspection"],
  "emotions": {"calm": 0.6, "anxious": 0.4}
}
```

---

## 🧱 Roadmap (Active)

*

---

## 👷️‍♂️ Tech Stack

* Python 3.11
* llama.cpp (`llama-cpp-python`)
* FastAPI + Gradio
* n8n (optional workflow glue)
* Watchdog (live file watching)
* ElevenLabs (optional TTS)

---

## 🙌 Creator

Built by **Mauricio Ventura**
AI Systems Builder | Automation Architect

> “Not just a note-taker — a local-first second brain.”

---
