import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# A STRICT system prompt: we tell the model exactly what shape to return
SYSTEM = """You are a data extraction tool.
You read a customer product review and return ONLY valid JSON — nothing else.
Use exactly this structure:
{
  "sentiment": "positive | negative | neutral",
  "score": <integer from 1 to 5>,
  "topics": [<short topic strings>],
  "summary": "<one short sentence>"
}
Do not include explanations, markdown, or code fences."""


def extract(review: str) -> dict:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=review,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM,
            temperature=0,   # 0 = consistent & repeatable, what we want here
        ),
    )

    text = response.text.strip()

    # Models sometimes wrap JSON in ```json ... ``` fences — strip them if present
    if text.startswith("```"):
        text = text.strip("`").replace("json", "", 1).strip()

    return json.loads(text)   # turn the JSON text into a real Python dict


# Try it on a sample review
review = ("I bought these headphones last week. The sound is amazing and the "
          "battery lasts forever, but they feel a bit tight on my ears.")

data = extract(review)

# Now we can USE the data like any Python dictionary
print("Sentiment:", data["sentiment"])
print("Score:    ", data["score"])
print("Topics:   ", data["topics"])
print("Summary:  ", data["summary"])