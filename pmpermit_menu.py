"""
Support chatbox for pmpermit.
Used by incoming messages with trigger as /start
Will not work for already approved people.
Credits: written by ༺αиυвιѕ༻ {@A_Dark_Princ3}
"""
import asyncio

from telethon import events, functions

import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql

from . import ALIVE_NAME, PM_START

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"
PREV_REPLY_MESSAGE = {}


@bot.on(events.NewMessage(pattern=r"\/start", incoming=True))
async def _(event):
    chat_id = event.from_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if chat_id not in PM_START:
            PM_START.append(chat_id)
        if event.fwd_from:
            return
        if not event.is_private:
            return
        PM = (
            "Hola. Estás accediendo al menú disponible de Skueletor, "
            f"{DEFAULTUSER}.\n"
            "__Hagamos esto sin problemas y déjeme saber por qué está aquí.__\n"
            "**Elija una de las siguientes razones por las que está aquí:**\n\n"
            "`a`. Para chatear con Skueletor.\n"
            "`b`. Para enviar spam a la bandeja de entrada de Skueletor.\n"
            "`c`. Para preguntar algo.\n"
            "`d`. Para pedir algo.\n"
        )
        ONE = (
            "__Bueno. Su solicitud ha sido registrada. No envíes spam a la bandeja de entrada de mi maestro. Puedes esperar una respuesta en 24 años luz. Es un hombre ocupado, probablemente a diferencia de ti.__\n\n"
            "**⚠️ Serás bloqueado y reportado si envías spam a Skueletor. ⚠️**\n\n"
            "__Utiliza__ `/start` __para volver al menú principal.__"
        )
        TWO = " `███████▄▄███████████▄  \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀▀▀█░░░░██████▀  \n░░░░░░░░░█░░░░█  \n░░░░░░░░░░█░░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░░▀▀ `\n\n**Que aburrido eres, esta no es tu casa. Ve a molestar a alguien más. Ha sido bloqueado y denunciado hasta nuevo aviso.**"
        THREE = "__Bueno. Skueletor aún no ha visto tu mensaje. Por lo general, responde a las personas, aunque no le gustan las repetidas.__\n __Él responderá cuando regrese, si quiere. Ya hay muchos mensajes pendientes.😶__\n **No envíe spam a menos que desee ser bloqueado y denunciado.**"
        FOUR = "`Bueno. por favor tenga los modales básicos para no molestar demasiado a Skueletor. Si desea ayudarlo, pronto le responderá.`\n**No pregunte repetidamente, de lo contrario será bloqueado y reportado.**"
        LWARN = "**Esta es tu última advertencia. NO envíes otro mensaje, de lo contrario será bloqueado y denunciado. Manten la paciencia. Skueletor te responderá lo antes posible.**\n__Utiliza__ `/start` __para volver al menú principal.__"
        try:
            async with event.client.conversation(chat) as conv:
                if pmpermit_sql.is_approved(chat_id):
                    return
                await event.client.send_message(chat, PM)
                chat_id = event.from_id
                response = await conv.get_response(chat)
                y = response.text
                if y == "a":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    await event.client.send_message(chat, ONE)
                    response = await conv.get_response(chat)
                    if not response.text == "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        await event.client.send_message(chat, LWARN)
                        response = await conv.get_response(chat)
                        if not response.text == "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            await event.client.send_message(chat, TWO)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
                elif y == "b":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    await event.client.send_message(chat, LWARN)
                    response = await conv.get_response(chat)
                    if not response.text == "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        await event.client.send_message(chat, TWO)
                        await asyncio.sleep(3)
                        await event.client(functions.contacts.BlockRequest(chat_id))
                elif y == "c":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    await event.client.send_message(chat, THREE)
                    response = await conv.get_response(chat)
                    if not response.text == "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        await event.client.send_message(chat, LWARN)
                        response = await conv.get_response(chat)
                        if not response.text == "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            await event.client.send_message(chat, TWO)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
                elif y == "d":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    await event.client.send_message(chat, FOUR)
                    response = await conv.get_response(chat)
                    if not response.text == "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        await event.client.send_message(chat, LWARN)
                        response = await conv.get_response(chat)
                        if not response.text == "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            await event.client.send_message(chat, TWO)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
                else:
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    await event.client.send_message(
                        chat,
                        "Ha introducido un comando no válido. Por favor envía `/start` nuevamente o no envíe otro mensaje si no desea ser bloqueado y reportado como spam.",
                    )
                    response = await conv.get_response(chat)
                    z = response.text
                    if not z == "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        await event.client.send_message(chat, LWARN)
                        await conv.get_response(chat)
                        if not response.text == "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            await event.client.send_message(chat, TWO)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
        except:
            pass
