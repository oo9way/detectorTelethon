from telethon import TelegramClient, events
from checker import check

api_id = 8184910
api_hash = "df0a97c7b6d2163610d94c01024e4107"

client = TelegramClient('telethon', api_id, api_hash)


@client.on(events.NewMessage)
async def handle_message(event):
    user_id = event.sender_id
    message_text = event.message.message
    sender = await event.get_sender()
    first_name = sender.first_name if sender.first_name else "Mijoz"

    if not check(message_text):
        return

    chat_title = event.chat.title if event.chat else "Unknown Group"
    user_profile_link = f"[{first_name}](tg://user?id={user_id})"
    user_profile_link_with_id = f"[havola](tg://user?id={user_id})"

    formatted_message = (
        "**Yangi buyurtma guruhdan:**\n"
        f"[{chat_title}](tg://resolve?domain={event.chat.username})\n\n"
        f"**Xabar**: {message_text}\n\n"
        f"**Yuboruvchi **: {user_profile_link}\n\n"
        f"**Aloqaga chiqish**: {user_profile_link_with_id}\n"
    )

    await client.send_message(-1002230931332, formatted_message, parse_mode='markdown')
    await client.send_message(-1002184517372, formatted_message, parse_mode='markdown')


async def main():
    await client.start()
    await client.run_until_disconnected()


if __name__ == '__main__':
    client.loop.run_until_complete(main())
