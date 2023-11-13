import requests
import telebot
from telebot import types

token = "6928739947:AAELEtzDlO1CUoimKbyZ9DH-XyUelx9m7LU"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_dice(message.chat.id)
    bot.send_message(
        message.chat.id,
        (
            f"Привет {message.from_user.first_name} {message.from_user.last_name},я первая версия бота!\n"
            f"Помощь /help\n"
            f"Погода /weather\n"
        ),
    )


@bot.message_handler(commands=["weather"])
def select_city(message):
    bot.send_message(message.chat.id, "Введите название города")


@bot.message_handler(commands=["help"])
def help_troll(message):
    keyboard = types.InlineKeyboardMarkup()
    url_help = types.InlineKeyboardButton(text="Документация", url="https://google.com")
    keyboard.add(url_help)
    bot.send_message(message.chat.id, "Читай документацию", reply_markup=keyboard)
    file = open("./1.png", "rb")
    bot.send_photo(message.chat.id, file)


@bot.message_handler(content_types=["text"])
def get_weather(message):
    city = message.text
    url = (
        "https://api.openweathermap.org/data/2.5/weather?q="
        + city
        + "&units=metric&lang=ru&appid=da7d4e595c06a6726c97a3cedc54a70a"
    )
    res = requests.get(url).json()

    cur_temp = round(res["main"]["temp"])
    wind = round(res["wind"]["speed"])
    w_now = "Сейчас в городе " + city + " " + str(cur_temp) + " °C"
    wind_speed = "Скорость ветра" + " " + str(wind)
    bot.send_message(message.chat.id, w_now)
    bot.send_message(message.chat.id, wind_speed)


# data=json.loads(res.text)
# bot.reply_to(message,f'Сейчас погода:{data["temp"]}')
# @bot.message_handler()
# ef talk(message):
# if message.text.lower()=='Привет':
#   bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
# elif message.text.lower()=='Как дела?':
# bot.send_message(message.chat.id, 'Все хорошо!')
# if message.text.lower()==message:
# bot.send_message(message.chat.id, 'Я не смогу вам ответить на это сообщения, но я только первая версия и еще выучусь!!!')


# @bot.message_handler(content_types=['text'])
# def repeat_all_messages(message):
#   bot.send_message(message.chat.id,message.text)


if __name__ == "__main__":
    bot.infinity_polling()
