import telebot;
import settings;
from telebot import types
import requst

bot = telebot.TeleBot(settings.telegram_token);


@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Start massage")
  button_message(message)
  print(message.chat.id)

@bot.message_handler(commands=['button'])
def button_message(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    note = types.KeyboardButton("Записная книжка")
    money_manager = types.KeyboardButton('Менеджмент расходов')
    search_note = types.KeyboardButton('поиск записки')
    markup.add(note,money_manager,search_note)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
    print('button')

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Записная книжка":
        requst.create_new_index(message.chat.id)
        bot.send_message(message.chat.id,"Вы выбрали записную книжку, напишите вашу заметку")
        requst.add_note(message.chat.id,'Я вчера кушал крутые яблоки')
        button_message(message)
    elif message.text=='поиск записки':
        bot.send_message(message.chat.id, requst.search_note(message.chat.id,'яблоки'))




bot.infinity_polling()