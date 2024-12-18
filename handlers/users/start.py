from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.tillar import tillar
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    photo = open("photos/cambridge1.jpg",'rb')
    msg = f"""
    Assalomu alleykum hurmatli <b>{message.from_user.username}👨🏻‍💻</b>!\n<b>Cambridg</b>ga.\nXush kelibsiz🤝\n\nHello Dear <b>{message.from_user.username}👨🏻‍💻</b>!\nWelcome to <b>Cambridge</b>\n\n<b>Tillni tanlang👇\nSelect language👇</b>
    """
    await message.answer_photo(photo=photo, caption=msg, reply_markup=tillar)