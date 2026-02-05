from fastapi import FastAPI
from app.routes import chat, audio, search, summary

app = FastAPI(title="Healthcare Translation API")

app.include_router(chat.router)
app.include_router(audio.router)
app.include_router(search.router)
app.include_router(summary.router)
