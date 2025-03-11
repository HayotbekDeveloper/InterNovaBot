from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def how_are_you_doing_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='Wonderful')
    kb.button(text='Bad')
    return kb.as_markup(resize_keyboard=True)