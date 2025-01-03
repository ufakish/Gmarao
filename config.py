import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "18499702"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001902619247"))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5050578106"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/DarkAarush/LU",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://www.jiosaavn.com/")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://www.jiosaavn.com/")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-AviaxMusic-08-14")


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("BQEvjOkAMobugvO1U6ctFgqJj7nAN_QF7fAxmhvEdY0LwswKt9qp2k3agdVtQ0UHoYttRM5HrFkHnZPqKPFNoCsPpn6wWP5D_9JflEQv5rA0VGKthEGcuYlesVT6GuPivwvLqPfcJSNkDOzcFPZYtskCISw947E5GoKebTO_3Aoa8vDL7oVRqxj98WzgsTBT4l627JFQ_EU9ZnLLhd4gK-_168OetyeMdqAr-qT6bxLMN-IDIXiSrktVHg8t-UAD523RxYrT7SbMmI32NoOEh5rRK-BOYcq9S1WoqbHlpxKdvKiig2pTqsuwp5ls6dCLcYYSXmBerPsCeSdRlKPtAltxSArmJQAAAAHMx7MCAA",)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/CwU.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/CLg.jpeg"
)
PLAYLIST_IMG_URL = "https://envs.sh/CLg.jpeg"
STATS_IMG_URL = "https://envs.sh/CLg.jpeg"
TELEGRAM_AUDIO_URL = "https://envs.sh/CLg.jpeg"
TELEGRAM_VIDEO_URL = "https://envs.sh/CLg.jpeg"
STREAM_IMG_URL = "https://envs.sh/CLg.jpeg"
SOUNCLOUD_IMG_URL = "https://envs.sh/1mX.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/CLg.jpeg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/CLg.jpeg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/CLg.jpeg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/CLg.jpeg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 800**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

