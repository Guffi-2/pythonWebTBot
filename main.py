from telebot import types
import telebot

bot = telebot.TeleBot('7177297829:AAFlOmNwqGPoLYRE2MksqTcTPVMY7MNQEzs')

def webAppKeyboard(): #создание клавиатуры с webapp кнопкой
   keyboard = types.ReplyKeyboardMarkup(row_width=1) #создаем клавиатуру
   webAppPin = types.WebAppInfo("https://pinterest.com") #создаем webappinfo - формат хранения url
   webAppYa = types.WebAppInfo("https://ya.ru")
   webAppTik = types.WebAppInfo("https://tiktok.com")
   one_butt = types.KeyboardButton(text="📌pinterest", web_app=webAppPin) #создаем кнопку типа webapp
   sec_btn = types.KeyboardButton(text='🔍yandex', web_app=webAppYa)
   thee_btn = types.KeyboardButton(text='🎵tiktok', web_app=webAppTik)
   keyboard.add(one_butt, sec_btn, thee_btn) #добавляем кнопки в клавиатуру
   print('pon ')
   return keyboard #возвращаем клавиатуру

@bot.message_handler(commands=['start']) #обрабатываем команду старт
def start_fun(message):
   bot.send_message( message.chat.id, 'Привет', parse_mode="Markdown", reply_markup=webAppKeyboard()) #отправляем сообщение с нужной клавиатурой

if __name__ == '__main__':
   print("bot is online")
   bot.infinity_polling()
