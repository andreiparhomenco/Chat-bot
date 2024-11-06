from aiogram import (
    F,
    Router,
)  # Импортирую бота, диспетчера, Ф-магический фильтр, благоря нему можно получать любые сообщения от пользователя.
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import app.keyboards as kb

router = (
    Router()
)  # из класса айограм достали роутер и подставили его вместо диспетчера dp


# Получаем от пользователя /start и отправляем ему в ответ первое сообщение
@router.message(CommandStart())
async def cmd_start(message: Message):
    # Метод реплай это именно ответ на отправленное сообщение, т.е в содержании будет указано первое сообщение, в отличии от ансвер
    await message.reply(
        f"Привет! Я ответил!\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}",
        reply_markup=kb.settings,
    )


# Получаем от пользователя /help и отправляем ему в ответ сообщение инструкцию
@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("это команда /help")


# Получаем от пользователя сообщение и сравниваем с нашим благодаря F.text
@router.message(F.text == "Как дела?")
async def how_are_you(message: Message):
    await message.answer("Спасибо, что спрашиваешь, у меня все отлично!")


# Отправляем пользователю картинку если знаем айти, или загружаем по ссылке отправляем по команде /get_photo
@router.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAMeZynqoXAsfj3obkpdDei3eWiiySAAAizjMRuQBFBJIydt5qMpt-MBAAMCAAN3AAM2BA",
        caption="img",
    )


# Получаем от пользователя изображение
@router.message(F.photo)
async def take_photo(message: Message):
    await message.answer(f"ID фото: {message.photo[-1].file_id}")
