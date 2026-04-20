# 🧠 AI Bug Assistant (Full-Stack Project)

A full-stack web application that acts as an **AI-style debugging assistant**, helping developers identify causes, fixes, and examples for common programming errors.

Built using **FastAPI (Python backend)** and **React (frontend)**, this project simulates an AI-powered debugging tool using a structured rule-based engine.

---

## 🚀 Live Demo

*(Add after deployment)*

- 🌐 Frontend: https://your-app.vercel.app  
- ⚙️ Backend API: https://your-api.onrender.com  

---

## 📌 Project Overview

The AI Bug Assistant allows users to:

- Enter a bug or error description in natural language
- Receive instant structured debugging feedback
- Understand:
  - 🔍 Cause of the bug
  - 🛠️ Fix
  - 💡 Code example

This project simulates AI reasoning using a smart backend logic system (with future upgrade potential to LLM integration).

---

## 🧠 Key Features

- ⚡ Instant bug analysis response
- 🧠 AI-style rule-based reasoning engine
- 💬 Structured output (Cause → Fix → Example)
- 🌐 Full-stack integration (React + FastAPI)
- 🔄 Real-time API communication
- 🎯 Clean and minimal UI
- 🧩 Extensible architecture (ready for OpenAI upgrade)

---

## 🏗️ Tech Stack

### Frontend
- React (Vite)
- JavaScript (ES6+)
- Fetch API
- HTML + CSS

### Backend
- FastAPI
- Python 3.12
- Pydantic
- Uvicorn
- CORS Middleware

---

## 📁 Project Structure
ai-bug-assistant/
│
├── backend/
│ ├── main.py # FastAPI backend logic
│ ├── requirements.txt # Python dependencies
│
├── frontend/
│ ├── src/
│ │ ├── App.jsx # Main React UI
│ │ └── main.jsx
│ ├── package.json
│
└── README.md


---

## ⚙️ How It Works

1. User enters a bug description in the UI
2. React sends request to FastAPI backend (`/solve`)
3. Backend processes input using rule-based AI logic
4. System identifies bug category (React, API, Null error, etc.)
5. Returns structured response:
   - Cause
   - Fix
   - Example
6. UI displays formatted solution

---

## 🔌 API Endpoints

### 🔹 GET `/`

Health check

```json
{
  "message": "AI Bug Assistant is running 🚀"
}

Example Bug Inputs

You can test with:

React state not updating after API call
Null pointer error in Python
API returning 500 error
CORS error between frontend and backend
Database connection failure
🔧 Key Learning Outcomes

This project demonstrates:

Full-stack development (React + FastAPI)
REST API design
State management in React
Backend routing and logic handling
CORS configuration
Rule-based AI system design
Frontend-backend integration
Debugging real-world software issues
🚀 Future Improvements
🔥 Integrate OpenAI / LLM for real AI responses
📊 Add bug history tracking
👤 Add authentication system
💬 Chat-style UI (ChatGPT-like interface)
☁️ Deploy as SaaS product
📈 Add analytics dashboard
👨‍💻 Author

Manasa R

📍 London, UK
💻 Software Engineer
🧠 Python | FastAPI | React | AI Systems
📜 License

This project is open-source and can be used for learning and portfolio purposes.