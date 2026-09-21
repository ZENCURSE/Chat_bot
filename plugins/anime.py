from pyrogram import Client, filters
import requests
@Client.on_message(filters.command("anime"))
async def anime(c,m):
    if len(m.command)<2: return await m.reply("Usage: /anime <name>")
    q = " ".join(m.command[1:])
    query = '''query ($s: String){Media(search:$s, type:ANIME){title{romaji english} description averageScore episodes coverImage{large} siteUrl}}'''
    r = requests.post("https://graphql.anilist.co", json={"query":query,"variables":{"s":q}}).json()
    media = r.get("data",{}).get("Media")
    if not media: return await m.reply("Not found")
    txt = f"**{media['title']['romaji']}**\nScore: {media['averageScore']}\nEpisodes: {media['episodes']}\n{media['description'][:400]}...\n{media['siteUrl']}"
    await m.reply_photo(media["coverImage"]["large"], caption=txt)
