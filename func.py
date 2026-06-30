import asyncio
from aiogram import Dispatcher, Bot, Router
from aiogram.filters import Command, callback_data
from aiogram.types import message, Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Узнать погоду")]
        ], resize_keyboard=True

    )
    return keyboard

    return keyboard
def main_inline_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="О боте", callback_data="info")],
        [InlineKeyboardButton(text="Команды", callback_data="commands")]
    ]
    )
    return keyboard