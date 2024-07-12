from telethon import TelegramClient, events

api_id = 8184910
api_hash = "df0a97c7b6d2163610d94c01024e4107"

word_list = ["odam", "ketadigan", "кетадиган", "pochta", "poshta", "пошта", "bor", "одам", "почта", "бор", "ketish", 
             "kerak", "кетиш", "керак", "ketishim", "ketmoqchi", "кетмоқчи", "кетмокчи" "edik", "едик", "едим",
             "кетишим", "borish", "borishim", "боришим", "бориш", "пучта", "puchta", "po'chta", "powta", "po'wta"]

black_list = ["юрамиз", "юраман", "оламиз", "оламан", "yuramiz", "yuraman", "olamiz", "olaman"]

client = TelegramClient('telethon', api_id, api_hash)


@client.on(events.NewMessage)
async def handle_message(event):
    user_id = event.sender_id
    message_text = event.message.message

    min_matches = 0
    black_list_matches = 0
    for text in message_text.split(" "):
        if str(text).lower() in word_list:
            min_matches += 1

        if str(text).lower() in black_list:
            black_list_matches += 1

    if black_list_matches != 0:
        return
    
    if not min_matches >= 2:
        return

    chat_title = event.chat.title if event.chat else "Unknown Group"
    user_profile_link = f"[Client](tg://user?id={user_id})"

    formatted_message = (
        "**Yangi buyurtma**\n\n"
        f"**Guruh**: [{chat_title}](tg://resolve?domain={event.chat.username})\n"
        f"**Mijoz**: {user_profile_link}\n"
        f"**Xabar**: {message_text}"
    )

    await client.send_message(-1002230931332, formatted_message, parse_mode='markdown')


async def main():
    await client.start()
    await client.run_until_disconnected()


if __name__ == '__main__':
    client.loop.run_until_complete(main())
