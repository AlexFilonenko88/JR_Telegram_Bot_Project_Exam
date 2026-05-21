import os
from dotenv import load_dotenv

load_dotenv()

token_telegram = os.getenv('TOKEN_TG')
token_openai = os.getenv('TOKEN_OPENAI')
token_openweather = os.getenv('TOKEN_OPENWEATHER')
token_weatherapi = os.getenv('TOKEN_WEATHERAPI')