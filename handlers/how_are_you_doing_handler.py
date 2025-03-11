from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.how_are_you_doing_keyboard import how_are_you_doing_kb

router = Router()


@router.message(Command('question'))
async def cmd_question(message: Message):
    await message.answer("How are you?", reply_markup=how_are_you_doing_kb())
    

@router.message(F.text.lower() == 'wonderful')
async def answer_yes(message: Message):
    await message.answer("I'm really happy for you :)", reply_markup=ReplyKeyboardRemove())
    
    
@router.message(F.text.lower() == 'bad')
async def answer_no(message: Message):
    await message.answer("sadly :(", reply_markup=ReplyKeyboardRemove())