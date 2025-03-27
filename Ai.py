import os
import openai
from telethon import TelegramClient, events

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("⚠️ OPENAI_API_KEY is missing. Please set it in environment variables.")

openai.api_key = OPENAI_API_KEY

# Telegram API Credentials
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

if not API_ID or not API_HASH:
    raise ValueError("⚠️ API_ID or API_HASH is missing. Please set them in environment variables.")

API_ID = int(API_ID)

# Initializing Telegram Client
client = TelegramClient("my_session", API_ID, API_HASH)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    sender = await event.get_sender()
    user_message = event.message.message.strip()

    if not user_message:
        return  

    print(f"📩 {sender.first_name}: {user_message}")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
            max_tokens=150,
            temperature=0.7
        )

        bot_reply = response["choices"][0]["message"]["content"].strip()
        print(f"🤖 AI: {bot_reply}")

        await event.reply(bot_reply)

    except Exception as e:
        error_msg = "❌ Error: AI response failed."
        print(f"{error_msg} {str(e)}")
        await event.reply(error_msg)

print("✅ AI Auto Reply Bot Started...")
client.start()
client.run_until_disconnected()