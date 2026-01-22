import random
import asyncio
from telegram import Bot
from telegram.constants import ParseMode

# ================= CONFIG =================
BOT_TOKEN = "8307980171:AAEPQxPujHOy0j1WN-bA2RWfq7z_fTKcOes"
CHAT_ID = -1003407035529  

INTERVAL_SECONDS = 360  # 1 Stunde

# ================= FACTS =================
SUIMON_FACTS = [
    "When the original dev abandoned the project, the community stepped up and took over as CTO to continue building.",
    "SUIMON proves that strong communities can revive and grow projects even after setbacks.",
    "SUIMON is a reminder that in crypto, the community is the real backbone of any project.",
    "Built by the people, for the people — SUIMON is powered by its community.",
    "From abandoned to reborn — SUIMON is a true community comeback story.",
    "SUIMON shows that transparency and consistency matter more than hype.",
    "In crypto, strong hands build long-term value — SUIMON embraces that mindset.",
    "SUIMON focuses on organic growth, not short-term hype.",
    "No promises, just building — that’s the SUIMON way.",
    "SUIMON believes real value is created during quiet times, not during hype cycles.",
    "Community over charts — SUIMON keeps building regardless of market conditions.",
    "Slow and steady building often wins the race — SUIMON stays consistent.",
    "SUIMON is an example of how decentralization starts with community responsibility.",
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




