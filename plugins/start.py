import pyrogram
@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(chat_id=update.chat.id,text="Salom, xush kelibsiz. Ushbu botga url manzildagi fayl manzilini yuboring va shu bot orqali yuklab oling. Agarda video yoki fayllaringiz ustida rasm(thumbnail) bo'lishini hohlasangiz hoziroq rasmingizni yuboring.\nEslatma: url manzil http yoki https bilan boshlanishi shart",reply_to_message_id=update.message_id)