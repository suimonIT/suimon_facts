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
    "🚨 BREAKING: Suikachu escaped rehab again. Hopium reserves at all time highs. Authorities advise calm and diamond hands.",
    "📘 The Suidex lists overconfidence as a passive debuff with a 99% uptime.",
    "🏟️ Arena leaders respect only one thing: consistency. And sometimes memes.",
    "🧪 Mixing hopium with impatience causes instant confusion and random button clicking.",
    "🐢 Suimon moves slow so trainers dont lose their sanity watching charts.",
    "🔍 The rarest Suimon ability is ignoring noise and not replying to doom posts.",
    "💊 Side effects of holding Suimon may include euphoria, delayed sleep, and saying trust the process unironically.",
    "🌫️ Suimon trainers dont chase pumps. They inhale hopium and wait.",
    "🧠 Adeniyi said build for the long term. Suimon trainers heard dont panic sell.",
    "⚗️ The Sui ecosystem runs on Move. Suimon trainers run on caffeine and hopium.",
    "🎮 Suimon is inspired by childhood games and adult financial trauma.",
    "📉 When charts go down, Suimon gains emotional resistance.",
    "🔥 Every Suimon arena teaches the same lesson: survive the noise.",
    "🌀 Too much alpha exposure may result in temporary delusion.",
    "🛑 Suimon rehab centers are full. Nobody wants to leave the ecosystem.",
    "🎨 Someone once tried to draw Suimon sober. It didnt feel right.",
    "🧬 Long term holders develop natural immunity to FUD.",
    "🧃 The official Suimon drink is optimism with a splash of disbelief.",
    "👁️ Suimon doesnt watch the chart. The chart watches Suimon."
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

    message = f"🧠<b>SUIMON Fact</b>\n\n{fact}"

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

































