from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup 

tillar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
          InlineKeyboardButton(text="🇺🇿 O'zbek",callback_data="Ozbek"),
          InlineKeyboardButton(text="🇺🇸 English",callback_data="english"),
        ],
    ], row_width=True
)