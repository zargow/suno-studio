from fastapi import FastAPI
from .routers import audio_api

app = FastAPI()

app.include_router(audio_api.router)
