from aiogram import types
from aiogram.types import  ReplyKeyboardRemove
from keyboards.inline.tillar import tillar
from keyboards.inline.eng_menu_keyboards import Menu , menu,menuabout,coursemenu,course1,employeesmenu,nilufar,dilzoda
from loader import dp

@dp.callback_query_handler(text="english")
async def menu_select(call: types.CallbackQuery):
    photo = open("photos/cambridge1.jpg", 'rb')
    habar = "<b>Brief information about Cambridge Learning Centre:</b>\n\n"
    habar +="At Cambridge Learning Center you can learn English from professionals.\n"
    habar += "During the course, you can get high-quality education based on a special methodology from highly qualified teachers."
    await call.message.answer_photo(photo=photo, caption=habar, reply_markup=Menu)



@dp.callback_query_handler(text="1back")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = open("photos/cambridge1.jpg",'rb')
    msg = f"""
    Assalomu alleykum hurmatli <b>{call.message.from_user.username}👨🏻‍💻</b>!\n<b>Cambridge</b>ga.\nXush kelibsiz🤝\n\nHello Dear <b>{call.message.from_user.username}👨🏻‍💻</b>!\nWelcome to <b>Cambridge</b>\n\n<b>Tillni tanlang👇\nSelect language👇</b>
    """
    await call.message.answer_photo(photo=photo,caption=msg,reply_markup=tillar)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Menu2")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = open("photos/about.jpg", 'rb')
    await call.message.answer_photo(photo=photo, reply_markup=menu)


@dp.callback_query_handler(text="menuback")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/cambridge1.jpg",'rb')
    msg = "Hello👋\n<b>Welcome</b>\nto Cambridge🤝\n\n"
    msg += "<b>Cambridge Learning Centr</b>da you <b>can learn Enlish</b> from Professionals.\n\n"
    msg += "During the course, you can get quality education based on a special methodology from highly qualified teachers."
    await call.message.answer_photo(photo=photo, caption=msg, reply_markup=Menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="about")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/cambridge1.jpg",'rb')
    msg = "<b> You can learn English at Cambridge Learning Cente.</b>"
    await call.message.answer_photo(photo=photo, caption=msg, reply_markup=menuabout)


@dp.callback_query_handler(text="aboutback")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    msg = "<b>Menu:</b>"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=menu)
@dp.callback_query_handler(text="course")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/kurslar.jpg",'rb')
    await call.message.answer_photo(photo=photo,reply_markup=coursemenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="courseback")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    msg = "<b>Menyu:</b>"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=menu)

@dp.callback_query_handler(text="begen")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/beginner.jpg",'rb')
    msg = "Some topics covered include learning resources and concepts suitable for the beginner level. It is suitable for various fields at the initial learning level"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=course1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="back2")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/kurslar.jpg",'rb')
    await call.message.answer_photo(photo=photo,reply_markup=coursemenu)


@dp.callback_query_handler(text="elementr")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAOFZ160ezATHKvLHW7Eygtowg2jPVwAAoIHAAJuvKBKLSaLPzpxwgQ2BA"
    msg = "<b>If you're asking about the Elementary level, this level is often a step up from elementary, where students learn basic concepts and begin to solve simple tasks with them:</b>\n\n"
    await call.message.answer_video(video=video, caption=msg,reply_markup=course1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="preinter")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAOUZ162ulqJvs8YeOE5RBrryv_5-jwAAnoGAALyMSFIzWj4nLCtfdU2BA"
    msg ="<b>Pre-intermediate level is a step up from beginner, where students are able to perform everyday tasks with greater consistency and ease..</b>\n\n"
    await call.message.answer_video(video=video, caption=msg,reply_markup=course1)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="interm")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAOWZ1630r3l4UYjoNBIQFuRiC2BmdAAApAHAAJqH5FIQRFU3edHbME2BA"
    msg = "<b>Intermediate Level is the third stage of language learning, where students consolidate basic grammar and begin to express themselves freely and clearly with complex phrases and expressions.</b>\n\n"
    await call.message.answer_video(video=video, caption=msg, reply_markup=course1)
    await call.answer(cache_time=60)



@dp.callback_query_handler(text="employees")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Employees:👇</b>", reply_markup=employeesmenu)


@dp.callback_query_handler(text="employeesback")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    msg = "<b>Menu:</b>"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=menu)




@dp.callback_query_handler(text="nilufara")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/cambridge1.jpg",'rb')
    msg = "<b>Name and Surname </b>\n"
    msg += "Nilufar Xushboqova.\n\n"   
    msg += "<b>Year and place of birth: \n</b>"
    msg += "8-january 2001-year;\n"
    msg += "Jizzakh city, Jizzakh region.\n\n"
    msg += "<b>Work experience: \n</b>"
    msg += "Cambridge Learning Centr main teacher.\n"
    msg += "<b>Language: \n</b>"
    msg += "Uzbek language (Mother tongue);\n"
    msg += "English language (IELTS 8);\n"
    msg += "Arabic language (Being able to read)."
    await call.message.answer_photo(photo=photo,caption=msg,reply_markup=nilufar)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="nilufarback")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Employees:</b>", reply_markup=employeesmenu)


@dp.callback_query_handler(text="dilzodaa")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/cambridge1.jpg",'rb')
    msg = "<b>Name and Surname: </b>\n"
    msg += "Dilzoda Eqamqulova.\n\n"   
    msg += "<b>Year and place of birth: \n</b>"
    msg += "2-december 2002-year;\n"
    msg += "Kokan city, Fergana region.\n\n"
    msg += "<b>Work experience: </b>\n"
    msg += "Cambride Learning Centr support teacher.\n"
    msg += "<b>Language: \n</b>"
    msg += "Uzbek language (Mother tongue);\n"
    msg += "English language (IELTS 7.5);\n"
    await call.message.answer_photo(photo=photo,caption=msg,reply_markup=dilzoda)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="dilzodaback")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Employees:👇</b>", reply_markup=employeesmenu)