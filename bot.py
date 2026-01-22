import random
import asyncio
import os
from telegram import Bot
from telegram.constants import ParseMode

# ========== CONFIG (Render Environment Vars) ==========
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# ========== FACTS ==========
SUIMON_FACTS = [
    "SUIMON is built on the Sui blockchain, designed for high-speed and low-latency transactions.",
    "The Sui network uses an object-centric data model, which SUIMON benefits from for scalability.",
    "SUIMON focuses on community-driven growth and on-chain transparency.",
    "Sui uses the Move programming language, giving SUIMON a strong security foundation.",
    "Low fees on Sui allow SUIMON to stay accessible for everyday users.",
    "SUIMON benefits from fast finality, settling transactions in seconds.",
    "The Sui ecosystem is still early-stage, giving SUIMON long-term upside potential.",
    "Parallel transaction execution on Sui improves SUIMON performance under load.",
]

# ========== BOT LOGIC ==========
async def send_fact():
    bot = Bot(token=BOT_TOKEN)
    fact = random.choice(SUIMON_FACTS)

    message = (
        "🧠 <b>SUIMON Fact</b>\n\n"
        f"{fact}"
    )

    await bot.send_message(
        chat_id=CHAT_ID,
        text=message,
        parse_mode=ParseMode.HTML
    )

if __name__ == "__main__":
    asyncio.run(send_fact())
