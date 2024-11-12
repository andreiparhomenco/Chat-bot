from aiogram import (
    F,
    Router,
)  # Импортирую бота, диспетчера, Ф-магический фильтр, благоря нему можно получать любые сообщения от пользователя.
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

# импортировали все из файла кейборд
import app.keyboards as kb

# из файла миддлваре импортируем нашу функцию тестмидлваре
from app.middlewares import TestMiddleware

# из класса айограм достали роутер и подставили его вместо диспетчера dp
router = Router()
# роутер для обработки мидлваре
router.message.middleware(TestMiddleware())

# из айограм импортировали состояния
from aiogram.fsm.state import StatesGroup, State

# Импортируем контекст нужен для управления состояниями
from aiogram.fsm.context import FSMContext


# Сделали класс рег в котором будут храниться наши состояния
class Reg(StatesGroup):
    name = State()
    number = State()


# Получаем от пользователя /start и отправляем ему в ответ первое сообщение
# Метод реплай это именно ответ на отправленное сообщение, т.е в содержании будет указано первое сообщение, в отличии от ансвер
@router.message(CommandStart())
async def cmd_start(message: Message):

    await message.reply(
        f"Привет! Я ответил!\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}",
        reply_markup=kb.main,
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


# Получаем callback от кейбордс
@router.callback_query(F.data == "firstcourse")
async def firstcourse(callback: CallbackQuery):
    await callback.answer("Вы выбрали первокурсникам", show_alert=True)
    await callback.message.edit_text(
        "Погрузим тебя в атмосферу библиотеки в твои первые дни учебы",
        reply_markup=await kb.Inline_roles(),
    )


# Делаем роутер для фиксации регистрации через состояния, шаг первый запрашиваем при регистрации имя
@router.message(Command("reg"))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer("Vvedite imya")


# Делаем шаг второй сохраняем имя и запрашиваем номер
@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer("Введите номер телефона")


# Делаем шаг третий записываем в переменную дата информацию из переменных и показываем пользователю, отчистили состояния
@router.message(Reg.number)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(
        f"thank, register is done \n Имя: {data['name']}\n Номер:{data['number']}"
    )
    await state.clear()
