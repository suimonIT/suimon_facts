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
    "♣️Pokermon 5pm EST♣️ Trainer don't forget to register! https://www.pokernow.com/mtt/pokermon-2426-21tf98IWa7",
    "♣️Pokermon 5pm EST♣️Forgot our Pokermon Night today? Don't worry register now: https://www.pokernow.com/mtt/pokermon-2426-21tf98IWa7",
    "😌🚬 Chad lost his house at a Pokermon table and never left PokerNow.",
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



























