import random
import asyncio
from telegram import Bot
from telegram.constants import ParseMode

# ================= CONFIG =================
BOT_TOKEN = "8307980171:AAEPQxPujHOy0j1WN-bA2RWfq7z_fTKcOes"
CHAT_ID = -1002664937769  

INTERVAL_SECONDS = 5385

# ================= FACTS =================
SUIMON_FACTS = [
    "🌍 Suimon is technically a post-apocalyptic world where animals are already extinct.",
    "⚔️ One by one, Suimon beats every arena on SUI.",
    "⛰ Suiamp can move mountains… yet still needs 4 arms to carry groceries.",
    "🃏 Chad lost his house playing Pokermon, yet he still can’t stop hanging out on PokerNow.",
    "🤵 Chad has been 10 years old for over 25 years. This makes him canonically immortal.",
    "🏕️ Every long route has a rest stop. This is one of them.",
    "⚡ Suikachu refused rehab after repeated attempts. Hopium is a helluva drug.",
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


















