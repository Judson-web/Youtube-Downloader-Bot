from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("PRIMER ROOM SERIES UPDATES MOVIES🍿🍿", url="https://t.me/PRIMER_ROOM")],
        [InlineKeyboardButton(
            "🎥Story Time channel Files 🎥", url="https://t.me/storytimeoG")]
    ])
    welcomed = f"𝙃𝙮 <b>{message.from_user.first_name}</b>\n𝙎𝙚𝙚 /help 𝙛𝙤𝙧 𝙢𝙤𝙧𝙚 𝙙𝙚𝙩𝙖𝙞𝙡𝙨."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
