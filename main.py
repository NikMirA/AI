import re
import random
from datetime import datetime

def commands():
    return (
        "Я могу помочь с такими запросами:\n"
        "- приветсвие и простой диалог\n"
        "- Как тебя зовут?\n"
        "- Какая погода?\n"
        "- Сколько времени?\n"
        "- Какая сегодня дата?\n"
        "- Выполнить арифметические операции, такие как 2 + 2 или 3 * 3.\n"
    )

responses = {
    r"привет": "Привет, как я могу помочь?",
    r"здравс": "Здравствуйте, как я могу помочь?",
    r"как тебя зовут": "Я бот-помощник!",
    r"как дела": "Отлично! У вас как дела?",
    r"хорошо": "Я рад за вас!",
    r"спасибо": "Всегда пожалуйста!",
    r"что ты умеешь\??": "Я умею отвечать на простые вопросы. Попробуй спросить: 'Как тебя зовут?' или напиши 'команды'",
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

        if re.search(pattern, text):
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
        print("Бот: ", chatbot_response(user_input))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
