import yaml
from pyrogram import Client, filters, idle
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
import keyboards

# Load configuration from config.yaml
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

api_id = config['api']['id']
api_hash = config['api']['hash']
bot_token = config['api']['bot_token']

app = Client(
    config['bot']['name'],
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

user_states = {}

@app.on_message(filters.command("start"))
def start(client, message):
    user_id = message.from_user.id
    user_states[user_id] = "home_menu"
    print(user_states)
    message.reply_text(
        config['messages']['welcome'],
        reply_markup = keyboards.welcome
    )

@app.on_message(filters.text & filters.private)
def handle_text(client, message):
    user_id = message.from_user.id
    user_state = user_states.get(user_id, "home_menu")
    
    if user_state == "home_menu":
        if message.text == "📄 Papers":
            user_states[user_id] = "papers_menu"
            print(user_states)
            message.reply_text(
                config['messages']['papers_prompt'],
                reply_markup = keyboards.papers
            )
    elif user_state == "papers_menu":
        if message.text == "📄 Physics":
            user_states[user_id] = "physics_papers_menu"
            print(user_states)
            message.reply_text(
                "Select a type of paper:",
                reply_markup = keyboards.papers_type
            )
    elif user_state == "physics_papers_menu":
        if message.text == "Past Papers":
            message.reply_text(
                "Select a type of paper:",
                reply_markup = keyboards.years_keyboard
            )
        elif message.text == "👈 Back":
            user_states[user_id] = "papers_menu"
            print(user_states)
    elif message.text == "📒 Notes":
        message.reply_text(
            "Select a subject:",
            reply_markup = keyboards.notes
        )
    elif message.text == "📚 Resources Books":
        message.reply_text(
            "Select a subject:",
            reply_markup = keyboards.resources_books
        )
    elif message.text == "👩‍🏫 Teachers' Guide":
        message.reply_text(
            "Select a subject:",
            reply_markup = keyboards.teachers_guide
        )
    elif message.text == "🏠 Main Menu":
        start(client, message)

app.run()