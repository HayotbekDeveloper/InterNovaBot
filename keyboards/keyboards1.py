from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

def keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.row(
        KeyboardButton(text='Create Profile')
    )
    kb.row(
        KeyboardButton(text='HTML and Markdown texts'),
        KeyboardButton(text='Stickers'),
        KeyboardButton(text='Emoji')
    )
    kb.row(
        KeyboardButton(text='Image'),
        KeyboardButton(text='Video'),
        KeyboardButton(text='Group')
    )
    kb.row(
        KeyboardButton(text='Audio'),
        KeyboardButton(text='Document'),
        KeyboardButton(text='Location')
    )
    kb.row(
        KeyboardButton(text='Photo'),
        KeyboardButton(text='URL'),
        KeyboardButton(text='Random number')
    )
     
    return kb.as_markup(resize_keyboard=True)