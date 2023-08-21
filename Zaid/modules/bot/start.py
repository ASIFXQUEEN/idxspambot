from Zaid import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    "✘ Heya!\n\n✘ I'm Your Assistant?\n\n‣ I can help you to host Your Left Clients.\n\n‣ Repo: github.com/Itz-Zaid/Zaid-Userbot \n\n‣ This is specially for Buzzy People (lazy)\n\n‣ Now /clone {send your PyroGram String Session}"
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
        [
            InlineKeyboardButton("✘ Updates Channel", url="t.me/TheUpdatesChannel"),
        ],
        [
            InlineKeyboardButton("✘ Support Group", url="t.me/TheSupportChat"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("Booting Your Client")
        # Change this directory according to your repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="Zaid/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully As {user.first_name} ✅.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
