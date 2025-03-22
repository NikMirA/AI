import re
import random
import requests
import webbrowser
from datetime import datetime

API_KEY = "0a20cfd450598adf9dba25bbb99e9839"

def log_dialog(user_input, bot_response):
    with open("chat_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"user: {user_input}\n")
        log_file.write(f"UI: {bot_response}\n")
        log_file.write("-" * 40 + "\n")

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        return f"В городе {city} сейчас {weather_desc} при температуре {temp}°C."
    else:
        return "Не удалось получить информацию о погоде. Попробуйте другой город."

def commands():
    return (
        "Я могу помочь с такими запросами:\n"
        "- приветсвие и простой диалог\n"
        "- Как тебя зовут?\n"
        "- Погода в <город>\n"
        "- Сколько времени?\n"
        "- Какая сегодня дата?\n"
        "- Выполнить арифметические операции, такие как 2 + 2 или 3 * 3.\n"
        "- Для поиска в интернете используйте команду: 'поиск <ваш запрос>'."
    )

def search_web(query):
    url = f"https://www.google.com/search?q={query.replace('', '+')}"
    webbrowser.open(url)
    return f"Открываю результаты поиска для: '{query}'"

responses = {
    r"привет": ["Привет, как я могу помочь?", "Здравствуйте! Чем могу помочь?", "Привет! Как ваши дела?"],
    r"здравс": ["Здравствуйте, как я могу помочь?", "Приветствую! Каков ваш вопрос?"],
    r"как тебя зовут": ["Я бот-помощник!", "Мое имя - Бот. А ваше?"],
    r"как дела": ["Отлично! У вас как дела?", "Все прекрасно! Как вы?"],
    r"хорошо":  ["Я рад за вас!", "Прекрасно слышать!"],
    r"спасибо": ["Всегда пожалуйста!", "Не за что!", "Обращайтесь в любое время!"],
    r"что ты умеешь\??": ["Я умею отвечать на простые вопросы. Попробуйте что-то спросить!",
                          "Я могу помочь с разными запросами. Напишите 'команды', чтобы узнать больше."],
    r"какая погода": "Не знаю, не могу проверить погоду.",
    r"сколько времени": "Сейчас: " + datetime.now().strftime("%H:%M"),
    r"сколько сейчас времени": "Сейчас: " + datetime.now().strftime("%H:%M"),
    r"который час": "Сейчас " + datetime.now().strftime("%H:%M"),
    r"который сейчас час": "Сейчас " + datetime.now().strftime("%H:%M"),
    r"какая дата": "Сегодня " + datetime.now().strftime("%d.%m.%Y"),
    r"какая сегодня дата": "Сегодня " + datetime.now().strftime("%d.%m.%Y"),
    r"команды": commands(),
}

def calculate_expression(expression):
    try:
        result = eval(expression)
        return f"вот ответ: {result}"
    except Exception as e:
        return f"Не удалось выполнить вычисление. {e}"

def chatbot_response(text):
    text = text.lower()
    for pattern, response in responses.items():
        if re.search(r'^\s*\d+\s*[\+\-\*\/]\s*\d+\s*$', text):
            return calculate_expression(text)

        match = re.search(r"поиск\s+(.+)", text, re.IGNORECASE)
        if match:
            return search_web(match.group(1))

        match_weather = re.search(r"погода в (.+)", text, re.IGNORECASE)
        if match_weather:
            return get_weather(match_weather.group(1))

        if re.search(pattern, text):
            if isinstance(response, list):
                return random.choice(response)
            else:
                return response

    return random.choice(["Я не понял вопрос.", "Попробуйте перефразировать", "Не распознал ваш ответ"])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Введите 'выход' для завершения диалога")
    print("Введите 'команды' для обозрения всех возможностей бота")
    while True:
        user_input = input("Вы: ")
        if user_input.lower() == "выход":
            print("Бот: До свидания!")
            break
        bot_response = chatbot_response(user_input)
        print("Бот: ", chatbot_response(user_input))
        log_dialog(user_input, bot_response)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
