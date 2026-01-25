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
    "Does she even hold your Suiballs?",
    "Nurse Joy and Officer Jenny are not just relatives, they are implied to be genetic clones.",
    "Suimon is technically a post-apocalyptic world where animals are already extinct.",
    "No one has ever seen a Suimon use the bathroom, yet the world has plumbing. Think about that.",
    "Chad has been 10 years old for over 25 years. This makes him canonically immortal.",
    "Suiamp can move mountains yet still needs 4 arms to carry groceries.",
    "Team Rocket has attempted more kidnappings than most true crime podcasts.",
    "Suimon trainers have never paid taxes in any known region.",
    "If a Suimon stares at a chart long enough, the chart moves out of fear.",
    "Suimon eggs hatch faster when the price goes up.",
    "Suikachu refused rehab after repeated attempts. Hopium is a helluva drug.",
    "Suimon only evolves after you emotionally detach.",
    "The Jengarcide will be studied for years to come.",
    "Whalemon can move markets by sneezing."
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






