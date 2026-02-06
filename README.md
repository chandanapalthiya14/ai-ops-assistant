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
Running the Project

Run the project locally using one command:

uvicorn main:app


The API will be available at:

http://127.0.0.1:8000


Swagger UI:

http://127.0.0.1:8000/docs
## Example Prompts to Test the System (3–5)

Find top AI GitHub repositories and weather in Bangalore

Get trending ML repositories and Mumbai weather

Show GitHub AI projects and Delhi weather

Find popular data science repositories and Hyderabad weather

## Known Limitations / Tradeoffs

Sequential execution (no parallel API calls)

No caching of API responses

LLM calls are abstracted for deterministic local execution

Designed for clarity and reliability rather than scale
