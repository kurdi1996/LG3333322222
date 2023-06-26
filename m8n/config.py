# Created By @xl444
# Copyright By watan

from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgDD5utUrSySVXPprK34eJtNwOU0esAd0Cv0IIYZqc2BT5kLNidCdlSyuu1evaK156FAMxthqVGHboQeFrOK2uVAOM7AahXVhKkZKercNCVCvMTue_w2pzZnineSnMCXMiijWMLwxqBdJBstlmxpqfSh8aWZMneslWy_LevnD87mKTgxa3ERmKeYiKpdL7W5GEDPZ54toj6KySY8Dya-1_qEI7AMnCfHy7My7TCwRgDgeAdIH-5ULYpDoRPdhVvFVZehvZ2aMAVnyCg7an9mmvohyL6tBk3nr5-Oo5kbgHQBPJUHo0oA0FelmehzU-EZR-OHZcvBOwUGYqCqGvq5mZ1oAAAAAWAPW_kA")
BOT_TOKEN = getenv("BOT_TOKEN", "6007715792:AAE1Iqa-UdREmuqbFqHe08p8E2TfV9uVdcE")
BOT_NAME = getenv("BOT_NAME", "bot")
BOT_USERNAME = getenv("BOT_USERNAME", "Saiadjabot")
ASSID = int(getenv("ASSID", "5941688740"))
ASSNAME = getenv("ASSNAME", "Kasijekg")
ASSUSERNAME = getenv("ASSUSERNAME", "Kasijekg")

BOT_ID = int(getenv("BOT_ID", "6007715792"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/LG")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
API_ID = int(getenv("API_ID", "28746916"))
API_HASH = getenv("API_HASH", "5f4eb51a1208fa6631fb8a5f3e225f17")
OWNER_ID = int(getenv("OWNER_ID", "6174915391"))
UPDATE = getenv("UPDATE", "TM_412")
SUPPORT = getenv("SUPPORT", "TM_412")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "999"))
CMD_MUSIC = list(getenv("CMD_MUSIC", ". / ! + - @ # $").split())
BG_IMG = getenv("BG_IMG", "https://graph.org/file/04d0acb87765c2cde5e89.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6174915391").split()))
START_PIC = getenv("START_PIC", "https://graph.org/file/04d0acb87765c2cde5e89.jpg")
OWNER_USERNAME = getenv("OWNER_USERNAME", "rr8r9")
IMG_1 = getenv("IMG_1", "https://graph.org/file/475127193de2444183fd4.jpg")
IMG_2 = getenv("IMG_2", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")
IMG_3 = getenv("IMG_3", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")
IMG_4 = getenv("IMG_4", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")
