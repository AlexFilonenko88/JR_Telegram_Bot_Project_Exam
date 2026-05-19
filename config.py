import os
from dotenv import load_dotenv

load_dotenv()
token_telegram = os.getenv('TOKEN_TG')
token_openai = os.getenv('TOKEN_OPENAI')