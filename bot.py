from pyrogram import Client 
from os import getenv
from dotenv import load_dotenv


load_dotenv()


bot = Client(
    "bot",
    api_id=getenv("TG_API_ID"),
    api_hash=getenv("TG_API_HASH"),
    bot_token=getenv("TG_BOT_TOKEN"),
    workdir="data"
)
