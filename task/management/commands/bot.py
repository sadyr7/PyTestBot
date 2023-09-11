from django.core.management.base import BaseCommand
from task.models import Task_Backend, Task_Frontend
from telebot import TeleBot, types

bot = TeleBot('6435207550:AAEZglHbN6cVmhuYi1hyoOBsHGf1mvN2Re8', threaded=False)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()


@bot.message_handler(commands=['start'])
def start_message(message):

    keyboard = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('BackEnd')
    button2 = types.KeyboardButton('Frontend')
    keyboard.add(button1, button2)

    message2 = bot.send_message(
        message.chat.id,
        'Привет, это PyTestBot!🚀\n\nМоя задача - сделать управление задачами легким и визуальным.🔰\n Я буду отправлять тебе картинки с задачами,\n чтобы ты всегда был в курсе текущих задач по фронтенду и бэкенду.Давай начнем совместную работу!',
        reply_markup=keyboard
    )


@bot.message_handler(func=lambda x: x.text in ['BackEnd'])
def task_backend(message):
    keyboard = types.ReplyKeyboardMarkup()
    button3 = types.KeyboardButton('Таски Backend')
    button4 = types.KeyboardButton('Назад')
    keyboard.add(button3, button4)

    message3 = bot.send_message(message.chat.id, 'Начинаем BackEnd задачи', reply_markup=keyboard)

current_task_Backend_id = 1

@bot.message_handler(func=lambda x: x.text in ['Таски Backend'])
def task_backend_next(message, *args, **kwargs):
    global current_task_Backend_id
    try:
        current_task = Task_Backend.objects.get(id=current_task_Backend_id)
    except Task_Backend.DoesNotExist:
        bot.send_message(message.chat.id, "BackEnd задачи закончились")
        return

    current_task_Backend_id += 1

    with open(current_task.image.path, 'rb') as image_file:
        bot.send_photo(message.chat.id, image_file)

@bot.message_handler(func=lambda x: x.text in ['Frontend'])
def task_frontend(message):
    keyboard = types.ReplyKeyboardMarkup()
    button5 = types.KeyboardButton('Таски Frontend')
    button6 = types.KeyboardButton('Назад')
    keyboard.add(button5, button6)

    message3 = bot.send_message(message.chat.id, 'Начинаем Frontend задачи', reply_markup=keyboard)

current_tasks_Frontend_id = 1

@bot.message_handler(func=lambda x: x.text in ['Таски Frontend'])
def task_frontend_next(message, *args, **kwargs):
    global current_tasks_Frontend_id
    try:
        current_tasks = Task_Frontend.objects.get(id=current_tasks_Frontend_id)
    except Task_Frontend.DoesNotExist:
        bot.send_message(message.chat.id, "Frontend задачи закончились")
        return

    current_tasks_Frontend_id += 1

    with open(current_tasks.image.path, 'rb') as image_file:
        bot.send_photo(message.chat.id, image_file)


@bot.message_handler(func=lambda x: x.text == 'Назад')
def go_back(message):
    keyboard = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('BackEnd')
    button2 = types.KeyboardButton('Frontend')
    keyboard.add(button1, button2)

    bot.send_message(
        message.chat.id,
        'Вы вернулись в главное меню.',
        reply_markup=keyboard
    )


bot.polling()