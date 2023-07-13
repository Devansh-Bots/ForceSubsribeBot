from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Help Message
@Client.on_message(filters.command("help"))
async def _help(bot, msg):
    await bot.send_message(
        msg.chat.id,
        "**ʜᴇʀᴇ's ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ?**\n" + Data.HELP,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )
