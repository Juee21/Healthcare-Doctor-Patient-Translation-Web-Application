# Healthcare Doctor–Patient Translation Web Application

A full‑stack web application that acts as a translation bridge between doctors and patients. The system supports text and voice-based interactions, translates conversations into the selected language in near real time, and leverages AI to generate concise medical summaries.

This project was built as a time‑boxed (12‑hour) assignment to demonstrate system design, AI integration, and rapid full‑stack development.

---

## 🚀 Live Demo

* **Frontend (Streamlit UI):** *Add deployed Streamlit link here*
* **Backend (FastAPI):** *Add deployed backend link here*

---

## 🧩 Problem Statement

In healthcare settings, language barriers between doctors and patients can lead to miscommunication and poor outcomes. This application aims to reduce that gap by providing:

* Real‑time translation of doctor–patient conversations
* Support for both text and voice interactions
* AI‑generated summaries highlighting medically important details

---

## ✨ Features

### 1. Real‑Time Doctor–Patient Translation

* Supports two roles: **Doctor** and **Patient**
* Messages typed or spoken by one role are translated into the selected language of the other role
* REST‑based near real‑time translation

### 2. Text Chat Interface

* Simple and intuitive chat-style UI built with Streamlit
* Role selection (Doctor / Patient)
* Translated responses displayed immediately

### 3. Audio Recording & Transcription

* Audio recorded directly from the browser using Streamlit’s microphone input
* Recorded audio is playable in the UI
* Audio is sent to the backend and transcribed using AI (OpenAI Whisper)

### 4. Conversation Logging (Partial)

* Conversation and message schemas designed
* Unique conversation IDs generated per session
* Database integration scaffolded

> Note: Due to time constraints, full persistence of conversation history across sessions is partially implemented at the backend level but not fully wired to the UI.

### 5. Conversation Search (Planned / Partial)

* Backend route structure and schemas prepared for keyword-based search
* Intended to support searching across past conversations with contextual results

> Note: Search functionality is not fully implemented in the current UI but the system architecture supports it.

### 6. AI‑Powered Medical Summary

* Generate a concise summary at any point during or after a conversation

* Designed to highlight medically important information such as:

  * Symptoms
  * Diagnoses
  * Medications
  * Follow‑up actions

* Includes graceful fallback handling if AI API quota limits are reached

---

## 🏗️ Tech Stack

### Frontend

* **Streamlit** – Rapid UI development and browser-based audio recording

### Backend

* **FastAPI** – REST API framework
* **SQLAlchemy** – ORM and database abstraction
* **SQLite** (local development) / PostgreSQL (production-ready)

### AI & ML

* **OpenAI GPT models** – Translation and summarization
* **OpenAI Whisper** – Audio transcription

---

## 🗂️ Project Structure

```
backend/
 ├── app/
 │   ├── main.py
 │   ├── database.py
 │   ├── models.py
 │   ├── schemas.py
 │   ├── ai.py
 │   └── routes/
 │       ├── chat.py
 │       ├── audio.py
 │       ├── search.py
 │       └── summary.py
 ├── requirements.txt
 └── .env

streamlit_app.py
```

---

## ⚙️ Setup & Run Locally

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
streamlit run streamlit_app.py
```

---

## 🔐 Environment Variables

Create a `.env` file in the `backend/` directory:

```env
DATABASE_URL=sqlite:///./health_translation.db
OPENAI_API_KEY=your_openai_api_key
```

---

## 🧠 AI Integration Notes

* OpenAI APIs are used for translation, transcription, and summarization
* If API quota limits are exceeded, the application degrades gracefully without crashing
* Mock / fallback responses are used to ensure uninterrupted demo functionality

---

## ⚠️ Known Limitations & Trade‑offs

* Real‑time communication is REST‑based (no WebSockets)
* Conversation persistence and search are partially implemented
* UI prioritizes functionality over advanced chat styling
* Audio files are handled as temporary storage during development

These trade‑offs were made intentionally to prioritize core functionality within the given time constraints.

---

## 📈 Future Improvements

* Full conversation persistence and retrieval
* Keyword-based search with highlighted context
* Structured medical entity extraction (symptoms, medications, diagnoses)
* WebSocket-based real-time translation
* Role-based chat UI with message bubbles

---

## 📄 License

This project is for evaluation and educational purposes.

---

## 👤 Author

**Juee Khandale**

Full‑stack developer with an interest in AI‑powered healthcare solutions.
