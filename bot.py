import random
import asyncio
from telegram import Bot
from telegram.constants import ParseMode

# ================= CONFIG =================
BOT_TOKEN = "8307980171:AAEPQxPujHOy0j1WN-bA2RWfq7z_fTKcOes"
CHAT_ID = -1003407035529  

INTERVAL_SECONDS = 30

# ================= FACTS =================
SUIMON_FACTS = [
    "SUIMON is a CTO project on the Sui blockchain.",
    "The visual theme of SUIMON is inspired by classic Pokémon-style character design.",
    "After the original developer stopped maintaining the project, community members assumed technical leadership.",
    "SUIMON operates without a centralized company structure.",
    "The project relies on community coordination rather than venture capital backing.",
    "SUIMON is deployed on the Sui blockchain, which uses the Move programming language.",
    "The Sui blockchain allows parallel transaction execution, which SUIMON inherits by default.",
    "SUIMON development decisions are discussed openly within the community.",
    "The project continued after its initial launch despite reduced liquidity during early stages.",
]

# ===== STATE =====
last_fact = None

# ===== BOT =====
bot = Bot(token=BOT_TOKEN)

async def send_fact():
    global last_fact

    fact = random.choice(SUIMON_FACTS)
    while fact == last_fact:
        fact = random.choice(SUIMON_FACTS)

    last_fact = fact

    message = f"🧠 <b>SUIMON Fact</b>\n\n{fact}"

    await bot.send_message(
        chat_id=CHAT_ID,
        text=message,
        parse_mode=ParseMode.HTML
    )

async def main():
    while True:
        try:
            await send_fact()
        except Exception as e:
            print("Error:", e)
        await asyncio.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    asyncio.run(main())






