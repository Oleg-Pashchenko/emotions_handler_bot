import random

from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import F

from main import bot
from bot import dp
from misc import db

class Form(StatesGroup):
    filename = State()
    event = State()
    date = State()


@dp.message(Form.filename)
async def handle_photo_and_video(message: types.Message, state: FSMContext):
    if message.content_type == types.ContentType.PHOTO:
        file_id, ext = message.photo[-1].file_id, 'png'
    elif message.content_type == types.ContentType.VIDEO:
        file_id, ext = message.video.file_id, 'mp4'
    elif message.content_type == types.ContentType.VOICE:
        file_id, ext = message.voice.file_id, 'oga'
    elif message.content_type == types.ContentType.VIDEO_NOTE:
        file_id, ext = message.video_note.file_id, 'mp4'
    else:
        await message.answer("Некорректный формат файла!")
        return
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path
    try:
        downloaded_file = await bot.download_file(file_path)
        filename = f'web/static/files/{random.randint(1000000, 10000000)}.{ext}'
        await state.update_data(filename=filename)
        with open(filename, 'wb') as new_file:
            new_file.write(downloaded_file.read())
        await state.set_state(Form.event)
        await message.answer(
            f"Вложение получено!\nКак назовем?")
    except:
        await message.answer("Файл пока слишком большой! Но разработчик обещал починить как только выйдет из запоя!")

@dp.message(Form.event)
async def new_event_action(message: types.Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)

    await message.answer("Почти все. Введи дату события в формате (dd.mm.yyyy):")
    await state.set_state(Form.date)


@dp.message(Form.date)
async def write_date_action(message: types.Message, state: FSMContext) -> None:
    date_s = message.text
    date = date_s.split('.')
    if date[0].isdigit() and date[1].isdigit() and date[2].isdigit() and len(date[0]) == 2 and len(date[1]) == 2 and len(date[2]) == 4:
        data = await state.get_data()
        db.save(data['filename'], data['name'], date_s)
        await message.answer(f"Сохранено! Нажмите /start")
        await state.clear()
    else:
        await message.answer("Некорректный формат!")
