import uvicorn
import os
import fastapi

from fastapi import FastAPI

from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

from fastapi_discord.exceptions import ClientSessionNotInitialized
from dotenv import load_dotenv 

from dependencies import discord

load_dotenv() 

app = FastAPI(middleware=[Middleware(SessionMiddleware, secret_key=os.getenv("MIDDLE_SECRET"))])



@app.on_event("startup")
async def startup_event():
    await discord.init()



if __name__ == "__main__":
    uvicorn.run("main:app",reload=True,host="127.0.0.1",port=int(os.getenv("PORT",default=8080)))