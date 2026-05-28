import aiohttp
import config


async def get_weather(city: str | None):
    if not city:
        return "Вы не ввели город ❌"

    TOKEN_OPENWEATHER = config.token_openweather
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city.strip(),
        "appid": TOKEN_OPENWEATHER,
        "units": "metric",
        "lang": "ru"
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as resp:
                data = await resp.json()

                # ❗ проверяем API-ошибку
                if resp.status != 200 or str(data.get("cod")) != "200":
                    return f"Ошибка: {data.get('message', 'неизвестно')} ❌"

                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                wind = data["wind"]["speed"]

                return f"🌡 {temp}°C\n☁️ {desc}\n💨 Ветер: {wind} м/с"

    except aiohttp.ClientError:
        return "Ошибка соединения 🌐"
    except Exception as e:
        return f"Ошибка: {e}"
