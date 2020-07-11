import logging
import os
import sys
from pymongo import MongoClient
from telethon import TelegramClient
import telegram.ext as tg

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

ENV = bool(os.environ.get('ENV', True))

if ENV:

    try:
        TOKEN = set(int(x) for x in os.environ.get("TOKEN", "").split())
    except ValueError:
        raise Exception("Your sudo users list does not contain valid integers.")

    try:
        OWNER_ID = int(os.environ.get('OWNER_ID', None))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")

    MESSAGE_DUMP = os.environ.get('MESSAGE_DUMP', None)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)

    try:
        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    except ValueError:
        raise Exception("Your sudo users list does not contain valid integers.")

    try:
        SUPPORT_USERS = set(int(x) for x in os.environ.get("SUPPORT_USERS", "").split())
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WHITELIST_USERS = set(int(x) for x in os.environ.get("WHITELIST_USERS", "").split())
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    WEBHOOK = bool(os.environ.get('WEBHOOK', False))
    URL = os.environ.get('URL', "")  # Does not contain token
    API_KEY = os.environ.get("API_KEY", None)
    API_HASH = os.environ.get("API_HASH", None)
    PORT = int(os.environ.get('PORT', 5432))
    CERT_PATH = os.environ.get("CERT_PATH")
    OPENWEATHERMAP_ID = os.environ.get('OPENWEATHERMAP_ID', None)
    DB_URI = os.environ.get('DATABASE_URL')
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    DEL_CMDS = bool(os.environ.get('DEL_CMDS', False))
    STRICT_ANTISPAM = bool(os.environ.get('STRICT_ANTISPAM', True))
    DEEPFRY_TOKEN = os.environ.get('DEEPFRY_TOKEN', "")
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    WORKERS = int(os.environ.get('WORKERS', 8))
    WOLFRAM_ID = os.environ.get('WOLFRAM_ID', None)
    BAN_STICKER = os.environ.get('BAN_STICKER', 'CAACAgUAAxkBAALtC17p4EIAATVENsrWdMiTEinfiUXp3wACDwADTB0uPDaYvTB8iR7eGgQ')
    ALLOW_EXCL = os.environ.get('ALLOW_EXCL', True)
    SUDO_USERS.add(OWNER_ID)
    GBAN_LOGS = os.environ.get('GBAN_LOGS', None)
    tbot = TelegramClient("haruka", API_KEY, API_HASH)
    updater = tg.Updater(TOKEN, workers=WORKERS)
    dispatcher = updater.dispatcher
    SUDO_USERS = list(SUDO_USERS)
    REM_BG_API_KEY = os.environ.get('REM_BG_API_KEY', None)
    WHITELIST_USERS = list(WHITELIST_USERS)
    IBM_WATSON_CRED_URL = os.environ.get('IBM_WATSON_CRED_URL', None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get('IBM_WATSON_CRED_PASSWORD', None)
    SUPPORT_USERS = list(SUPPORT_USERS)
    WALL_API = os.environ.get('WALL_API', None)
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)
    CASH_API_KEY = os.environ.get('CASH_API_KEY', None)
    TIME_API_KEY = os.environ.get('TIME_API_KEY', None)
    # Load at end to ensure all prev variables have been set
    from haruka.modules.helper_funcs.handlers import CustomCommandHandler, CustomRegexHandler, GbanLockHandler
    # make sure the regex handler can take extra kwargs
    tg.RegexHandler = CustomRegexHandler

    if ALLOW_EXCL:
       tg.CommandHandler = CustomCommandHandler
    tg.CommandHandler = GbanLockHandler
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)   
    TEMPORARY_DATA = os.environ.get('TEMPORARY_DATA', None)
    SPAMMERS = os.environ.get('SPAMMERS', "")
    SPAMMERS = list(SPAMMERS)

    try:
      from haruka.antispam import antispam_restrict_user, antispam_cek_user, detect_user
      antispam_module = True
    except ModuleNotFoundError:
      antispam_module = False
      
    def spamfilters(text, user_id, chat_id, message):
        if user_id == 1372161900:
           return False
        print("{} | {} | {} | {}".format(text, user_id, message.chat.title, chat_id))
        if antispam_module:
           parsing_date = time.mktime(message.date.timetuple())
           detecting = detect_user(user_id, chat_id, message, parsing_date)
           if detecting:
              return True
           antispam_restrict_user(user_id, parsing_date)
        if int(user_id) in SPAMMERS:
           print("This user is spammer!")
           return True
        else:
           return False
else:
   quit(1)
