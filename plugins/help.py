from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Bro/Sis Currently Only supports Youtube Single Vedio Link Within A Time So Just Send Youtube Vedio/Song Url (No playlist)"
    await message.reply_text(helptxt)
