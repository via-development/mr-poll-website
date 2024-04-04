from fastapi_discord import DiscordOAuthClient

from dotenv import load_dotenv 
load_dotenv() 


discord = DiscordOAuthClient(
   "ID",
   "Token",  # auth app coming soon.
   "Redirect",
   ("identify",)
)
