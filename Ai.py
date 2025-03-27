import openai
from telethon import TelegramClient, events
import os

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Telegram API Credentials
API_ID = 27574582  # तुम्हारी API ID
API_HASH = "29926c178311ce9399459617fbbe7d01"  # तुम्हारा API Hash

# Telethon Client (Session-Based)
client = TelegramClient("my_session", API_ID, API_HASH)

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

print("🤖 AI Auto Reply started...")
client.start()
client.run_until_disconnected()