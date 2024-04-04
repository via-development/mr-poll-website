from fastapi import APIRouter 
from fastapi.responses import JSONResponse

from ..dependencies import discord

router = APIRouter()

@router.get('/auth/login')
async def authentication():
    return JSONResponse({"url":discord.oauth_login_url},200)

@router.get("/auth/callback")
async def callback(code:str):
    try:
        token, refresh_token = await discord.get_access_token(code)
        return JSONResponse({"success": True, "token": token}, 200)
    except:
        return JSONResponse({"success": False},400)
