from pyrogram import Client, filters, idle
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

api_id = 11965840
api_hash = "716c845bdc09adf2b6db0b63e4a455"
bot_token = "6998765478:AAF-bWsygAmJQpUKSCgINRhs7wOAeYG9fiQ"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.command("start"))
def start(client, message):
    # Define the initial keyboard layout with more buttons
    keyboard = ReplyKeyboardMarkup(
        [
            [KeyboardButton("Papers"), KeyboardButton("Notes")],
            [KeyboardButton("Resources Books"), KeyboardButton("Teachers' Guide")],
            [KeyboardButton("About Us")]
        ],
        resize_keyboard=True  # Optional: make the keyboard smaller
    )
    
    # Send the welcome message with the keyboard
    message.reply_text(
        "Welcome! 🎓 I'm here to help with your advanced studies.",
        reply_markup=keyboard
    )

@app.on_message(filters.text & filters.private)
def handle_text(client, message):
    if message.text == "Papers":
        # Define the keyboard layout for subjects
        papers_keyboard = ReplyKeyboardMarkup(
            [
                [KeyboardButton("Physics"), KeyboardButton("Mathematics")],
                [KeyboardButton("Biology"), KeyboardButton("Chemistry")],
                [KeyboardButton("ICT"), KeyboardButton("Agrricultural Science")],
                [KeyboardButton("Back")]
            ],
            resize_keyboard=True  # Optional: make the keyboard smaller
        )
        
        # Send the message with the new keyboard
        message.reply_text(
            "Please select a subject:",
            reply_markup=papers_keyboard
        )
    elif message.text == "Back":
        start(client, message)

app.run()