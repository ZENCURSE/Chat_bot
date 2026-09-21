from pyrogram import Client, filters
@Client.on_message(filters.command("ban") & filters.group)
async def ban(c,m):
    if m.reply_to_message:
        await c.ban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
        await m.reply("Banned ✅")
@Client.on_message(filters.command("unban") & filters.group)
async def unban(c,m):
    if m.reply_to_message:
        await c.unban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
        await m.reply("Unbanned ✅")
@Client.on_message(filters.command("purge") & filters.group)
async def purge(c,m):
    if not m.reply_to_message: return
    msgs = []
    async for msg in c.get_chat_history(m.chat.id, offset_id=m.reply_to_message.id, reverse=True):
        msgs.append(msg.id)
        if len(msgs)>100: break
    await c.delete_messages(m.chat.id, msgs)
    await m.reply(f"Purged {len(msgs)}")
