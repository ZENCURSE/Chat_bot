from pyrogram import Client, filters
import random, pymongo, config
client = pymongo.MongoClient(config.MONGO_URL)
db = client["coderips_bot"]
chars = db["characters"]
users = db["users"]
@Client.on_message(filters.group & ~filters.me)
async def spawn(c,m):
    if random.randint(1,100) == 1: # 1% spawn chance
        char = list(chars.aggregate([{"$sample":{"size":1}}]))
        if char:
            ch = char[0]
            await m.reply_photo(ch["img"], caption=f"A wild waifu appeared! {ch['rarity']}\nGuess with /guess {ch['name'][:2]}...")
@Client.on_message(filters.command("guess"))
async def guess(c,m): await m.reply("Waifu guess system - add MongoDB logic here (see waifu-catcher repo)")
@Client.on_message(filters.command("collection"))
async def coll(c,m): await m.reply("Your collection")
