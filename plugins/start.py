from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("PRIMER ROOM SERIES UPDATES MOVIES🍿🍿", url="https://t.me/PRIMER_ROOM")],
        [InlineKeyboardButton(
            "😇Add Me To Your Group😇", url="https://t.me/storytimeoG%22)]
    ])
    welcomed = f"Hy <b>{message.from_user.first_name}</b>\n💁🏻‍♂️ How To Use Me? Just Send Me Any YouTube Video Link To Download The Video (Hit /help for more details)!                                           Made With ❤️ By @PRIMER_ROOM🔥"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
