import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.types import Message
from dotenv import load_dotenv, set_key

CONFIG_FILE = ".env"

def load_config():
    load_dotenv(CONFIG_FILE)
    token = os.getenv("TG_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    return token, chat_id

async def _setup():
    token = input("enter the Telegram bot token:").strip()
    if not token:
        return
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()
    print("Send any message to your bot in Telegram to determine the chat_id")
    chat_id = None
    
    @dp.message()
    async def on_message(message: Message):
        nonlocal chat_id
        if chat_id is None:
            chat_id = message.from_user.id
            print(f"The chat_id is defined: {chat_id}")
            await message.answer("telepush is configured!")
            await message.answer("use it at the beginning: <code>from telepush import telepush_send</code>", parse_mode="HTML")
            await message.answer("to send, use: <code>telepush_send()</code>", parse_mode="HTML")
            await bot.session.close()
            await dp.stop_polling()
            
    await dp.start_polling(bot)
    if chat_id is not None:
        set_key(CONFIG_FILE, "TG_TOKEN", token)
        set_key(CONFIG_FILE, "CHAT_ID", str(chat_id))
        print("the configuration is saved in .env")
    else:
        print("couldn't get chat_id, repeat the setting")

async def _send_async(text):
    token, chat_id = load_config()
    if not token or not chat_id:
        raise RuntimeError("telepush is not configured, launch telepush.py for setting up")
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode="HTML"))
    await bot.send_message(chat_id=int(chat_id), text=str(text))
    await bot.session.close()

def telepush_send(text):
    try:
        asyncio.run(_send_async(text))
    except RuntimeError as e:
        print(e)

def setup():
    if os.path.exists(CONFIG_FILE):
        print("telepush is already configured")
        asyncio.run(_send_async("telepush is ready!"))
    else:
        print("telepush is not configured. Starting setup...")
        asyncio.run(_setup())

if __name__ == "__main__":
    setup()
