from aiogram import Router, types

router = Router()

@router.message(commands=["myinfo"])
async def myinfo(message: types.Message):
    user = message.from_user.username or message.from_user.id

    text = f"""
{user}@debian
━━━━━━━━━━━━━━━━━━━━━━
🤖 My Custom Info

🟢 Status: Online

🌐 OS: Android / Linux
📦 Version: Custom Build

⏱ Uptime: Active
🧠 RAM: Safe Mode
⚙️ CPU: Disabled

📡 Ping: Stable

━━━━━━━━━━━━━━━━━━━━━━
💠 FLAX CUSTOM SYSTEM
"""
    await message.answer(text)
