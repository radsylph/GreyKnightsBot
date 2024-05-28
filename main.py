import asyncio
import re
import sys
import os
from random import randint
from typing import Final
from telegram import Update, Bot
import json
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)

from database import (
    agregar_participante,
    eliminar_participante,
    consultar_participantes,
    borrar_todo,
)


TOKEN: Final = "6731060923:AAHXN9u6mtDsi4QjRxhgP20Wq_VOTu38Jxg"
BOTNAME: Final = "@Lord_Emperador_Bot"
chatId = "-1002126307423"

bot: Bot = Bot(token=TOKEN)
updater: Updater = Updater(token=TOKEN, use_context=True)


def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded {file} successfully")
        return json.load(bot_responses)


response_data = load_json("botMessages.json")


def BotMessages(userInput: str) -> str:
    for response in response_data:
        if userInput in response["user_input"]:
            return response["bot_response"]


# Bot commands
def Bot_help_commands(update: Update, context: CallbackContext):
    update.message.reply_text(
        """
    /ayuda: enseña como usar el bot de forma facil y sencilla
        /agregar <grupo>: agrega una persona a la base de datos
        /eliminar <grupo>: elimina una persona de la base de datos 
    """
    )


# Bot Messages


def handle_message(update: Update, context: CallbackContext) -> None:
    text: str = update.message.text.lower()
    print(update.message.text)
    response = BotMessages(text)
    print(response)
    if response == "event_everyone":
        print("toditos")
        response = handler_list_participants(update, context)
        update.message.reply_text(response)
    update.message.reply_text(response)


async def handler_chatId(update: Update, context: CallbackContext):
    await update.message.reply_text(f"el chad id es: {update.message.chat_id}")
    chatId = await update.message.chat_id


def handler_add_participant(update: Update, context: CallbackContext):
    nombre = update.message.text.split(" ")[1]
    # grupo = update.message.text.split(" ")[2]
    response = agregar_participante(nombre)
    update.message.reply_text(response)


def hanlder_delete_participant(update: Update, context: CallbackContext):
    nombre = update.message.text.split(" ")[1]
    # grupo = await update.message.text.split(" ")[2]
    response = eliminar_participante(nombre)
    update.message.reply_text(response)


def handler_list_participants(update: Update, context: CallbackContext):
    response = consultar_participantes()
    update.message.reply_text(response)


async def get_group_members(update: Update, context: CallbackContext):
    chat_id = await update.message.chat_id
    admins = await context.bot.get_chat_administrators(chat_id)
    message = "los miembros del grupo son: \n"
    for admin in admins:
        message += "@" + admin.user.username + "\n"
    await update.message.reply_text(message)


if __name__ == "__main__":
    print("Starting bot")
    updater.dispatcher.add_handler(CommandHandler("ayuda", Bot_help_commands))
    updater.dispatcher.add_handler(CommandHandler("agregar", handler_add_participant))
    updater.dispatcher.add_handler(
        CommandHandler("eliminar", hanlder_delete_participant)
    )
    updater.dispatcher.add_handler(CommandHandler("id", handler_chatId))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    print("Polling...")
    updater.start_polling()
    updater.idle()
