from telethon import TelegramClient, events

api_id = 8184910
api_hash = "df0a97c7b6d2163610d94c01024e4107"

word_list = ["odam", "pochta", "bor", "одам", "почта", "бор", "ketish", "kerak", "кетиш", "керак", "ketishim",
             "кетишим", "borish", "borishim", "боришим", "бориш"
             "пучта", "puchta", "po'chta", "powta", "po'wta"]

client = TelegramClient('telethon', api_id, api_hash)



@client.on(events.NewMessage)
async def handle_message(event):
    sender = await event.get_sender()
    group = event.chat
    user_id = event.message.from_id
    message = f"""
    Yangi buyurtma

    Guruh: {group.title} (https://t.me/c/{group.id})
    Mijoz: Asadbey K.
    Xabar: odam bor
    Aloqa:5230756957 (https://t.me/user?id=5230756957)    
    """
    print(event.chat)
    print(event.message.text)
    print(f"Message: {vars(event.message.from_id)}")


async def main():
    await client.start()
    await client.run_until_disconnected()


if __name__ == '__main__':
    client.loop.run_until_complete(main())