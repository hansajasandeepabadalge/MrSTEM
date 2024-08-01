from pyrogram import Client, filters, idle
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
import keyboards

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
    message.reply_text(
        "Welcome! 🎓 I'm here to help with your advanced studies.",
        reply_markup = keyboards.welcome
    )

@app.on_message(filters.text & filters.private)
def handle_text(client, message):
    if message.text == "Papers":
        message.reply_text(
            "Please select a subject:",
            reply_markup = keyboards.papers
        )

    elif message.text == "Notes":
        message.reply_text(
            "Please select a subject:",
            reply_markup = keyboards.notes

    elif message.text == "Back":
        start(client, message)

app.run()