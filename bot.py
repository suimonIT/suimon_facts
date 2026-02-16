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
"🚀 Team Rocket has a worse success rate than random SUIMON predictions.",
"⚡ Pikatchu evolved into Suikatchu after migrating to the SUI chain.",
"🚓 Officer Jenny monitors suspicious levels of hopium activity.",
"💊 Nurse Joy recommends touching grass after extreme SUIMON exposure.",
"🌌 Legendary SUIMON reportedly ignore normal probability rules.",
"💎 Diamond hands considered a natural trainer ability.",
"🚓 Officer Joy briefly detained Sgt. Jeff and Van Johnovich for excessive SUIMON enthusiasm.",
"👨‍🍳 Gordon reportedly cooks better than Ramsey after discovering SUIMON.",
"💊 Suikatchu has been through more rehab cycles than Lindsay Lohan.",
"📜 Ancient trainer myths describe a creature matching SUIMON’s energy."
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












































