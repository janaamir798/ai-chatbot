# 🤖 Pixel — Full-Stack AI Chatbot

A full-stack AI chat application powered by Google's Gemini API, with a Python backend and a React frontend — deployed live.

## 🔗 Live Demo
**Try it:** https://ai-chatbot-lime-kappa.vercel.app

## ✨ Features
- Real-time chat with an AI assistant (Google Gemini)
- Conversation memory within a session
- Clean, responsive React interface
- RESTful API with automatic interactive docs

## 🛠️ Tech Stack
**Backend:** Python, FastAPI, Google Gemini API
**Frontend:** React (Vite)
**Deployment:** Render (API) + Vercel (frontend)

## 🏗️ Architecture
React frontend → FastAPI backend → Gemini API → response streamed back to the UI

## 🚀 Run Locally
\`\`\`bash
# Backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn api:app --reload

# Frontend (in a second terminal)
cd frontend
npm install
npm run dev
\`\`\`

Add a `.env` file with your `GEMINI_API_KEY` to run the backend.

## 👤 Author
Jana Alamir — Computer & Communications Engineering