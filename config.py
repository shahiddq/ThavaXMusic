import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "28435307"))

API_HASH = getenv("API_HASH", "080f5bf6faf2a1656f5719db47eb9c2b")

BOT_TOKEN = getenv("BOT_TOKEN", "6880909457:AAGIMSvHx7GZzwuf-gvVEhYgzIvpdn4Sy78")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ericabraham016:shahiddq12@musicbot.zmtpq.mongodb.net/?retryWrites=true&w=majority&appName=Musicbot")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(getenv("LOGGER_ID", "-1002232962113"))

OWNER_ID = int(getenv("OWNER_ID", "6436690546"))

START_STICKER_ID = getenv("START_STICKER_ID", "CAACAgUAAxkBAAIYJ2XDYrt9C1aT2TMAAVbvhu7GQt4pxQACOg4AAs7jGVZZ_1ODkCxOcx4E")

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝐆𝚯𝗝𝚯 𝖲𝚨𝚻𝚶𝐑𝚶")

POWERED_BY = getenv("POWERED_BY", "˹ 𝐆ᴏᴊᴏ ✘ 𝐌ᴜꜱɪᴄ ˼")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Thava-OX/ThavaXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/musictestttt")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/musictestttt")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", None))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")


PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "300"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))



# Get your pyrogram v2 session from @TBN_StringGeneratorRobot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGx42sAEC2H2gCO7BmVi8ugDDBwZqbMJeSCQAzPsTDDWrrUVNG_Qf7ePrz78XAOoMgBxvx3_ALw8Y0vZezg2BWHFm7Rilfn_R5JIrZ7_TeytliioeOGMzxf9gh-KA9kZz5yufFyR4hiyQYDGKmIpfcvwU0GZtiFFdNBrTc2W4pIXGLD5OPhw3v2oeXh7dA51kZh94LpqtGCSmVMBwR0MWi5ELa3LGkCd513hz68aMfrNyMMZDfRv0jn3R54rEUCrEm1vZh8tp2qJEnXA6PQaeVwr03oi7cceL20pUqd01SA37wU5RkiM-f0Rs1lNFeNKZgRSg3bhByJX1-eDmpYoKbwGrte6AAAAAGR4MmKAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/cfde7fce2fb2c105c7451.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/30577470793677e5408ee.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/7db32a17b15440fa88f91.jpg"
STATS_IMG_URL = "https://telegra.ph/file/02af26494524244cf83d0.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/b00af14042edff8b71f2e.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/9f3720a8d4ec5ae50977f.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
