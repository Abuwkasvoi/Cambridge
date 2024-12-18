from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
# from utils.notify_admins import comment


from loader import dp
from states.states_vacancy import eng_personalData
from keyboards.inline.eng_menu_keyboards import  menu, info

@dp.callback_query_handler(text="vacancy")    
async def enter_text(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("In which direction you want to work:")
    await eng_personalData.eng_qaysi_sohaga.set()

@dp.message_handler(state=eng_personalData.eng_qaysi_sohaga)
async def answer_soha(message: Message, state: FSMContext):
    soha = message.text

    await state.update_data(
        {
            'soha tanlandi': soha
        }
    )
    await message.answer("Enter your full name:")
    await eng_personalData.eng_fullname.set()

@dp.message_handler(state=eng_personalData.eng_fullname)
async def answer_fullname(message: Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {
            'F.I.O': fullname
        }
    )
    await message.answer("Submit your resume to:")
    await eng_personalData.next()

@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=eng_personalData.eng_resume)
async def answer_resume(message: Message, state: FSMContext):
    resume = message.document

    await state.update_data(
        {
            'resume': resume.file_name
        }
    )
    await message.answer("Send your phone number:")
    await eng_personalData.next()

@dp.message_handler(state=eng_personalData.eng_phoneNumber)
async def answer_phone(message: Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {
            'telefon nomer': phone
        }
    )
    
    data = await state.get_data()
    soha = data.get('soha tanlandi')
    fullname = data.get('F.I.O')
    resume = data.get('resume')
    phone = data.get('telefon nomer')




    msg = (
        "The following information has been received.\n"
        "Our operators will be in touch soon.\n\n\n"
        f"<b>The direction you submitted</b>: {soha}\n"
        f"<b>first name last name</b>: {fullname}\n"
        f"<b>Your resume</b>: {resume}\n"
        f"<b>Your phone number</b>: {phone}"
    )

    
    # await comment(msg)

    
    # await state.reset_state(with_data=False)
    await message.answer(msg, reply_markup=info)
    await state.finish()

@dp.callback_query_handler(text="2back")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    await call.message.answer_photo(photo=photo, reply_markup=menu)