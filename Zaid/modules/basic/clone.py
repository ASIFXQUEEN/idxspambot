import os
from pyrogram import Client, filters, Message

OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", "404 : Bio Lost")

@Client.on_message(filters.command("clone", ".") & filters.me)
async def clone(_, message: Message):
    text = message.text.split(" ", 1)[1]
    op = await message.edit_text("`Cloning`")
    userk = (await get_user(message, text))[0]
    user_ = await _.get_users(userk)
    
    if not user_:
        await op.edit("`Whom i should clone:(`")
        return
    
    get_bio = await _.get_chat(user_.id)
    f_name = user_.first_name
    c_bio = get_bio.bio
    pic = user_.photo.big_file_id
    poto = await _.download_media(pic)
    
    await _.set_profile_photo(photo=poto)
    await _.update_profile(
        first_name=f_name,
        bio=c_bio,
    )
    await message.edit(f"**From now I'm** __{f_name}__")

@Client.on_message(filters.command("revert", ".") & filters.me)
async def revert(_, message: Message):
    await message.edit("`Reverting`")
    r_bio = BIO

    await _.update_profile(
        first_name=OWNER,
        bio=r_bio,
    )
    
    photos = await _.get_profile_photos("me")
    if len(photos) > 0:
        await _.delete_profile_photos(photos[0].file_id)
    
    await message.edit("`I am back!`")

# Assuming you have a function 'add_command_help' that you've imported from somewhere
add_command_help(
    "clone",
    [
        ["clone", "To Clone someone Profile."],
        ["revert", "To Get Your Account Back."],
    ],
)
