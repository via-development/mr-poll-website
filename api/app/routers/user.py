from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from fastapi_discord import DiscordOAuthClient, RateLimited, Unauthorized, User

from ..dependencies import discord

router = APIRouter()

@router.get('/users/me',dependencies=[Depends(discord.requires_authorization)],response_model=User)
async def users(user: User = Depends(discord.user)):
    try:
        return user
    except:
        return JSONResponse({"success": False},401)