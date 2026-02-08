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
"🎒 Suimon trainers say just one more arena and wake up in a different timezone.",
"🧬 The SUI ecosystem feels less like finance and more like a very serious game engine.",
"🚓 Officer Jenny joined SUIMON because even arrests finalize instantly.",
"🩺 Nurse Joy recommends hydration, rest, and not reading Move docs at 3am.",
"🎮 Suimon tested SUI and asked why other chains feel turn-based.",
"🧠 Extended time on SUI causes irreversible onchain thinking.",
"🧪 Reading SUI dev threads late at night creates unnatural confidence.",
"🚨🚓 BREAKING: Unauthorized Suiballs detected on testnet.",
"🎭 Suimon teaches emotional control through repeated exposure.",
"🧬 SUI developers accidentally built something Suimon would actually respect.",
"🎲 Every Suimon arena doubles as a mental endurance test.",
"🌫️ Trainers report strange clarity after disconnecting from everything except SUI.",
"🔐 Suimon trust SUI because objects behave like objects.",
"🩺 Nurse Joy confirmed trainers suffer from chronic onchain brain.",
"🌀 Reality feels slightly optional after deep dives into SUI architecture.",
"🏟️ The final arena unlocks when trainers stop asking wen.",
"🧠 SUI feels like a blockchain designed by people who played too many games.",
"🚓 Officer Jenny closed the case after realizing everything was working as intended.",
"🧬 Suimon exists where nostalgia meets technical overengineering."
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






































