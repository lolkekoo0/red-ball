import telebot
from telebot import types

bot = telebot.TeleBot('6476838653:AAEY_-LWRqUlejU-zMDZbYtz7pkQZw6eo1c')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Как стать автором на Хабре?')
        btn2 = types.KeyboardButton('Правила сайта')
        btn3 = types.KeyboardButton('Советы по оформлению публикации')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота

    elif message.text == 'Привет':
        bot.send_message(message.from_user.id, "Здравствуй", parse_mode='Markdown')
    elif message.text == 'Советы по оформлению публикации':
        bot.send_message(message.from_user.id, '', parse_mode='Markdown')
    elif message.text == 'привет':
        bot.send_message(message.from_user.id, "Здравствуй", parse_mode='Markdown')
    elif message.text == 'Ты жива?':
        bot.send_message(message.from_user.id, "Да", parse_mode='Markdown')
    elif message.text == 'ты жива?':
        bot.send_message(message.from_user.id, "Да", parse_mode='Markdown')
    elif message.text == 'Ты жива':
        bot.send_message(message.from_user.id, "Да", parse_mode='Markdown')
    elif message.text == 'ты жива':
        bot.send_message(message.from_user.id, "Да", parse_mode='Markdown')
    elif message.text == 'Как дела?':
        bot.send_message(message.from_user.id, "Отлично", parse_mode='Markdown')
    elif message.text == 'Как дела':
        bot.send_message(message.from_user.id, "Отлично", parse_mode='Markdown')
    elif message.text == 'как дела?':
        bot.send_message(message.from_user.id, "Отлично", parse_mode='Markdown')
    elif message.text == 'как дела':
        bot.send_message(message.from_user.id, "Отлично", parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть

