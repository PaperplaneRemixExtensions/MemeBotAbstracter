# Meme Bots Helper Extension for PaperplaneRemix.

# Abstracted conversation with @QuotLyBot to generate
# stickers to quote people's famous words [XD].

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest

from userbot import client
from userbot.utils.events import NewMessage

plugin_category = "misc"


@client.onMessage(command=("quote", plugin_category),
                  outgoing=True,
                  regex=r"q(uote)?$")
async def quotly(event: NewMessage.Event) -> None:
    """Stickerize a message using @QuotLyBot"""
    await event.get_reply_message()
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`I can't quote the void!`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("`Reply to text message`")
        return
    chat = "@QuotLyBot"
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739))
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await client.send_read_acknowledge(conv.chat_id, response)
        except YouBlockedUserError:
            await event.reply("`You need to` /start `the` @QuotLyBot `first!`")
            return
        if response.text.startswith("Hi!"):
            await event.edit(
                "`Can you kindly disable your forward privacy settings for good?`"
            )
        else:
            await event.delete()
            await event.client.send_message(event.chat_id,
                                            response.message,
                                            reply_to=event.reply_to_msg_id)
