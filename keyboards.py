from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

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