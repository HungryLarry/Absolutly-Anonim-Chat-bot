import aiogram
import config as cfg
from aiogram import types
from googletrans import Translator
msges = open('messages.txt', 'a')
transl = Translator()
bot = aiogram.Bot(token=cfg.TOKEN)
dp = aiogram.Dispatcher(bot)
#des = "en"
#chislomsg = 0
bufer = 0
print('bot started')
ids = []
@dp.message_handler()
async def transl_message(msg: types.Message):
    global bufer
    global ids
    if(str(msg.text) == "/start"):
        idsread = open(r'ids.txt', 'r')
        with open(r'ids.txt', 'r') as f:
            for line in f:
                bufer = 1
                break
        idsread.close()
        if bufer == 0:
            ids = open(r'ids.txt', 'a')
            ids.write(str(msg.from_user.id) + '\n')
            ids.close()
    idsread = open(r'ids.txt', 'r')
    for usrid in idsread:
        await bot.send_message(usrid, msg.text)
    idsread.close()
if __name__ == '__main__':
    aiogram.executor.start_polling(dp)

