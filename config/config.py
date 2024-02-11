import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

API_ID = int(getenv("API_ID", "29848797"))
API_HASH = getenv("API_HASH", "f83cdcaafe472e3184cecab68baf4570")
BOT_TOKEN = getenv("BOT_TOKEN", "5204315005:AAGUB2q0QafBUwjDPGRAOcruwhUdqyXVlz4")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "30000"))
STRING_SESSION = getenv("STRING_SESSION", "AgHHdN0Ae3NXcJhejs9_Uu8mUdTW4XxAxDHpvPEGjTZdX2ru4s8hTdzRncEABeM0VmTI3I_b3oPwS4jq-EufR-JDT90zO5HGKKvOxrE7drR840RrJnqGsOsMTDjUIof6ig_TCxfbGHSrxn9wC1VTWfNH_CyzErAEhWCdstnrmIin_MTPRMomiRjkEGqdzf0JjeMztDOCXZZyjIuDBr0-ll-m3ELT6EueLXiaISWFhcYQFnLoQEIy0TU5JUVXdlPddf-gmZ-Li9YIE6PwGU2vLAwHClI4CLkqxwF_jd3iiwz6eokc0sVLdcIqyhaVYQF2qyG2JvPCInQdBlOLoacVRIoeJbA_BgAAAAFS9d0uAA")
BOT_USERNAME = getenv("BOT_USERNAME", "R_R8bot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5686811950").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5686811950").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-2123473531")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "A_weaa")
GROUP = getenv("GROUP", "A_weaae")
BOT_NAME = getenv("BOT_NAME", "قصائد تلاميذ المنتقم")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


