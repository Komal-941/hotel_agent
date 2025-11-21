**Hotel Room Service Agent — AI-Powered Backend (FastAPI + Gemini)**

An AI-powered backend service that acts as a hotel room-service assistant using FastAPI, MongoDB, and LLMs (Gemini / Groq / HuggingFace).
The system supports menu browsing, chatting, and structured order processing through REST APIs.

---

## 🏗️ File Structure  
```bash 

hotel-room-service-agent/
│
├── main.py
├── agent.py
├── database.py
├── menu.py
├── requirements.txt
├── .env
│
└── utils/
    ├── prompts.py
    ├── menu_rules.py
    └── __init__.py
```

---
## .env file template 
```
MONGODB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/
DB_NAME= your db_name
LLM_PROVIDER=gemini/groq
GEMINI_API_KEY=your_gemini_key_here
GROQ_API_KEY=your_groq_key_here

```
---
- AI-powered order confirmation (Gemini / Groq )
- Fully dynamic menu from MongoDB
- Order creation, validation & finalization
- Stores order history and active orders
- REST API architecture (no business logic on frontend)
- Environment-based LLM configuration

---
