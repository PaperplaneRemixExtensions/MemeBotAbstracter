# Meme Bots Helper Extension for PaperplaneRemix.
# Abstracted Inline Queries of @stickerizerbot.
# Copyright (C) 2020 Avinash Reddy <https://github.com/AvinashReddy3108>

import re
from userbot import client
from userbot.utils.events import NewMessage

plugin_category = "memes"

# Credits: https://git.io/JvxOa
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats 
    "]+")


@client.onMessage(command=("waifu", plugin_category),
                  outgoing=True,
                  regex="(wy|wai)fu(?: |$|\n)([\s\S]*)")
async def waifu(event: NewMessage.Event) -> None:
    """Generate random waifu sticker with the text!"""
    text = event.matches[0].group(2)
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            await event.answer("`No text given, hence the waifu ran away.`")
            return
    animus = [20, 32, 33, 40, 41, 42, 58]
    sticcers = await client.inline_query(
        "stickerizerbot", f"#{random.choice(animus)}{(deEmojify(text))}")
    try:
        await sticcers[0].click(event.chat_id,
                                reply_to=event.reply_to_msg_id,
                                silent=True if event.is_reply else False,
                                hide_via=True)
        await event.delete()
    except IndexError:
        await event.answer("`F, can't find any waifu for you :P`")
        return


@client.onMessage(command=("spongemock", plugin_category),
                  outgoing=True,
                  regex="(spng|sponge)mock(?: |$|\n)([\s\S]*)")
async def spngmock(event: NewMessage.Event) -> None:
    """Generate Spongebob sticker with the mocked text!"""
    text = event.matches[0].group(2)
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            await event.answer("`Can't mock to nothing`")
            return
    sticcers = await client.inline_query("stickerizerbot",
                                         f"#7{(deEmojify(text))}")
    try:
        await sticcers[0].click(event.chat_id,
                                reply_to=event.reply_to_msg_id,
                                silent=True if event.is_reply else False,
                                hide_via=True)
        await event.delete()
    except IndexError:
        await event.answer("`F, Spongebob ran away :P`")
        return


@client.onMessage(command=("google", plugin_category),
                  outgoing=True,
                  regex="(g|goo)gle(?: |$|\n)([\s\S]*)")
async def google(event: NewMessage.Event) -> None:
    """Generate Google search link with a fancy sticker."""
    text = event.matches[0].group(2)
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            await event.answer("`Can't google nothing`")
            return
    sticcers = await client.inline_query("stickerizerbot",
                                         f"#12{(deEmojify(text))}")
    try:
        await sticcers[0].click(event.chat_id,
                                reply_to=event.reply_to_msg_id,
                                silent=True if event.is_reply else False,
                                hide_via=True)
        await event.delete()
    except IndexError:
        await event.answer("`F, Google can't search this for you :P`")
        return


def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, '', inputString)
