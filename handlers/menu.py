from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.markdown import hbold

from bot import dp
from handlers.adder import Form
from misc import db

on_site_btn_text = 'Просмотр историй на сайте'
delete_my_story_btn_text = 'Удалить историю'
add_story_btn_text = 'Добавить историю'
hello_keyboard = [[KeyboardButton(text=add_story_btn_text), KeyboardButton(text=delete_my_story_btn_text)],
                  [KeyboardButton(text=on_site_btn_text)]]
hello_markup = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=hello_keyboard)


@dp.message(lambda m: m.text == '/start')
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Привет, {hbold(message.from_user.full_name)}!\nДобро пожаловать в {hbold('Хранителя Эмоций')}.\n\n"
        f"Здесь ты можешь напоследок сохранить запоминающиеся и ключевые моменты"
        f" в своей жизни связанные со мной (@DrunkenHedgehog).\nСмотреть моменты также можно в Web версии по адресу:\nhttp://juicy-and-seekness.ru/\n\nДумаю такая база может стать неплохой "
        f"защитой от удаления нашего чата.\n\nДля добавления момента достаточно либо просто переслать сюда "
        f"любое вложение из нашего чата (фото, видео, голосовое, кружок), либо действовать через кнопку `Добавить историю`.\n\n"
        f"Если существует несколько вложений относящихся к одному и тому же событию их можно"
        f" связывать. Это ты легко поймешь из инструкции потом.\n\n\nТы - первый человек кто им"
        f" пользуется, поэтому могут быть баги.\n\n\n{hbold('Если ты не хочешь')}"
        f"{hbold(' идти в будущее, то хотя бы сохрани прошлое.')}\n\n\nНе думаю что что-то вообще возможно потом после всего что я сейчас чувствую,"
        f" а я чувствую использованность, я в целом не знаю зачем это я сейчас это делаю и пишу, "
        f"возможно я хочу показать тебе значимость тебя в своей жизни.\n\nВсе хватит.\n\nПриветственный текст и так затянулся.",
        reply_markup=hello_markup)


@dp.message(lambda m: m.text == on_site_btn_text)
async def view_on_site_action(message: types.Message) -> None:
    await message.answer("Посмотреть все истории ты можешь на сайте:\nhttp://juicy-and-seekness.ru/")


@dp.message(lambda m: m.text == add_story_btn_text)
async def add_story_action(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Form.filename)
    await message.answer("Отправь фото, видео, голосовое, кружочек, либо перешли его сюда:")


@dp.message(lambda m: m.text == delete_my_story_btn_text)
async def edit_my_stories_action(message: types.Message) -> None:
    inline_keyboard = []
    for i in db.get_all_stories():
        inline_keyboard.append([InlineKeyboardButton(text=i[1], callback_data=f'delete-{i[1]}')])
    await message.answer("Выберите историю для удаления:", reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard))


@dp.callback_query(lambda m: 'delete' in m.data)
async def delete_story(data):
    await data.answer("Ok!")
    db.delete_story(data.data.replace('deete-', ''))
    await data.message.answer('История удалена!')
    await command_start_handler(data.message)