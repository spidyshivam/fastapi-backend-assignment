from fastapi import FastAPI
from app.routers import user
from app.database.database import init_db
import asyncio

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()

app.include_router(user.router)
