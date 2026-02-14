import random
import asyncio
from telegram import Bot
from telegram.constants import ParseMode

# ================= CONFIG =================
BOT_TOKEN = "8307980171:AAEPQxPujHOy0j1WN-bA2RWfq7z_fTKcOes"
CHAT_ID = -1002664937769  

INTERVAL_SECONDS = 3720

# ================= FACTS =================
SUIMON_FACTS = [
"⚡ After Pikachu inhaled toilet dust, he evolved into Suikatchu.",
"💊 Nurse Joy prescribes touching grass and closing the app.",
"🎤 Drake buys SUIMON because he has a history of liking things early.",
"💂 Sgt. Jeff joined SUIMON to support the war against Team Jeet.",
"🍄 After eating mushrooms with Suikatchu, JDL unlocked a vision where SUIMON hits unimaginable levels.",
"🥷 Ninja silently eliminates Team Jeet members one dip at a time.",
"💰 Ronny’s Pokermon luck classified as a legendary passive ability.",
"🌟 Otex spawned like a legendary SUIMON and instantly boosted the entire squad.",
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









































