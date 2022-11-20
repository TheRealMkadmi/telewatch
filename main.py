from loguru import logger
from telethon import TelegramClient, events

API_ID = 21896519
API_HASH = '0fe40568b1bb3d76b877aa1e35e7f90e'

client = TelegramClient('session_read', API_ID, API_HASH)


@client.on(events.NewMessage(
    chats=("DB-MARKEET", "Crackers Club"),
    forwards=False,
    incoming=True,
))
async def my_event_handler(event):
    chat = await event.get_chat()
    sender = await event.get_sender()
    logger.info(f'Chat: {chat.title} | Sender: {sender.first_name} | Message: {event.text}')
    logger.info(f"Message from {sender.username}: {event.raw_text}")

    # do whatever you want here


client.start()
client.run_until_disconnected()
