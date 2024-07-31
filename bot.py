from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api_id = 11965840
api_hash = "716c845bdc09adf2b6db0b63e4a455"
bot_token = "6998765478:AAF-bWsygAmJQpUKSCgINRhs7wOAeYG9fiQ"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

@app.on_message(filters.command("start"))
def start(client, message):
    # Define the keyboard layout with more buttons
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

app.run()