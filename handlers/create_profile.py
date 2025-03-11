from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from db.add_user import add_user
from keyboards.keyboards1 import keyboard

router = Router()


class ProfileStates(StatesGroup):
    name = State()
    age = State()
    description = State()
    photo = State()

@router.message(Command('create'))
async def create_command(message: Message, state: FSMContext):
    await message.answer("Enter your name:")
    await state.set_state(ProfileStates.name)


@router.message(ProfileStates.name)
async def state_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Enter your age:")
    await state.set_state(ProfileStates.age)
    
    
@router.message(ProfileStates.age)
async def state_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(text="Age must be a number")
        return
    await state.update_data(age=message.text)
    await message.answer("Write about yourself:")
    await state.set_state(ProfileStates.description)
    

@router.message(ProfileStates.description)
async def state_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Send your photo:")
    await state.set_state(ProfileStates.photo)
    

@router.message(ProfileStates.photo)
async def state_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    user_data = await state.get_data()
    
    await message.answer_photo(photo=user_data['photo'],
                               caption=f"Your name is: {user_data['name']}\nYou're: {user_data['age']} years old\nAbout you: {user_data['description']}")
    
    
    await add_user(user_id=message.from_user.id, 
                   name=user_data['name'], 
                   age=user_data['age'], 
                   description=user_data['description'], 
                   photo=user_data['photo'])
    
    await message.answer("Profile created successfully!", reply_markup=keyboard())
    await state.clear()