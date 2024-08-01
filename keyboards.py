from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

welcome = ReplyKeyboardMarkup(
        [
            [KeyboardButton("Papers"), KeyboardButton("Notes")],
            [KeyboardButton("Resources Books"), KeyboardButton("Teachers' Guide")],
            [KeyboardButton("About Us")]
        ],
        resize_keyboard=True  # Optional: make the keyboard smaller
    )

papers = ReplyKeyboardMarkup(
            [
                [KeyboardButton("Physics"), KeyboardButton("Mathematics")],
                [KeyboardButton("Biology"), KeyboardButton("Chemistry")],
                [KeyboardButton("ICT"), KeyboardButton("Agrricultural Science")],
                [KeyboardButton("Back")]
            ],
            resize_keyboard=True  # Optional: make the keyboard smaller
        )

notes = ReplyKeyboardMarkup(
            [
                [KeyboardButton("Physics"), KeyboardButton("Mathematics")],
                [KeyboardButton("Biology"), KeyboardButton("Chemistry")],
                [KeyboardButton("ICT"), KeyboardButton("Agrricultural Science")],
                [KeyboardButton("Back")]
            ],
            resize_keyboard=True
        )