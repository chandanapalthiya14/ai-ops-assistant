# AI Operations Assistant (GenAI Intern Assignment)

This project is a lightweight **AI Operations Assistant** built using a **multi-agent architecture**.  
It accepts a natural-language task, plans the required steps, executes real tools (APIs), and verifies the final result.

The system is designed to **run locally**, demonstrate **agent-based reasoning**, **structured outputs**, and **real API integrations**, as required in the assignment.

---

##  Features

- Multi-agent design (Planner, Executor, Verifier)
- Structured planning and verification
- Real third-party API integrations
- End-to-end task execution
- One-command local run

---

##  Architecture Overview

The system follows a **three-agent workflow**:

### 1. Planner Agent
- Interprets the user’s natural-language task
- Breaks it into structured steps
- Outputs a JSON execution plan

### 2. Executor Agent
- Executes each planned step
- Calls real external APIs
- Collects raw results

### 3. Verifier Agent
- Validates the execution output
- Ensures completeness
- Returns a clean, structured final response

---

##  APIs Integrated

- **GitHub Search API**  
  Used to fetch top repositories based on stars and relevance.

- **OpenWeatherMap API**  
  Used to fetch live weather information by city.

- **LLM Interface**  
  Used for planning and verification with structured JSON outputs.  
  (Abstracted to ensure stable local execution during evaluation.)

---

## ⚙️ Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt
