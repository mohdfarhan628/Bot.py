import openai
from telethon import TelegramClient, events
import os

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Telegram Bot Token
BOT_TOKEN = os.getenv("7740037319:AAEz_4UBuY04U3FcgBKsQKJsTdz-14JWd-A")  # Render में .env set file

# Telethon Client (Bot Session)
client = TelegramClient("bot_session", api_id=0, api_hash="", bot_token=BOT_TOKEN)

async def main():
    await client.start(bot_token=BOT_TOKEN)
    print("✅ AI Auto Reply Bot Started...")

    @client.on(events.NewMessage(incoming=True))
    async def handler(event):
        user_message = event.message.message
        print(f"User: {user_message}")

        # OpenAI API Call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )

        bot_reply = response["choices"][0]["message"]["content"]
        print(f"AI: {bot_reply}")

        await event.reply(bot_reply)

    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())