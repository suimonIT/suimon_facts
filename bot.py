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
    "🐢 Some Suimon are not slow. They are training endurance.",
    "🌍 Suimon is technically a post-apocalyptic world where animals are already extinct.",
    "🚽 No one has ever seen a Suimon use the bathroom, yet the world has plumbing. Think about that.",
    "📈 If a Suimon stares at a chart long enough, the chart moves out of fear.",
    "🥚 Suimon eggs hatch faster when the price goes up.",
    "⚡ Suikachu refused rehab after repeated attempts. Hopium is a helluva drug.",
    "💀 The Jengarcide will be studied for years to come.",
    "🐋 Whalemon can move markets by sneezing."
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















