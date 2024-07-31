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

@app.on_message(filters.text & filters.private)
async def welcome(client, message):
    user_id = message.from_user.id
    if message.text.lower() == "hi":
        buttons = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Button 1", callback_data="button1")],
                [InlineKeyboardButton("Button 2", callback_data="button2")]
            ]
        )
        await message.reply("Welcome! How can I assist you today?", reply_markup=buttons)
    else:
        await message.reply(f"{message.text} (User ID: {user_id})")

@app.on_callback_query()
async def handle_callback_query(client, callback_query):
    data = callback_query.data
    if data == "button1":
        await callback_query.message.edit_text("You pressed Button 1")
    elif data == "button2":
        await callback_query.message.edit_text("You pressed Button 2")

async def send_direct_message():
    target_user_id = 6131532789
    await app.send_message(target_user_id, "Hello! This is a direct message.")

async def main():
    await app.start()
    await send_direct_message()
    await idle()
    await app.stop()

app.run(main())