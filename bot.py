import random
import asyncio
from telegram import Bot
from telegram.constants import ParseMode

# ================= CONFIG =================
BOT_TOKEN = "8307980171:AAEPQxPujHOy0j1WN-bA2RWfq7z_fTKcOes"
CHAT_ID = -1002664937769  

INTERVAL_SECONDS = 4000

# ================= FACTS =================
SUIMON_FACTS = [
    "🎒 Suimon trainers always say just one more arena and disappear for six hours.",
    "🚨 Just in: Suikachu escaped rehab again. Hopium is flooding the land. The Suimon Authority has declared a national emergency.",
    "📘 The Suidex lists overconfidence as a common trainer debuff.",
    "🏟️ Arena leaders respect only one thing. Consistency."
    "🧪 Mixing hopium and impatience causes instant confusion.",
    "🐢 Suimon moves slow so trainers can keep up.",
    "🔍 The rarest Suimon ability is ignoring noise.",
    "🎨 Picasso lost an ear after someone asked him to draw a Suimon meme for Fan Art Friday."
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


























