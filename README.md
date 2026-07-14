Markdown
# Unified AI Hub 🚀

A full-stack, state-managed AI assistant powered by FastAPI and Google's Gemini 3.5 Flash. 

This project is custom-tuned via a backend System Prompt to act as a **Mechanical Engineering Copilot**, specializing in thermodynamics, fluid mechanics, materials science, and CAD automation via Python.

## ✨ Features

* **Custom System Prompt:** Engine tuned specifically for Mechanical Engineering logic, formulas, and terminology.
* **Stateful Conversational Memory:** The FastAPI backend maintains an active chat session, allowing the AI to remember context across multiple messages.
* **Memory Wipe Mechanism:** Full-stack integration allowing users to clear the active chat session instantly.
* **Modern Asynchronous Backend:** Built with FastAPI for lightning-fast, non-blocking API endpoints.
* **Responsive Glassmorphism UI:** Built completely in vanilla HTML/JS and styled dynamically with Tailwind CSS.

## 🛠️ Tech Stack

* **Frontend:** HTML5, Vanilla JavaScript, Tailwind CSS (via CDN), FontAwesome
* **Backend:** Python, FastAPI, Uvicorn (ASGI server)
* **AI Engine:** Google GenAI SDK (`gemini-3.5-flash`)

## 🚀 Getting Started

### 1. Clone the repository
bash
git clone https://github.com/prinson2006-bot/unified-ai-hub.git
cd unified-ai-hub


### 2. Install dependencies
Ensure you have Python installed, then run:
bash
pip install fastapi uvicorn google-genai pydantic


### 3. Set up environment variables
Create a `.env` file in the root directory and add your Google Gemini API key:
env
GEMINI_API_KEY=your_api_key_here


### 4. Run the local server
Start the FastAPI backend:
bash
uvicorn app.main:app --reload

The API will now be running on `http://127.0.0.1:8000`.

### 5. Launch the UI
Simply double-click the `index.html` file to open it in your web browser. The frontend will automatically connect to your local Python server.

## ⚙️ Architecture Notes
* **CORS Configuration:** The backend is configured to accept requests from any local origin during development.
* **Global State:** Chat sessions are currently stored in-memory on the server.