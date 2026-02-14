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
"🚀 Team Rocket committed more career crimes than most Netflix documentaries.",    
"🚓 Officer Jenny investigating suspicious levels of hopium.",
"🌫️ Second-hand hopium exposure linked to extreme price targets.",
"💊 Nurse Joy prescribes touching grass and closing the app.",
"💊 Nurse Joy warns that hopium is not a substitute for risk management.",
"🎬 Leonardo DiCaprio buys SUIMON because it’s still early.",
"💔 Taylor Swift left SUIMON just to write a song about it.",    
"🎤 Drake buys SUIMON because he also has a history of liking things early.",
"🎭 Team Rocket has a higher failure rate than day-one traders.",    
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








































