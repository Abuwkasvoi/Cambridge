from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import  ReplyKeyboardRemove
from keyboards.inline.tillar import tillar
from keyboards.inline.uzb_menu_keyboards import Menuuzb, aboutmenu, kurslarmenu, informatsiya, anketa2, kurslar2, xodimlarmenu, nilufar, dilzoda, menuuzb

from loader import dp

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)


@dp.callback_query_handler(text="Ozbek")
async def menu_select(call: types.CallbackQuery):
    photo = open("photos/cambridge1.jpg", 'rb')
    habar = "<b>Cambridge Learning Centr haqida qisqacha ma'lumot:</b>\n\n"
    habar +="Cambridge Learning Centrda siz ingilis tilini professionallardan o'rganishingiz mumkin.\n"
    habar += "Kurs davomida yuqori malakali ustozlardan maxsus metodika asosida sifatli ta’lim olishingiz mumkun."
    await call.message.answer_photo(photo=photo, caption=habar, reply_markup=Menuuzb)



@dp.callback_query_handler(text="1ortga")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = open("photos/cambridge1.jpg",'rb')
    msg = f"""
    Assalomu alleykum hurmatli <b>{call.message.from_user.username}👨🏻‍💻</b>!\n<b>Cambridge</b>ga.\nXush kelibsiz🤝\n\nHello Dear <b>{call.message.from_user.username}👨🏻‍💻</b>!\nWelcome to <b>Cambridge</b>\n\n<b>Tillni tanlang👇\nSelect language👇</b>
    """
    await call.message.answer_photo(photo=photo,caption=msg,reply_markup=tillar)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Menu")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = open("photos/about.jpg", 'rb')
    await call.message.answer_photo(photo=photo, reply_markup=menuuzb)


@dp.callback_query_handler(text="menuortga")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/cambridge1.jpg",'rb')
    msg = "Salom👋\n<b>Cambridge</b>ga.\nXush kelibsiz🤝\n\n"
    msg += "<b>Cambridge Learning Centr</b>da siz <b>Ingiliz tilini Professionallardan</b> o'rganishingiz mumkin.\n\n"
    msg += "Kurs davomida yuqori malakali ustozlardan mahsus metodika asosida sifatli ta’lim olishingiz mumkin."
    await call.message.answer_photo(photo=photo, caption=msg, reply_markup=Menuuzb)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="about2")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/cambridge1.jpg",'rb')
    msg = "<b> Cambridge Learning Centrida siz ingliz tilini o'rganishingiz mumkin</b>"
    await call.message.answer_photo(photo=photo, caption=msg, reply_markup=aboutmenu)


@dp.callback_query_handler(text="aboutortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    msg = "<b>Menyu:</b>"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=menuuzb)
@dp.callback_query_handler(text="kurslar")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/kurslar.jpg",'rb')
    await call.message.answer_photo(photo=photo,reply_markup=kurslarmenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="kurslarortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    msg = "<b>Menyu:</b>"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=menuuzb)

@dp.callback_query_handler(text="beginer")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/beginner.jpg",'rb')
    msg = "Beginner darajasiga mos tushadigan o'quv resurslari va tushunchalarni o'z ichiga olgan ba'zi mavzularni ko'rib chiqishdi. Bu boshlang'ich o'rganish darajasida turli sohalar uchun mos bo'ladi"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=kurslar2)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="ortga2")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/kurslar.jpg",'rb')
    await call.message.answer_photo(photo=photo,reply_markup=kurslarmenu)


@dp.callback_query_handler(text="elemen")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAOFZ160ezATHKvLHW7Eygtowg2jPVwAAoIHAAJuvKBKLSaLPzpxwgQ2BA"
    msg = "<b>Elementary level o'rganish darajasi haqida so'rasangiz, bu daraja ko'pincha boshlang'ichdan bir qadam oldinga o‘tgan bo‘lib, o‘quvchilar asosiy tushunchalarni o‘zlashtirib, ular bilan oddiy vazifalarni hal qilishni boshlashadi:</b>\n\n"
    await call.message.answer_video(video=video, caption=msg,reply_markup=kurslar2)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="pinter")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAOUZ162ulqJvs8YeOE5RBrryv_5-jwAAnoGAALyMSFIzWj4nLCtfdU2BA"
    msg ="<b>Pre-intermediate daraja — bu boshlang'ichdan bir qadam yuqoriroq bo'lib, o'quvchilar kundalik vazifalarni hal qilishda yanada mustahkamroq va osonroq ishlashadi.</b>\n\n"
    await call.message.answer_video(video=video, caption=msg,reply_markup=kurslar2)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="inter")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAOWZ1630r3l4UYjoNBIQFuRiC2BmdAAApAHAAJqH5FIQRFU3edHbME2BA"
    msg = "<b>Intermediate Level– bu til o‘rganishning uchinchi bosqichi bo‘lib, o‘quvchilar asosiy grammatikani mustahkamlab, murakkab iboralar va ifodalar bilan o‘z fikrlarini erkin va aniq ifodalashni boshlaydilar</b>\n\n"
    await call.message.answer_video(video=video, caption=msg, reply_markup=kurslar2)
    await call.answer(cache_time=60)



@dp.callback_query_handler(text="xodimlar")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=xodimlarmenu)


@dp.callback_query_handler(text="xodimlarortga")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    msg = "<b>Menyu:</b>"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=menuuzb)




@dp.callback_query_handler(text="nilufar")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/cambridge1.jpg",'rb')
    msg = "<b>Ismi-sharifi: </b>\n"
    msg += "Nilufar Xushboqova.\n\n"   
    msg += "<b>Tug'ilgan yili va joyi: \n</b>"
    msg += "8-yanvar 2001-yil;\n"
    msg += "Jizzax viloyati, Jizzax shahri.\n\n"
    msg += "<b>Ta'limi: \n</b>"
    msg += "Toshkent temir yo'l transport kasb-hunar kolleji Buxgalteriya hisobi va audit (2015-2018).\n\n"
    msg += "<b>Ish tajribasi: \n</b>"
    msg += "Cambridge Learning Centr asosiy ustozi.\n"
    msg += "<b>Tillar: \n</b>"
    msg += "O'zbek tili (Ona tili);\n"
    msg += "Ingliz tili (IELTS 8);\n"
    msg += "Arab tili (O'qiy olish)."
    await call.message.answer_photo(photo=photo,caption=msg,reply_markup=nilufar)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="nilufarortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=xodimlarmenu)


@dp.callback_query_handler(text="dilzoda")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/cambridge1.jpg",'rb')
    msg = "<b>Ismi-sharifi: </b>\n"
    msg += "Isroilov Rustamjon.\n\n"   
    msg += "<b>Tug'ilgan yili va joyi: \n</b>"
    msg += "2-dekabr 2002-yil;\n"
    msg += "Farg'ona viloyati, Qo'qon shahri.\n\n"
    msg += "<b>Ish tajribasi: </b>\n"
    msg += "Cambride Learning Centr support ustozi.\n"
    msg += "<b>Tillar: \n</b>"
    msg += "O'zbek tili (Ona tili);\n"
    msg += "Ingliz tili (IELTS 7.5);\n"
    await call.message.answer_photo(photo=photo,caption=msg,reply_markup=dilzoda)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="dilzodaortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=xodimlarmenu)
























































