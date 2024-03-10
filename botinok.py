import telebot
import threading
import time

# Задаем токен вашего бота
TOKEN = '6888834841:AAEcCzCds56nhcIRSu8gFiepgJeaj4yqI04'

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)

# Функция для отправки сообщения в чат
def send_message():
    chat_id = '-1001641309643'  # Укажите ID чата, куда бот будет отправлять сообщение
    message = "Андрей пидр"
    bot.send_message(chat_id, message)

# Функция для выполнения отправки сообщения каждую минуту
def send_message_periodically():
    while True:
        send_message()
        time.sleep(60)  # Подождать 60 секунд перед следующим запуском

# Запускаем функцию отправки сообщения в отдельном потоке
thread = threading.Thread(target=send_message_periodically)
thread.start()

# Запускаем бота
bot.polling(none_stop=True)
