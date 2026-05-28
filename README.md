🤖 Telegram Bot

Telegram-бот содержит 6 проектов:
 - Рандомный факт
 - ChatGPT интерфейс
 - Диалог с известной личностью
 - Квиз
 - Переводчик
 - Погода


🛠 Технологии используемые в проекте

Python 3.13
aiogram 3
aiohttp
API (OpenWeather, OpenAI)


📂 Структура проекта

bot/
│── handlers/        # обработчики команд
│── images/          # изоражения
│── keyboards/       # клавиатуры
│── services/        # работа с API
│── utils/           # вспомогательные функции
│── config.py        # настройки
│── proxy.py         # прокси
│── main.py          # запуск бота


⚙️ Установка и запуск

1. Клонировать репозиторий
git clone https://github.com/AlexFilonenko88/JR_Telegram_Bot_Project_Exam.git
cd your_project
2. Создать виртуальное окружение
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
source .venv/Scripts/activate  # Windows
3. Установить зависимости
pip install -r requirements.txt
4. Создать .env файл
TOKEN_TG=your_telegram_token
TOKEN_OPENAI=your_openai_token
TOKEN_OPENWEATHER=your_openweather_token
5. Запуск бота
python main.py


Примеры команд

|- /start - запуск бота
|- /random - запусе рандомного факта
|- /weather - узнать погоду
|- /quiz - запустить квиза
|- /talk - диалог с известной личностью
|- /translator - переводчик
|- /gpt - запуск gpt interface


👤 Автор

Alex F
GitHub: https://github.com/AlexFilonenko88/JR_Telegram_Bot_Project_Exam.git


Ссылка

@Jr_Pyvenom_tg_eaxm_project_bot
