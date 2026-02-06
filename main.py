from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

from planner import planner_agent
from executor import executor_agent
from verifier import verifier_agent

load_dotenv()

app = FastAPI(title="AI Operations Assistant")


class TaskRequest(BaseModel):
    task: str


@app.post("/run")
def run_task(request: TaskRequest):
    plan = planner_agent(request.task)
    execution_result = executor_agent(plan)
    final_result = verifier_agent(request.task, execution_result)
    return final_result
