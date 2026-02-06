from github_tool import github_search
from weather_tool import get_weather


def executor_agent(plan: dict):
    results = {}

    for step in plan.get("steps", []):
        tool = step["tool"]
        inputs = step["input"]

        if tool == "github_search":
            results["github"] = github_search(
                query=inputs.get("query", "AI"),
                limit=inputs.get("limit", 3)
            )

        elif tool == "get_weather":
            results["weather"] = get_weather(
                city=inputs.get("city", "Bangalore")
            )

    return results
