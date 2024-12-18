from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



Menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌎 Menu", callback_data="Menu2"),
            InlineKeyboardButton(text="⬅ Back", callback_data="1back"),
        ],
    ],row_width=True
)



menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📜 About", callback_data="about"),
            InlineKeyboardButton(text="📊 Course", callback_data="course"),
        ],
        [
            InlineKeyboardButton(text="👨‍💻 Employees", callback_data="employees"),
            InlineKeyboardButton(text="🧾 Vacancy", callback_data="vacancy"),
        ],
        [
            InlineKeyboardButton(text="📞 Сontact us", url="https://t.me/cambridge_learning_center" ),
        ],
        [
            InlineKeyboardButton(text="⬅️ Back", callback_data="menuback"),
        ],
    ],row_width=True
)




menuabout = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🎦 Video", url="https://youtube.com/shorts/mL5-sElSJ-w?si=v_EU0aBK_K45oroD"),
        InlineKeyboardButton(text="⬅️ Back", callback_data="aboutback"),
    ],
])

coursemenu =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📘 Beginner",callback_data="begen"),
            InlineKeyboardButton(text="📕 Elementary", callback_data="elementr"),
        ],
        [
            InlineKeyboardButton(text="📙 Pre-Intermediate",callback_data="preinter"),
            InlineKeyboardButton(text="📗 Intermediate",callback_data="interm"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Back", callback_data="courseback"),
        ],
    ],row_width=True
)



info = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="⤴️ Back", callback_data='2back')
        ]
    ]
)


anketa = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="⤴️ Back", callback_data='3back')
        ]
    ]
)


course1= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✍️ Registration for courses", callback_data="anketa"),
            InlineKeyboardButton(text="⬅️ Back", callback_data="back2"),
        ],
    ],)

employeesmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👤 Nilufar Xushboqova", callback_data="nilufara"),
            InlineKeyboardButton(text="👤 Dilzoda Egamqulova", callback_data="dilzodaa"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Back", callback_data="employeesback"),
        ],
    ],
)

nilufar =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Back", callback_data="nilufarback"),
            InlineKeyboardButton(text="🔗 Link", url="https://t.me/Abuwkasvoi"),
        ],
    ],row_width=True
)


dilzoda = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Back", callback_data="dilzodaback"),
            InlineKeyboardButton(text="🔗 Link",url="https://t.me/Abuwkasvoi"),
        ],
    ],row_width=True
)
