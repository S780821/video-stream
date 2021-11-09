import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Xmartperson")
ALIVE_NAME = getenv("ALIVE_NAME", "Xmarty")
BOT_USERNAME = getenv("BOT_USERNAME", "Xmarty_vc_player_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "cleo_invida")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Xmarty_Support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "welcomefriendclub")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/bf3d5334efaa345955275.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c1b0b567c6db19da5080e.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/bf3d5334efaa345955275.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/bf3d5334efaa345955275.jpg")
