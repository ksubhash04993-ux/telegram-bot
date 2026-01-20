from telegram.ext import Updater, MessageHandler, Filters
import os

class ID:
    def __init__(self):
        self.ID = 0
        self.name = "name"
        self.phone = "+39 55778895"
        self.username = "@username"


numbers = []
for i in range(0, 15000):
    numbers.append(ID())
    numbers[i].ID = i
    numbers[i].name = f"name_{i}"
    numbers[i].phone = f"+39 55778895_{i}"
    numbers[i].username = f"@user_{i}"


def reply(update, context):
    user_input = update.message.text.strip()

    filtResult = list(filter(lambda x: x.phone == user_input or x.username == user_input, numbers))

    if not filtResult:
        update.message.reply_text("Not found")
    else:
        data = filtResult[0]
        update.message.reply_text(
            f"ID: {data.ID}\n"
            f"Name: {data.name}\n"
            f"Phone: {data.phone}\n"
            f"Username: {data.username}"
        )


TOKEN = os.environ.get("8403450771:AAGtRCsJ66LaAPGY-pPCXjrL47VU-Kr8YZM")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

print("Bot is running...")
updater.start_polling()
updater.idle()
