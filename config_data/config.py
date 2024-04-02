import os
import dotenv
import json


if not dotenv.find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    dotenv.load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")  # https://t.me/bk_alihan_tg_bot
ADMIN_LIST = json.loads(os.getenv("ADMIN_LIST"))


