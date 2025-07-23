import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")
VECTOR_PATH = "vector_store"
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")