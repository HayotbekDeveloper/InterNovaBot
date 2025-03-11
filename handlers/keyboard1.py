from aiogram import Router, F, types, html
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message
from aiogram.types import FSInputFile, URLInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.types import ReplyKeyboardRemove

from keyboards.keyboards1 import keyboard

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(f"Hi, {html.bold(message.from_user.full_name)}! 👋 \nWelcome to InterNova Bot! 💡", reply_markup=keyboard(), parse_mode=ParseMode.HTML)

@router.message(F.text.lower() == 'html and markdown texts')
async def texts(message: types.Message):
    await message.reply('<i>HI i am an italic </i>\n<b>and i am a bold text</b>',
                         parse_mode=ParseMode.HTML)
    await message.reply('||Spoiler||\n~Hellooooo~\n[Click to this text](https://wallhere.com/ru/wallpaper/1315051)',
                         parse_mode=ParseMode.MARKDOWN_V2)

@router.message(F.text.lower() == 'stickers')
async def sticker_commands(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAEN0Hhnsw6l7Vw2esXWKI_IAehWlYvi2AACVAADQbVWDGq3-McIjQH6NgQ')
    await message.answer_sticker('CAACAgIAAxkBAAEN0r1ns4hnoSw490iG3XKQucKDtrm2HgACBQADwDZPE_lqX5qCa011NgQ')

@router.message(F.text.lower() == 'emoji')
async def emoji_commands(message: types.Message):
    await message.answer_dice(DiceEmoji.DART)
    
@router.message(F.text.lower() == 'image', flags={'type_operation': 'upload_photo'})
async def image_commands(message: types.Message):
    my_image = FSInputFile('./cute-kitten-3840x2743-12770.jpg')
    my_image2 = URLInputFile('https://avatars.mds.yandex.net/get-mpic/3907093/img_id8825566720493712783.jpeg/orig')
    await message.answer_photo(my_image, caption="Sleeping cat!")
    await message.answer_photo(my_image2, caption="Rain!")

@router.message(F.text.lower() == 'video', flags={'type_operation': 'upload_video'})
async def video_commands(message: types.Message):
    video = FSInputFile('./12981693_1280_720_30fps.mp4')
    await message.answer_video(video, caption="Snow")

@router.message(F.text.lower() == 'group', flags={'type_operation': 'upload_group'})
async def group_commands(message: types.Message):
    media = MediaGroupBuilder(caption="Mediagroup!")
    media.add_photo(FSInputFile('./cute-kitten-3840x2743-12770.jpg'))
    media.add_photo(FSInputFile('./dandelion-flower-5120x2880-12847.png'))
    media.add_video(FSInputFile('./12981693_1280_720_30fps.mp4'))
    await message.answer_media_group(media=media.build())

@router.message(F.text.lower() == 'audio', flags={'type_operation': 'upload_audio'})
async def audio_commands(message: types.Message):
    audio = FSInputFile('./Meditative(chosic.com).mp3')
    await message.answer_audio(audio, caption="just music")
    await message.answer_voice(audio, caption="just music")
    
@router.message(F.text.lower() == 'document', flags={'type_operation': 'upload_document'})
async def document_commands(message: types.Message):
    file = FSInputFile('./cute-kitten-3840x2743-12770.jpg')
    file2 = FSInputFile('./dandelion-flower-5120x2880-12847.png')
    await message.answer_document(file, caption='image file1')
    await message.answer_document(file2, caption='image file2')

@router.message(F.text.lower() == 'location', flags={'type_operation': 'upload_location'})
async def location_commands(message: types.Message):
    await message.answer_location('40.799696', '72.331668')

@router.message(F.text.lower() == 'photo')
async def download_photos(message: types.Message):
    await message.answer('Send any photo')
@router.message(F.text.lower() == 'create profile')
async def texts(message: types.Message):
    await message.answer(text='For creating a new profile use /create function.', reply_markup=ReplyKeyboardRemove())

@router.message(F.text.lower() == 'url')
async def url_commands(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='YouTube', url='https://youtube.com/'))
    builder.row(InlineKeyboardButton(text='Instagram', url='http://instagram.com/hayotbek_graphics'))
    await message.answer('HI, choose url', reply_markup=builder.as_markup())

@router.message(F.text.lower() == 'random number')
async def random_number_command(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Choose the number from 1 to 10",
        callback_data='random_value'
    ))
    await message.answer('Click here', reply_markup=builder.as_markup())

