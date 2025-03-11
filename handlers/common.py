from aiogram import Router, F, types
from aiogram.enums import ParseMode
from config.bot_config import bot, dp
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import FSInputFile, URLInputFile, KeyboardButton, ReplyKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.utils.media_group import MediaGroupBuilder
from random import randint
from aiogram.filters.command import Command, CommandObject
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from db.get_user import get_user

TEXT = '''
/help - reference text
/start - start the bot
/test_args - enter some arguments
/text - different text in different formats
/sticker - i'll send you stickers
/emoji - let's try your luck!
/image - shows images
/video - shows videos
/group - mediagroup
/audio - shows audios
/document - shows documents
/location - shows locations
/url - url inline button
/random_number - Random Number from 1 to 10
'''

router = Router()

@router.message(Command(commands=['profile']))
async def profile_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text='For creating a new profile use /create function. or use /cancel to end creating profile process') 

@router.message(Command(commands=['cancel']))
async def cancel_command(message: Message, state: FSMContext):
    if await state.get_state() is None:
        await message.answer(text='You have not started creating a profile yet')
        return

    await state.clear()
    await message.answer(text='You have canceled creating a profile')

# GET_USER
@router.message(Command(commands=['my_profile']))
async def my_profile_command(message: Message):
    profile = await get_user(user_id=message.from_user.id)
    await message.answer_photo(photo=profile.photo, 
                               caption=f"Your name is: {profile.name}\nYou're: {profile.age} years old\nAbout you: {profile.description}")

# HTML and Markdown texts
@router.message(F.text, Command(commands=['text']))
async def start_command(message: types.Message):
    await message.answer('<i>HI i am an italic </i>\n<b>and i am a bold text</b>',
                         parse_mode=ParseMode.HTML)
    await message.answer('||Spoiler||\n~Hellooooo~\n[Click to this text](https://wallhere.com/ru/wallpaper/1315051)',
                         parse_mode=ParseMode.MARKDOWN_V2)

# Stickers
@router.message(Command(commands=['sticker']))
async def sticker_command(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAEN0Hhnsw6l7Vw2esXWKI_IAehWlYvi2AACVAADQbVWDGq3-McIjQH6NgQ')
    await message.answer_sticker('CAACAgIAAxkBAAEN0r1ns4hnoSw490iG3XKQucKDtrm2HgACBQADwDZPE_lqX5qCa011NgQ')

# emoji
@router.message(Command(commands=['emoji']))
async def emoji_command(message: types.Message):
    await message.answer_dice(DiceEmoji.DART)

#image from computer and internet
@router.message(Command(commands=['image']), flags={'type_operation': 'upload_photo'})
async def image_command(message: types.Message):
    my_image = FSInputFile('./cute-kitten-3840x2743-12770.jpg')
    my_image2 = URLInputFile('https://avatars.mds.yandex.net/get-mpic/3907093/img_id8825566720493712783.jpeg/orig')
    await message.answer_photo(my_image, caption="Sleeping cat!")
    await message.answer_photo(my_image2, caption="Rain!")

#video from computer
@router.message(Command(commands=['video']), flags={'type_operation': 'upload_video'})
async def video_command(message:Message):
    video = FSInputFile('./12981693_1280_720_30fps.mp4')
    await message.answer_video(video, caption="Snow")
    
#video and image groups from computer
@router.message(Command(commands=['group']))
async def group_command(message: types.Message):
    media = MediaGroupBuilder(caption="Mediagroup!")
    media.add_photo(FSInputFile('./cute-kitten-3840x2743-12770.jpg'))
    media.add_photo(FSInputFile('./dandelion-flower-5120x2880-12847.png'))
    media.add_video(FSInputFile('./12981693_1280_720_30fps.mp4'))
    await message.answer_media_group(media=media.build())
    
#audio from computer
@router.message(Command(commands=['audio']), flags={'type_operation': 'upload_audio'})
async def audio_command(message: types.Message):
    audio = FSInputFile('./Meditative(chosic.com).mp3')
    await message.answer_audio(audio, caption="just music")
    await message.answer_voice(audio, caption="just music")

#document from computer
@router.message(Command(commands=['document']), flags={'type_operation': 'upload_document'})
async def document_command(message: types.Message):
    file = FSInputFile('./cute-kitten-3840x2743-12770.jpg')
    file2 = FSInputFile('./dandelion-flower-5120x2880-12847.png')
    await message.answer_document(file, caption='image file1')
    await message.answer_document(file2, caption='image file2')

#sending location
@router.message(Command(commands=['location']))
async def location_command(message: types.Message):
    await message.answer_location('40.799696', '72.331668')

# #send photo from user
# @router.message(F.photo)
# async def download_photo(message: types.Message):
#     await bot.download(message.photo[-1], destination='image.png')
#     await message.reply('Your image send')

# arguments
@router.message(Command(commands=['test_args']))
async def test_args_command(message: types.Message, command: CommandObject):
    if command.args is None:
        await message.answer("You're not enter any arguments")
        return
    try:
        name, age, city = command.args.split(' ')
    except ValueError:
        await message.answer("You're not write whole arguments, Example\n/test_args  <name> <age> <city>")
        return
    await message.answer(f'Your name is: {name}\nYou are: {age} years old\nYour city: {city}')
    
# message when user write help
@router.message(Command(commands=['help']))
async def start_command(message: types.Message):
    await message.reply(TEXT)

# inline url button 
@router.message(Command(commands=['url']))
async def url_command(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='YouTube', url='https://youtube.com/'))
    builder.row(InlineKeyboardButton(text='Instagram', url='http://instagram.com/hayotbek_graphics'))
    await message.answer('HI, choose url', reply_markup=builder.as_markup())

# inline button
@router.message(Command(commands=['random_number']))
async def random_number_command(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Choose the number from 1 to 10",
        callback_data='random_value'
    ))
    await message.answer('Click here', reply_markup=builder.as_markup())
    
@router.callback_query(F.data == 'random_value')
async def send_random_value(callback: CallbackQuery):
    await callback.message.answer(str(randint(1, 10)))
    await callback.answer('Thank you for using our bot!:)', show_alert=True)