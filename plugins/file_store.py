from pyrogram import Client, filters
from config import OWNER_ID, LOG_CHANNEL
@Client.on_message(filters.command("store") & filters.user(OWNER_ID))
async def store(c,m):
    if not m.reply_to_message:
        return await m.reply_text("Reply to a file to store")
    msg = await m.reply_to_message.copy(LOG_CHANNEL)
    link = f"https://t.me/{c.me.username}?start=file_{msg.id}"
    await m.reply_text(f"✅ Stored!\n\nLink: {link}")
@Client.on_message(filters.private & filters.command("start"))
async def get_file(c,m):
    if len(m.command)>1 and "file_" in m.command[1]:
        fid = int(m.command[1].split("_")[1])
        try:
            await c.copy_message(m.chat.id, LOG_CHANNEL, fid)
        except:
            await m.reply_text("File not found / deleted")
