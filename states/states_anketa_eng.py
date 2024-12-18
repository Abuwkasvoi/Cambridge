from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalData2(StatesGroup):
    eng_fullname = State()
    eng_phoneNumber = State()