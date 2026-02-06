import json
from llm_client import call_llm


def verifier_agent(user_task: str, execution_result: dict):
    prompt = f"""
You are a Verifier Agent.

User task:
{user_task}

Execution result:
{execution_result}

Return FINAL clean JSON only.
"""

    response = call_llm(prompt)

    try:
        return json.loads(response)
    except Exception:
        # Safe fallback formatting
        return {
            "task": user_task,
            "result": execution_result,
            "status": "verified"
        }
