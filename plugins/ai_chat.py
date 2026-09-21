from pyrogram import Client, filters
from config import OPENAI_KEY
import requests
@Client.on_message(filters.command("ai"))
async def ai(c,m):
    if len(m.command)<2: return await m.reply("Ask: /ai <question>")
    prompt = " ".join(m.command[1:])
    # Gemini free API
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={OPENAI_KEY}"
        data = {"contents":[{"parts":[{"text":prompt}]}]}
        res = requests.post(url, json=data).json()
        ans = res["candidates"][0]["content"]["parts"][0]["text"]
        await m.reply(ans[:4000])
    except Exception as e:
        await m.reply(f"Add GEMINI API key in config. Error: {e}")
