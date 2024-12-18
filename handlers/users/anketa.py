

from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext

from loader import dp
from states.states_anketa_uz import PersonalData1
from keyboards.inline.uzb_menu_keyboards import  menuuzb, anketa2

@dp.callback_query_handler(text="anketa2")
async def enter_text(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("To'liq ismingizni kiriting")
    await PersonalData1.fullname.set()

@dp.message_handler(state=PersonalData1.fullname)
async def answer_soha(message: Message, state: FSMContext):

    fullname = message.text
    await state.update_data(
        {
            'name': fullname
        }
    )

    await message.answer("Telefon raqamingizni kiriting:")
    await PersonalData1.next()

@dp.message_handler(state=PersonalData1.phoneNumber)
async def answer_phone(message: Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {
            'telefon_nomer': phone
        }
    )
    
    data = await state.get_data()
    fullname = data.get('name')
    phone = data.get('telefon_nomer')

    msg = f"""
        Quyidagi ma'lumotlar qabul qilindi.\n
        Tez orada operatorlarimiz bog'lanadi.\n\n\n
        <b>ism familiya sharifi</b>: {fullname}\n
        <b>Telefon raqamingiz</b>: {phone}
    """

    
    await message.answer(msg, reply_markup=anketa2)
    await state.finish()


@dp.callback_query_handler(text="3ortga")
async def cancel_buying(call: CallbackQuery):
    await call.message.delete()
    photo = open("photos/cambridge1.jpg", "rb")
    habar = "<b>Cambridge Learning Centr haqida qisqacha ma'lumot:</b>\n\n"
    habar += "Cambridge Learning Centrda siz ingilis tilini professionallardan o'rganishingiz mumkin..\n"
    habar += "Kurs davomida yuqori malakali ustozlardan maxsus metodika asosida sifatli ta’lim olishingiz mumkun."
    await call.message.answer_photo(photo=photo, caption=habar, reply_markup=menuuzb)