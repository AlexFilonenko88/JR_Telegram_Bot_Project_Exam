import aiohttp
import config

async def get_weather(city: str | None):
    TOKEN_OPENWEATHER = config.token_openweather
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": TOKEN_OPENWEATHER,
        "units": "metric",
        "lang": "ru"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            data = await resp.json()

            if resp.status != 200:
                return f"Ошибка: {data.get('message')}"

            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            wind = data["wind"]["speed"]

            print(data)

            # return f"🌡 {temp}°C\n☁️ {desc}\n💨 Ветер: {wind} м/с"