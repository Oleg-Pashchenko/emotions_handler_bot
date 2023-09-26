from aiogram import types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.markdown import hbold

from bot import dp


on_site_btn_text = 'Просмотр историй на сайте'
search_by_date_btn_text = 'Просмотр историй по датам'
delete_my_story_btn_text = 'Удалить историю'
add_story_btn_text = 'Добавить историю'
random_story_btn_text = 'Случайная история'
back_to_menu = 'Давай назад в меню!'
back_to_menu_markup = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[KeyboardButton(text=back_to_menu)]])
hello_keyboard = [[KeyboardButton(text=add_story_btn_text), KeyboardButton(text=random_story_btn_text)],
                  [KeyboardButton(text=delete_my_story_btn_text)],
                   [KeyboardButton(text=search_by_date_btn_text)],
                   [KeyboardButton(text=on_site_btn_text)]]
hello_markup = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=hello_keyboard)


@dp.message(lambda m: m.text == '/start' or m.text == back_to_menu)
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
        f"возможно я хочу показать тебе значимость тебя в своей жизни.\n\nВсе хватит.\n\nПриветственный текст и так затянулся.\n\n(P.S.) (Обычно такие творения от меня стоят примерно тысяч 20 (потрачено +- 6 кодочасов), но я хочу лишь эмоций)", reply_markup=hello_markup)


@dp.message(lambda m: m.text == on_site_btn_text)
async def view_on_site_action(message: types.Message) -> None:
    await message.answer("Посмотреть все истории ты можешь на сайте:\nhttp://juicy-and-seekness.ru/")


@dp.message(lambda m: m.text == search_by_date_btn_text)
async def search_by_date_action(message: types.Message) -> None:
    await message.answer("Для поиска истории по дате найди дату в списке или введи свою в формате dd.mm.yyyy.\n(Пример: 21.08.2022)")


@dp.message(lambda m: m.text == add_story_btn_text)
async def add_story_action(message: types.Message) -> None:
    await message.answer("Отправь фото, видео, голосовое, кружочек, либо перешли его сюда:", reply_markup=back_to_menu_markup)


@dp.message(lambda m: m.text == random_story_btn_text)
async def random_story_action(message: types.Message) -> None:
    await message.answer("Случайная история")


@dp.message(lambda m: m.text == delete_my_story_btn_text)
async def edit_my_stories_action(message: types.Message) -> None:
    await message.answer("Удалить историю")


