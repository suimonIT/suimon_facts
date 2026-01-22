import random
import asyncio
from telegram import Bot
from telegram.constants import ParseMode

# ================= CONFIG =================
BOT_TOKEN = "8307980171:AAEPQxPujHOy0j1WN-bA2RWfq7z_fTKcOes"
CHAT_ID = -1003407035529  

INTERVAL_SECONDS = 3600  # 1 Stunde

# ================= FACTS =================
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

# ================= BOT LOOP (BLEIBT IMMER WACH) =================
async def main():
    bot = Bot(token=BOT_TOKEN)

    while True:
        try:
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

            print("Fact gesendet")

        except Exception as e:
            print("Fehler:", e)

        await asyncio.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    asyncio.run(main())


