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
    "🎒 Suimon trainers say just one more arena and accidentally time travel six hours into the future.",
    "📘 The Suidex lists overconfidence as a passive debuff with a 99% uptime.",
    "🏟️ Arena leaders respect only one thing: consistency. And sometimes memes.",
    "🚨🚓 BREAKING: Trainers have summoned Adeniyi for not bringing Pokémon to SUI yet. Investigation ongoing."
    "🛠️ SUI engineers accidentally created a chain fast enough for real-time SUIMON battles.",
    "👮‍♂️ Authorities remind trainers: catching SUIMON off-chain is still illegal in SUI canon.",
    "🎲 Suimon rewards patience and punishes overthinking equally.",
    "🧬 SUI dev meetings reportedly start with one question: would SUIMON approve this?",
    "🧪 SUIMON tested SUI and asked why other chains are still loading.",
    "💊 Side effects of holding Suimon may include euphoria, delayed sleep, and saying trust the process unironically.",
    "🎮 Suimon is inspired by childhood games and adult financial trauma.",
    "🧃 The official Suimon drink is optimism with a splash of belief.",
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




































