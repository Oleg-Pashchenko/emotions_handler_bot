import random

from aiogram import types

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
from main import bot
from bot import dp
from handlers import menu

new_event_btn_text = 'Новое событие'
old_event_btn_text = 'Привязать к событию'
its_old_event_btn_text = 'Все же это уже созанное событие ;)'
its_new_event_btn_text = 'Все же это новое событие ;)'

new_or_old_event_markup = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[KeyboardButton(text=new_event_btn_text)],
                                                                              [KeyboardButton(
                                                                                  text=old_event_btn_text)],
                                                                              [KeyboardButton(text=menu.back_to_menu)]])
its_old_event_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                           keyboard=[[KeyboardButton(text=its_old_event_btn_text)],
                                                     [KeyboardButton(text=menu.back_to_menu)]])
its_new_event_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                           keyboard=[[KeyboardButton(text=its_new_event_btn_text)],
                                                     KeyboardButton(text=menu.back_to_menu)])


@dp.message(F.content_type.in_({'voice', 'video', 'photo', 'video_note'}))
async def handle_photo_and_video(message: types.Message):
    if message.content_type == types.ContentType.PHOTO:
        file_id, ext = message.photo[-1].file_id, 'png'
    elif message.content_type == types.ContentType.VIDEO:
        file_id, ext = message.video.file_id, 'mp4'
    elif message.content_type == types.ContentType.VOICE:
        file_id, ext = message.voice.file_id, 'oga'
    else:
        file_id, ext = message.video_note.file_id, 'mp4'
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path
    downloaded_file = await bot.download_file(file_path)
    with open(f'files/{random.randint(1000000, 10000000)}.{ext}', 'wb') as new_file:
        new_file.write(downloaded_file.read())
    await message.answer(
        f"Вложение получено!\nВыбери это новое событие или это событие уже относится к какому-то блогу ранее созданному:",
        reply_markup=new_or_old_event_markup)


@dp.message(lambda m: m == new_event_btn_text or m == its_new_event_btn_text)
async def new_event_action(message: types.Message) -> None:
    await message.answer(
        "Введи название блога в который сохранить эту историю\n\nПояснение: самая простая аналогия это день и событие. Если не знаешь как назвать блог можешь назвать его датой - 21.08.2022.\nУже внутри блога будут события.\n\nБлог - объедененные воедино события.\nТак введи все же название:",
        reply_markup=its_old_event_markup)


@dp.message(lambda m: m == old_event_btn_text or m == its_old_event_markup)
async def old_event_action(message: types.Message) -> None:
    await message.answer("Выбери блог к которому отнести это событие:", reply_markup=its_new_event_markup)


@dp.message()
async def write_blog_name_action(message: types.Message) -> None:
    pass


@dp.message()
async def write_event_name_action(message: types.Message) -> None:
    pass


@dp.message()
async def event_saved_action(message: types.Message) -> None:
    pass
