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
"🧬 SUIMON trainers claim their portfolios evolved purely out of instinct.",
"🚀 Some investors insist SUIMON found them, not the other way around.",
"📊 DiCaprio’s interest in SUIMON reportedly triggered by its early age.",
"⚡ After Pikachu inhaled toilet dust, he evolved into Suikatchu.",
"🕶️ Rumor says Van Johnovich is just John Wick operating under a cover identity.",
"🌌 JDL took a DMT trip with Suikatchu and witnessed SUIMON’s legendary future.",
"🎤 Drake buys SUIMON because he has a history of liking things early.",
"🎰 Ronny wins weekly Pokermon with suspicious consistency.",
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











































