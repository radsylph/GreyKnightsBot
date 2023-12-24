import re
from typing import Final
from telegram import Update
from telegram import Bot
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    Filters,
    Updater,
    CallbackContext,
)
from decouple import config
import sys

from database import (
    agregar_participante,
    eliminar_participante,
    consultar_participantes,
    borrar_todo,
)

TOKEN: Final = config("BOT_TOKEN")
BOTNAME: Final = "@Lord_Emperador_Bot"
chatId = "-1002126307423"


# Bot commands
def Bot_help_commands(update: Update, context: CallbackContext):
    update.message.reply_text(
        """
    /ayuda: enseña como usar el bot de forma facil y sencilla
    /agregar <nombre> <grupo>: agrega una persona a la base de datos
    /eliminar <nombre> <grupo>: elimina una persona de la base de datos \U0001f6a8
    /lista <grupo>: muestra todos los registros de personas en un grupo
    /reset <grupo>: CUIDADO elimina todos los registros de personas en un grupo \U0001f6a8
    """
    )


# Bot Messages


def handle_message(update: Update, context: CallbackContext):
    text: str = update.message.text.lower()
    print(text)
    if "@everyone" in text:
        update.message.reply_text(hanlder_list_participants(update, context))
    elif "sexo" in text:
        update.message.reply_text("anal")
    elif "hola" in text:
        update.message.reply_text(f"Hola @{update.message.from_user.username}")
    elif "guajiro" in text:
        update.message.reply_text("Que racista Papu :(")
    elif (
        (update.message.from_user.username == "InfinitumDecay")
        and (len(text) > 5)
        and ("soto" in text)
    ):
        print(text)
        update.message.reply_text("SOTOOOOO")


def handler_add_participant(update: Update, context: CallbackContext):
    nombre = update.message.text.split(" ")[1]
    # grupo = update.message.text.split(" ")[2]
    update.message.reply_text(agregar_participante(nombre))


def handler_chatId(update: Update, context: CallbackContext):
    update.message.reply_text(f"el chad id es: {update.message.chat_id}")
    chatId = update.message.chat_id


def hanlder_delete_participant(update: Update, context: CallbackContext):
    nombre = update.message.text.split(" ")[1]
    # grupo = update.message.text.split(" ")[2]
    update.message.reply_text(eliminar_participante(nombre))


def hanlder_list_participants(update: Update, context: CallbackContext):
    update.message.reply_text(consultar_participantes())


def get_group_members(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    admins = context.bot.get_chat_administrators(chat_id)
    message = "los miembros del grupo son: \n"
    for admin in admins:
        message += "@" + admin.user.username + "\n"
    update.message.reply_text(message)


if __name__ == "__main__":
    print("Starting bot")
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("ayuda", Bot_help_commands))
    dp.add_handler(CommandHandler("agregar", handler_add_participant))
    dp.add_handler(CommandHandler("eliminar", hanlder_delete_participant))
    dp.add_handler(CommandHandler("everyone", hanlder_list_participants))
    dp.add_handler(CommandHandler("id", handler_chatId))
    dp.add_handler(CommandHandler("members", get_group_members))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling()
    updater.idle()
