import os
API_ID = int(os.environ.get("API_ID", 12345))
API_HASH = os.environ.get("API_HASH", "your_api_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "bot_token")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://...")
OWNER_ID = int(os.environ.get("OWNER_ID", 0))
OPENAI_KEY = os.environ.get("OPENAI_KEY", "")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100123456))
