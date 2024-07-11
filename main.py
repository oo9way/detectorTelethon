from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode

api_id = 8184910
api_hash = "df0a97c7b6d2163610d94c01024e4107"
bot_token = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"

app = Client(
    "client_sasa",
    api_id=api_id, api_hash=api_hash,
    # bot_token=bot_token
)



word_list = ["odam", "pochta", "bor", "одам", "почта", "бор", "ketish", "kerak", "кетиш", "керак", "ketishim",
             "кетишим", "borish", "borishim", "боришим", "бориш"
             "пучта", "puchta", "po'chta", "powta", "po'wta"]

@app.on_message()
async def send_msg(client, message):
    print(message.text)


# @app.on_message(filters.group & filters.text & filters.incoming)
# async def my_handler(client, message):
#     print(message)
#     texts = message.text
#     user_id = message.from_user.id
#     first_name = message.from_user.first_name
#     group_name = message.chat.title
#     group_id = message.chat.id
#     telegram_profile_link = f"tg://user?id={user_id}"
#     min_matches = 0
#     # print(message)

    
#     for text in texts.split(" "):
#         if text in word_list:
#             min_matches += 1

#     if min_matches >=2:
#         profile_link = f'<a href="tg://t.me/user?id={user_id}">{user_id}</a>'

#         message = "<b>Yangi buyurtma</b>\n\n"
#         message += f"<b>Guruh</b>: <a href='https://t.me/c/{group_id}'>{group_name}</a>\n"
#         message += f"Mijoz: {first_name}\n"
#         message += f"Xabar: {texts}\n"
#         message += f"Aloqa:" + profile_link

#         # await app.send_message("me", message, parse_mode=ParseMode.HTML)
#         await app.send_message(chat_id=user_id, text=message)
        

app.run()

 # 