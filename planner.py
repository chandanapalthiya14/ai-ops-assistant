import json
from llm_client import call_llm


def planner_agent(user_task: str):
    prompt = f"""
You are a Planner Agent.

Break the user task into steps.

Available tools:
- github_search (query, limit)
- get_weather (city)

Return ONLY valid JSON. No explanations.

Example format:
{{
  "steps": [
    {{
      "tool": "github_search",
      "input": {{ "query": "AI", "limit": 3 }}
    }},
    {{
      "tool": "get_weather",
      "input": {{ "city": "Bangalore" }}
    }}
  ]
}}

User task:
{user_task}
"""

    response = call_llm(prompt)

    try:
        return json.loads(response)
    except Exception:
        # Fallback plan (never crash)
        return {
            "steps": [
                {
                    "tool": "github_search",
                    "input": {"query": "AI", "limit": 3}
                },
                {
                    "tool": "get_weather",
                    "input": {"city": "Bangalore"}
                }
            ]
        }
