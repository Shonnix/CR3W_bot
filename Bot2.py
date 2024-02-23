# Импорт для кнопки в закрепе
# import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo




bot = Bot(token='6929043221:AAF4_UHEuuW5ngoyosRWe1UNIoL6jG-0AjM', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)





@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://htmlpreview.github.io/?https://github.com/Shonnix/CR3W_bot/blob/main/main.html')))
    await message.answer('Hello', reply_markup=markup)







# Этот весь код для кнопки ебаной в закрепе
chat_id = -1002114518298

    

# Этот код нужен был для того, чтобы понять логику кнопки(/knopka)
# async def send_message(channel_id: int, text: str):
#     await bot.send_message(channel_id, text)


# async def main():
#     await send_message(chat_id, '<b>Hello!</b>')
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Сделать заказ', url='https://t.me/cr3ww_bot/cr3w'))
#     await message.reply('Hello', reply_markup= markup)


# Это рабочий код для кнопки в закрепе
# функция с кнопкой будет вызываться по команде /knopka и только админом(мной)
@dp.message_handler(commands=['knopka'])
async def main(message: types.Message):
    markup1= types.InlineKeyboardMarkup()
    markup1.add(types.InlineKeyboardButton('Открыть магазин', url='https://t.me/cr3ww_bot/cr3w'))
    if message.chat.id == 1086529883:
        await bot.send_message(chat_id, "Иди нахуй!", reply_markup=markup1)
    else:
        None

# по сути это нахуй не надо
# if __name__ == '__main__':
#     asyncio.run(main())



executor.start_polling(dp)