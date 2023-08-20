from Zaid import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    "💫🥀 𝙷𝙴𝚈 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝙾𝚇𝚈𝙶𝙴𝙽!\n\n✘ 𝙸'm ˹𝕆𝕩𝕪𝕘𝕖𝕟 ꭙ ℂ𝕝𝕠𝕟𝕖˼ 🫧?\n\n‣ 𝙸 𝙲𝙰𝙽 𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙲𝙻𝙾𝙽𝙴 𝙾𝚇𝚈𝙶𝙴𝙽 𝚄𝚂𝙴𝚁𝙱𝙾𝚃.\n\n‣ 2.0 \n\n‣ This specially for Buzzy People's(lazy)\n\n‣ Now /clone {send your PyroGram String Session}"
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton("🥀 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 🥀", url="t.me/PRADHAN474"),
            ],
            [
                InlineKeyboardButton("✨ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗚𝗥𝗢𝗨𝗣 ✨", url="t.me/BWANDARLOK"),
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
        # change this Directory according to your repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="Zaid/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully As {user.first_name} ✅.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
