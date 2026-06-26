import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are Pixel, a friendly and concise assistant. Keep replies short and warm.",
        temperature=0.7,
    ),
)

print("🤖 Pixel is ready! Type your message. (type 'quit' to leave)\n")

while True:
    user_input = input("You: ").strip()

    # Skip empty input — just ask again
    if not user_input:
        continue

    if user_input.lower() == "quit":
        print("Pixel: Bye, Jana! 👋")
        break

    # Stream the reply word-by-word as it arrives
    print("Pixel: ", end="", flush=True)
    for chunk in chat.send_message_stream(user_input):
        print(chunk.text, end="", flush=True)
    print("\n")