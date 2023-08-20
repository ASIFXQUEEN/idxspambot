from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from Zaid import API_ID, API_HASH, ALIVE_PIC

PHONE_NUMBER_TEXT = (
    "💫🥀 𝙷𝙴𝚈 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝙾𝚇𝚈𝙶𝙴𝙽!\n\n"
    "✘ 𝙸'm ˹𝕆𝕩𝕪𝕘𝕖𝕟 ꭙ ℂ𝕝𝕠𝕟𝕖˼ 🫧?\n\n"
    "‣ 𝙸 𝙲𝙰𝙽 𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙲𝙻𝙾𝙽𝙴 𝙾𝚇𝚈𝙶𝙴𝙽 𝚄𝚂𝙴𝚁𝙱𝙾𝚃.\n\n"
    "‣ 2.0 \n\n‣ This specially for Buzzy People's (lazy)\n\n"
    "‣ Now /clone {send your PyroGram String Session}"
)

app = Client(
    "Melody",
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="Zaid/modules")
)

@app.on_message(filters.command("start"))
async def hello(client: Client, message: Message):
    buttons = [
        [InlineKeyboardButton("🥀 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 🥀", url="t.me/PRADHAN474")],
        [InlineKeyboardButton("✨ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗚𝗥𝗢𝗨𝗣 ✨", url="t.me/BWANDARLOK")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

@app.on_message(filters.command("clone"))
async def clone(client: Client, message: Message):
    text = await message.reply("Usage:\n\n /clone session_string")
    cmd = message.command
    if len(cmd) >= 2:
        session_string = cmd[1]
        try:
            await text.edit("Booting Your Client")
            with app as clone_client:
                await clone_client.start()
                user = await clone_client.get_me()
                await message.reply(f"Your Client Has Been Successfully As {user.first_name} ✅.")
        except Exception as e:
            await message.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")

app.run()
