import os
import json
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from google.genai import types

# --- Setup (same as before) ---
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI(title="Jana's AI API")

# Allow a frontend (Day 5) to call this API from the browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # we'll tighten this when we deploy
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Define the SHAPE of incoming requests ---
class ChatRequest(BaseModel):
    message: str

class ReviewRequest(BaseModel):
    review: str

# --- Endpoint 1: a simple health check ---
@app.get("/")
def home():
    return {"status": "online", "message": "Jana's AI API is running"}

# --- Endpoint 2: chat ---
@app.post("/chat")
def chat(request: ChatRequest):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=request.message,
        config=types.GenerateContentConfig(
            system_instruction="You are Pixel, a friendly, concise assistant.",
            temperature=0.7,
        ),
    )
    return {"reply": response.text}

# --- Endpoint 3: review analyzer (your Day 3 work, now an API) ---
SYSTEM = """You are a data extraction tool. Return ONLY valid JSON:
{"sentiment":"positive|negative|neutral","score":<1-5 int>,"topics":[strings],"summary":"one sentence"}
No explanations, no code fences."""

@app.post("/analyze")
def analyze(request: ReviewRequest):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=request.review,
        config=types.GenerateContentConfig(system_instruction=SYSTEM, temperature=0),
    )
    text = response.text.strip()
    if text.startswith("```"):
        text = text.strip("`").replace("json", "", 1).strip()
    return json.loads(text)