from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup 


Menuuzb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌎 Menu", callback_data="Menu"),
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="1ortga"),
        ],
    ],row_width=True
)

menuuzb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📜 About", callback_data="about2"),
            InlineKeyboardButton(text="📊 Kurslar", callback_data="kurslar"),
        ],
        [
            InlineKeyboardButton(text="👨‍💻 Xodimlar", callback_data="xodimlar"),
            InlineKeyboardButton(text="🧾 Vakansiya", callback_data="vakansiya"),
        ],
        [
            InlineKeyboardButton(text="📞 Bog'lanish uchun", url="https://t.me/cambridge_learning_center" ),
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="menuortga"),
        ],
    ],row_width=True
)

aboutmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🎦 Video", url="https://youtube.com/shorts/mL5-sElSJ-w?si=v_EU0aBK_K45oroD"),
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="aboutortga"),
        ],
    ],row_width=True
)

kurslarmenu =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📘 Beginner",callback_data="beginer"),
            InlineKeyboardButton(text="📕 Elementary", callback_data="elemen"),
        ],
        [
            InlineKeyboardButton(text="📙 Pre-Intermediate",callback_data="pinter"),
            InlineKeyboardButton(text="📗 Intermediate",callback_data="inter"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="kurslarortga"),
        ],
    ],row_width=True
)

informatsiya = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="⤴️ Ortga", callback_data='2ortga')
        ]
    ]
)

anketa2 = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="⤴️ Ortga", callback_data='3ortga')
        ]
    ]
)

kurslar2= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✍️ Kurslarga yozilish", callback_data="anketa2"),
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga2"),
        ],
    ],)


xodimlarmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👤 Nilufar Xushboqova", callback_data="nilufar"),
            InlineKeyboardButton(text="👤 Dilzoda Egamqulova", callback_data="dilzoda"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="xodimlarortga"),
        ],
    ],
)

nilufar =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="nilufarortga"),
            InlineKeyboardButton(text="🔗 Link", url="https://t.me/Abuwkasvoi"),
        ],
    ],row_width=True
)

dilzoda = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="dilzodaortga"),
            InlineKeyboardButton(text="🔗 Link",url="https://t.me/Abuwkasvoi"),
        ],
    ],row_width=True
)

























































