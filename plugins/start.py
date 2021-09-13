from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("PRIMER ROOM SERIES UPDATES MOVIES🍿🍿", url="https://t.me/PRIMER_ROOM")],
        [InlineKeyboardButton(
            "🎥Story Time channel Files 🎥", url="https://t.me/storytimeoG")]
    ])
    welcomed = f"Hy <b>{message.from_user.first_name}</b>\nI Can Download YouTube Videos By Link, Send Me A Link To See That Magic. Hit /help for get an idea.Join @PRIMER_ROOM"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
