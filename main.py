import asyncio
import re
import sys
from decouple import config
from typing import Final
from telegram import Update, Bot
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
)

# from database import (
#     agregar_participante,
#     eliminar_participante,
#     consultar_participantes,
#     borrar_todo,
# )

TOKEN: Final = config("BOT_TOKEN")
BOTNAME: Final = "@Lord_Emperador_Bot"
chatId = "-1002126307423"

bot : Bot = Bot(token=TOKEN)
application : Application = Application.builder().token(TOKEN).build()

# Bot commands
async def Bot_help_commands(update: Update, context: CallbackContext):
    await update.message.reply_text(
        """
    /ayuda: enseña como usar el bot de forma facil y sencilla
    /agregar <nombre> <grupo>: agrega una persona a la base de datos
    /eliminar <nombre> <grupo>: elimina una persona de la base de datos \U0001f6a8
    /lista <grupo>: muestra todos los registros de personas en un grupo
    /reset <grupo>: CUIDADO elimina todos los registros de personas en un grupo \U0001f6a8
    """
    )


# Bot Messages


async def handle_message(update: Update, context: CallbackContext):
    text: str = update.message.text.lower()
    print(update.message.text)
    if "@everyone" in text:
        print("toditos")
        # await update.message.reply_text(handler_list_participants(update, context))
    elif "sexo" in text:
        await update.message.reply_text("anal")
    elif "hola" in text:
        await update.message.reply_text(f"Hola @{update.message.from_user.username}")
    elif "guajiro" in text:
        await update.message.reply_text("Que racista Papu :(")
    elif (
        (update.message.from_user.username == "InfinitumDecay")
        and (len(text) > 5)
        and ("soto" in text)
    ):
        print(text)
        await update.message.reply_text("SOTOOOOO")


# def handler_add_participant(update: Update, context: CallbackContext):
#     nombre = update.message.text.split(" ")[1]
#     # grupo = update.message.text.split(" ")[2]
#     update.message.reply_text(agregar_participante(nombre))


async def handler_chatId(update: Update, context: CallbackContext):
    await update.message.reply_text(f"el chad id es: {update.message.chat_id}")
    chatId = await update.message.chat_id


# async def hanlder_delete_participant(update: Update, context: CallbackContext):
#     nombre = await update.message.text.split(" ")[1]
#     # grupo = await update.message.text.split(" ")[2]
#     await update.message.reply_text(eliminar_participante(nombre))


# async def handler_list_participants(update: Update, context: CallbackContext):
#     await update.message.reply_text(consultar_participantes())


async def get_group_members(update: Update, context: CallbackContext):
    chat_id = await update.message.chat_id
    admins = await context.bot.get_chat_administrators(chat_id)
    message = "los miembros del grupo son: \n"
    for admin in admins:
        message += "@" + admin.user.username + "\n"
    await update.message.reply_text(message)


if __name__ == "__main__":
    print("Starting bot")
    application.add_handler(CommandHandler("ayuda", Bot_help_commands))
    # application.add_handler(CommandHandler("agregar", handler_add_participant))
    # application.add_handler(CommandHandler("eliminar", hanlder_delete_participant))
    # application.add_handler(CommandHandler("everyone", handler_list_participants))
    application.add_handler(CommandHandler("id", handler_chatId))
    # application.add_handler(CommandHandler("members", get_group_members))
    application.add_handler(MessageHandler(filters.TEXT, handle_message))
    print("Polling...")
    application.run_polling(1.0)
