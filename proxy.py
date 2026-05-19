from aiogram.filters import Command
from aiogram.client.session.aiohttp import AiohttpSession

def proxy():
    session = AiohttpSession(proxy="socks5://127.0.0.1:11000")
    return session