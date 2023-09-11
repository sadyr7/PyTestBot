from django.core.management.base import BaseCommand
from product import models
from product.models import CartItem
from project import settings
from telebot import TeleBot, types
import requests
import wikipedia

bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)



class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()


@bot.message_handler(commands=['start'])
def start_message(message):
    message2 = bot.send_message(message.chat.id,'выбери', reply_markup=keyboard)



keyboard = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('оплата')
button2 = types.KeyboardButton('ингредиент')
keyboard.add(button1, button2)

@bot.message_handler(func=lambda x: x.text in ['оплата'])
def oplata(message):
    #work = str(CartItem.objects.all())
    message3 = bot.send_message(message.chat.id, 'Выберите корзину пользователя', reply_markup=keyboard)
    bot.register_next_step_handler(message3, oplata1, oplata2, oplata3, oplata4)

    @bot.message_handler(commands=['rm'])
    async def process_rm_command(message: types.Message):
        await message.reply("Убираем шаблоны сообщений", reply_markup=bot.ReplyKeyboardRemove())

#keyboard = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('корзина1')
button2 = types.KeyboardButton('корзина2')
button3 = types.KeyboardButton('корзина3')
button4 = types.KeyboardButton('корзина4')
keyboard.add(button1, button2, button3, button4)

@bot.message_handler(func=lambda x: x.text in ['корзина1'])
def oplata1(message, *args, **kwargs):
    work = str(CartItem.objects.get(id=1))
    message3 = bot.send_message(message.chat.id, work, reply_markup=keyboard)
    #bot.register_next_step_handler(message3, work)

@bot.message_handler(func=lambda x: x.text in ['корзина2'])
def oplata2(message):
    work = (CartItem.objects.get(id=36))
    message3 = bot.send_message(message.chat.id, work, reply_markup=keyboard)


@bot.message_handler(func=lambda x: x.text in ['корзина3'])
def oplata3(message):
    work = (CartItem.objects.get(id=34))
    message3 = bot.send_message(message.chat.id, work, reply_markup=keyboard)



@bot.message_handler(func=lambda x: x.text in ['корзина4'])
def oplata4(message):
    work = (CartItem.objects.get(id=35))
    message3 = bot.send_message(message.chat.id, work, reply_markup=keyboard)


wikipedia.set_lang('ru')


def handle(self, *args, **kwargs):
    bot.enable_save_next_step_handlers(delay=2)
    bot.load_next_step_handlers()
    bot.infinity_polling()

def getwiki(s):
    try:
        wikitext = wikipedia.page(s).content[:500] # срезаем инфо до 500 символов
        wikitext = wikitext.split('.')
        wikitext = ''.join(wikitext[:-1]) + '.' # убераем последнее не законченое преложение и вставляем точку
        return wikitext
    except Exception as e:
        return 'такого нету'


# декоратор обрабатываем сообщения изера
@bot.message_handler(func=lambda x: x.text in ['ингредиент'])
def start_message(message):
    message2 = bot.send_message(message.chat.id,'отправь мне любое слово и я найду его значение в wikipedia')
    bot.register_next_step_handler(message2, handle_text)


def handle_text(message):
    word = message.text
    info = getwiki(word)
    message2 = bot.send_message(message.chat.id,info, reply_markup=keyboard)
    bot.register_next_step_handler(message2,info,word)


bot.polling()