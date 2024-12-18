

from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext

from loader import dp
from states.states_anketa_eng import PersonalData2
from keyboards.inline.eng_menu_keyboards import  menu, anketa

@dp.callback_query_handler(text="anketa")
async def enter_text(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Enter your full name")
    await PersonalData2.eng_fullname.set()

@dp.message_handler(state=PersonalData2.eng_fullname)
async def answer_soha(message: Message, state: FSMContext):

    fullname = message.text
    await state.update_data(
        {
            'name': fullname
        }
    )

    await message.answer("Enter your phone number:")
    await PersonalData2.next()

@dp.message_handler(state=PersonalData2.eng_phoneNumber)
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
        The following information has been received.\n
        Our operators will be in touch soon\n\n\n
        <b>first name last name</b>: {fullname}\n
        <b>Your phone number</b>: {phone}
    """

    
    await message.answer(msg, reply_markup=anketa)
    await state.finish()


@dp.callback_query_handler(text="3back")
async def cancel_buying(call: CallbackQuery):
    await call.message.delete()
    photo = open("photos/cambridge1.jpg", "rb")
    habar = "<b>Brief information about Cambridge Learning Centre:</b>\n\n"
    habar += "At Cambridge Learning Center you can learn English from professionals.\n"
    habar += "During the course, you can get quality education based on a special methodology from highly qualified teachers."
    await call.message.answer_photo(photo=photo, caption=habar, reply_markup=menu)