"""
Handles messages sent by user.
Then sends the messge to models.Admin.ADMIN.
"""

from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from telebot import formatting

# import models
from tgbot.models.users_model import Admin

blocked_users = []  # if you want, you can rewrite the bot with database.


async def user_text_message(message: Message, bot: AsyncTeleBot):
    """
    Handles messages sent by user.
    Then sends the message to models.Admin.ADMIN.
    This handler only detects text messages.
    """
    # Get the user's username
    username = message.from_user.username
    # Send the message to the recipient, along with the user's username and ID
    await bot.send_message(chat_id = Admin.ADMIN.value,
        text = formatting.format_text(f'From @{username} ({message.chat.id})', 'Message:',
            formatting.hitalic(message.text)
        ), parse_mode = 'HTML'
    )


async def user_media_message(message: Message, bot: AsyncTeleBot):
    """
    Handles messages sent by user.
    Then sends the message to models.Admin.ADMIN.

    This handler only detects media messages.
    """
    if message.sticker:
        # Send the sticker to the admin chat
        await bot.send_sticker(chat_id = Admin.ADMIN.value, sticker = message.sticker.file_id)
    else:
        # Send the media message to the admin chat
        await bot.copy_message(chat_id = Admin.ADMIN.value, from_chat_id = message.chat.id,
                               message_id = message.message_id,
                               caption = formatting.format_text(f'#{message.chat.id} ({message.chat.username})',
                                                                'Caption:', formatting.hitalic(
                                       message.caption if message.caption else 'No caption'
                                       )
                                                                ), parse_mode = 'HTML'
                               )


async def user_is_banned(message: Message, bot: AsyncTeleBot):
    """
    Show the user that he/she is banned.
    """
    await bot.send_message(chat_id = message.chat.id, text = 'You were banned some time ago. You cannot write anymore.'
    )


async def message_is_too_long(message: Message, bot: AsyncTeleBot):
    """
    Show the user that his/her message is too long.
    """
    await bot.send_message(chat_id = message.chat.id,
        text = 'Text or caption of the message is too long. Please try to shorten it.'
    )
