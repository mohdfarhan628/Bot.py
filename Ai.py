import openai
from telethon import TelegramClient, events

# OpenAI API Key
openai.api_key = "your_openai_api_key"

api_id = 1234567  
api_hash = "your_api_hash"

client = TelegramClient("my_session", api_id, api_hash)


@client.on(events.NewMessage(incoming=True))
async def handler(event):
    sender = await event.get_sender()
    user_message = event.message.message
    print(f"{sender.first_name}: {user_message}")

  
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    
    bot_reply = response["choices"][0]["message"]["content"]
    print(f"AI: {bot_reply}")

  
    await event.reply(bot_reply)

print("🤖 AI Auto Reply start...")
client.start()
client.run_until_disconnected()
