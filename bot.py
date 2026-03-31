import random
import asyncio
from telegram import Bot
from telegram.constants import ParseMode

# ================= CONFIG =================
BOT_TOKEN = "8307980171:AAEPQxPujHOy0j1WN-bA2RWfq7z_fTKcOes"
CHAT_ID = -1002664937769  

INTERVAL_SECONDS = 5700

# ================= FACTS =================
SUIMON_FACTS = [
"💦 Suiqrtle doesn’t panic — he just lets weak hands drown themselves.",
"🌿 Bausarimon once slapped a promoter so hard he’s still mumbling nonsense.",
"🔥 Suimander’s tail burns brighter every time someone sells and watches it pump after.",
"🥷 Ninja lands kicks harder than a missed stop-loss hurts ego.",
"💊 Nurse Joy doesn’t heal feelings — she just tells you to stop being soft.",
"🚨 Sgt. Jeff said he was on a 'private island mastermind trip' — bro came back acting like he owns the place.",
"👨‍🍳 Gordon raids harder than a SWAT team.",
"📉 Every dip reveals who was loud for attention and who was actually built for it.",
"💎 Diamond hands isn’t a flex — it’s surviving your own bad decisions.",
"🧠 Half the trainers don’t need strategy — they need supervision.",
"⚡ If you lose with SUIMON, that’s a skill issue.",
"🌿 Bausarimon doesn’t absorb sunlight — he absorbs excuses.",
"🔥 Suimander doesn’t fear water — only low testosterone energy.",
"🏆 The real evolution stone is embarrassment.",
"💥 Nira just joined and pushes harder than Escobar in his prime."
]

# ===== BOT =====
bot = Bot(token=BOT_TOKEN)

# ===== FACT QUEUE =====
fact_queue = []

def refill_facts():
    global fact_queue
    fact_queue = SUIMON_FACTS.copy()
    random.shuffle(fact_queue)

async def send_fact():
    global fact_queue

    if not fact_queue:
        refill_facts()

    fact = fact_queue.pop()

    message = f"🧠 <b>SUIMON Fact</b>\n\n{fact}"

    await bot.send_message(
        chat_id=CHAT_ID,
        text=message,
        parse_mode=ParseMode.HTML
    )

async def main():
    refill_facts()
    while True:
        try:
            await send_fact()
        except Exception as e:
            print("Error:", e)
        await asyncio.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    asyncio.run(main())












































