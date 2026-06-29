# My Prompt Patterns

## Force structured JSON output
- Give the model a clear ROLE ("you are a data extraction tool")
- Specify the EXACT JSON shape you want
- Say "return ONLY valid JSON, no explanations or code fences"
- Set temperature=0 for consistency
- Strip ``` fences, then json.loads() to parse