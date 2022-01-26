# Divyesh Vaghela // @ZaYNxOP 
from pyrogram import Client, filters
from modules.helpers.filters import command, other_filters
from modules.helpers.command import commandpro
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton




@Client.on_message(commandpro([ "/alive", "divyesh"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a8b04a83d5bc163370042.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "I'ᴍ Aʟɪᴠᴇ", url=f"https://t.me/Voicechatmusicsbot?startgroup=true")
                ]
            ]
        ),
    )

@Client.on_message(commandpro(["@ZaYNxOP","#creator","#owner"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/92bba3375827ea52df036.mp4",
        caption=f"Mʏ Mᴀsᴛᴇʀ🙂",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓆩 乙Λϒᮘ 𓆪‌‌‌‌ ✘⁪⁬⁮⁮⁮⁮ ⪨ ᎧᎮܔ ⪩ ›➤", url=f"https://t.me/ZaYNxOP")
                ]
            ]
        ),
    )


