from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton

welcome = ReplyKeyboardMarkup(
        [
            [KeyboardButton("📄 Papers"), KeyboardButton("📒 Notes")],
            [KeyboardButton("📚 Resources Books")],
            [KeyboardButton("👩‍🏫 Teachers' Guide")],
            [KeyboardButton("🖐 About Us"), KeyboardButton("🌟 Rate Us")]
        ],
        resize_keyboard=True
    )

papers = ReplyKeyboardMarkup(
            [
                [KeyboardButton("📄 Physics")],
                [KeyboardButton("📄 Mathematics"), KeyboardButton("📄 Biology")],
                [KeyboardButton("📄 ICT"), KeyboardButton("📄 Chemistry")],
                [KeyboardButton("📄 Agrricultural Science")],
                [KeyboardButton("🏠 Main Menu")]
            ],
            resize_keyboard=True
        )

papers_type = ReplyKeyboardMarkup(
            [
                [KeyboardButton("Past Papers"), KeyboardButton("Model Papers")],
                [KeyboardButton("Province Papers"), KeyboardButton("Zonal Papers")],
                [KeyboardButton("School Papers"), KeyboardButton("Seminar Papers")],
                [KeyboardButton("👈 Back"), KeyboardButton("🏠 Main Menu")]
            ],
            resize_keyboard=True
        )

notes = ReplyKeyboardMarkup(
            [
                [KeyboardButton("📕 Physics")],
                [KeyboardButton("📗 Biology"), KeyboardButton("📘 Mathematics")],
                [KeyboardButton("📙 ICT"),  KeyboardButton("📓 Chemistry")],
                [KeyboardButton("📒 Agrricultural Science")],
                [KeyboardButton("🏠 Main Menu")]
            ],
            resize_keyboard=True
        )

resources_books = ReplyKeyboardMarkup(
            [
                [KeyboardButton("📚 Physics")],
                [KeyboardButton("📚 Biology"), KeyboardButton("📚 Mathematics")],
                [KeyboardButton("📚 ICT"),  KeyboardButton("📚 Chemistry")],
                [KeyboardButton("📚 Agrricultural Science")],
                [KeyboardButton("🏠 Main Menu")]
            ],
            resize_keyboard=True
        )

teachers_guide = ReplyKeyboardMarkup(
            [
                [KeyboardButton("👩‍🏫 Physics")],
                [KeyboardButton("👩‍🏫 Biology"), KeyboardButton("👩‍🏫 Mathematics")],
                [KeyboardButton("👩‍🏫 ICT"),  KeyboardButton("👩‍🏫 Chemistry")],
                [KeyboardButton("👩‍🏫 Agrricultural Science")],
                [KeyboardButton("🏠 Main Menu")]
            ],
            resize_keyboard=True
        )
years_keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("2023", callback_data="year_2022")],
        [
            InlineKeyboardButton("2022", callback_data="year_2022"),
            InlineKeyboardButton("2021", callback_data="year_2021"),
            InlineKeyboardButton("2020", callback_data="year_2020"),
            InlineKeyboardButton("2019", callback_data="year_2019"),
            InlineKeyboardButton("2018", callback_data="year_2018"),
            InlineKeyboardButton("2005", callback_data="year_2005")
        ]
    ]
)