from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
@Client.on_message(filters.command("start"))
async def start(c,m):
    btn = InlineKeyboardMarkup([[InlineKeyboardButton("📢 Coderips", url="https://t.me/coderips")]])
    text = f"Hey {m.from_user.mention} 👋\nI'm **Coderips SuperBot** - Better than @iam_yunabot\n\n**All Features:**\n📁 File Store\n🎌 Anime Search\n🤖 AI Chat\n🎴 Waifu Cards\n🛡️ Group Tools\n📥 Downloader\n\nUse /help"
    await m.reply_text(text, reply_markup=btn)
@Client.on_message(filters.command("help"))
async def help(c,m):
    await m.reply_text("Commands:\n/start\n/help\n/store (reply to file)\n/anime naruto\n/ai what is python?\n/guess\n/collection\n/ban (reply)\n/yt <link>")
