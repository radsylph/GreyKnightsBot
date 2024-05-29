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