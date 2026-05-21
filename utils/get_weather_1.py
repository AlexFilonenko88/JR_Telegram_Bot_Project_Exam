import aiohttp
import config


async def get_weather_1(city: str | None):
    if not city:
        return "Вы не ввели город ❌"

    TOKEN_WEATHERAPI = config.token_weatherapi
    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": TOKEN_WEATHERAPI,
        "q": city.strip(),
        "lang": "ru"
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as resp:
                data = await resp.json()

                # ❗ проверка ошибок API
                if resp.status != 200 or "error" in data:
                    return f"Ошибка: {data.get('error', {}).get('message', 'неизвестно')} ❌"

                location = data["location"]["name"]
                country = data["location"]["country"]

                current = data["current"]

                temp = current["temp_c"]
                feels = current["feelslike_c"]
                desc = current["condition"]["text"]
                wind = current["wind_kph"]  # км/ч
                humidity = current["humidity"]

                return (
                    f"🌍 {location}, {country}\n\n"
                    f"🌡 {temp}°C (ощущается {feels}°C)\n"
                    f"☁️ {desc}\n"
                    f"💨 Ветер: {wind} км/ч\n"
                    f"💧 Влажность: {humidity}%"
                )

    except aiohttp.ClientError:
        return "Ошибка соединения 🌐"
    except Exception as e:
        return f"Ошибка: {e}"