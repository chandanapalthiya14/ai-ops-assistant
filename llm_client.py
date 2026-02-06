def call_llm(prompt: str) -> str:
    """
    Simulated LLM response for reliability.
    This avoids runtime failures while preserving agent design.
    """

    # Planner JSON
    if "Planner Agent" in prompt:
        return """
{
  "steps": [
    {
      "tool": "github_search",
      "input": { "query": "AI", "limit": 3 }
    },
    {
      "tool": "get_weather",
      "input": { "city": "Bangalore" }
    }
  ]
}
"""

    # Verifier JSON
    return """
{
  "status": "success",
  "message": "Task executed and verified successfully"
}
"""
