from aiogram.dispatcher.filters.state import StatesGroup, State


class eng_personalData(StatesGroup):
    eng_qaysi_sohaga = State()
    eng_fullname = State()
    eng_resume = State()
    eng_phoneNumber = State()