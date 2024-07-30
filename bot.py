from pyrogram import Client, filters
from pyrogram import Client, emoji, filters

api_id = 11965840
api_hash = "716c845bdc09adf2b6d36b0b63e4a455"
bot_token = "6998765478:AAF-bWsygAmJQpUKSCgINRhs7wOAeYG9fiQ"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)
@app.on_message(filters.text & filters.private)
async def welcome(client, message):
    if message.text.lower() == "hi":
        await message.reply("Welcome! How can I assist you today?")

app.run()
