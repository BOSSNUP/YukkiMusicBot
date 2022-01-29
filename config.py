from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN", "2133280461:AAGVomt0sqwz-J6R1MRneAhc6E9JLAH8gWw")
API_ID = int(getenv("API_ID", " 12553697"))
API_HASH = getenv("API_HASH", "ddbd36c19c379ce3e23eaf3a29a02ba7")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "610"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ZAID:ZAID@cluster0.c4wtt.mongodb.net/ZAID?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5046520072").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "1600454750").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001156708921"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "KingXlBot")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/NotReallyShikhar/YukkiMusicBot"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "BOSSNUP")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Hindi_English_Chatting_Group")


STRING1 = getenv("STRING_SESSION1", "BABkt9uN2mfqOU4i3sfl98MmIcU9xMps4xGgJbBBAq0gH0GdN3I8_W-onLLediaq8GPlyZmOUnEICxzTORKV1iptaLnAZhuHjshYy4I6OQyhIxXQCdFX80w84nCAc5Q-khaYvznkb7itE0XXhVd3bnE0JJBZQSLJF5MAtb9X-hZdFO4zDGKQMkVkySF6gEME-3p9u0g0xLP20EpAMBRuWYfM_Do4oGKWMwVEZv37m1c2fVdX2LV9HDmYjqKv4RxJqH5VM8bH2SEN_cuFYTTV6kuTP7dDfbABh38CoNhMPXqSnHf0s8pO55A5h7FBdB6wCIHZsD9gCbbsvoRCCU6IZ7RNf0swIAA")

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
