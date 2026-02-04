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
    "🥚 Suimon eggs don’t hatch by time — they hatch by belief.",
    "🃏 Legendary trainers have lost battles, gyms, and fortunes — but never their Suimon.",
    "🧠 Suimon only reaches its final form once you stop checking the price every five minutes.",
    "🐉 Dragons fear Suimon not for its power, but for its holder count.",
    "🔥 Some say Team Rocket never returned because they tried to short Suimon.",
    "💎 Suimon doesn’t ask if you hold — it already knows.",
    "🐋 When a Whalemon moves, the market notices. When Suimon moves, history does.",
    "🧿 Every Suimon journey begins as a meme and ends as lore."
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






















