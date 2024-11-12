from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

# Ипортируем билдер, который может подставлять значения в клавиатуру, переданные из вне, или предопределенные
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


# создаем кнопки клавитуры с помошью реплай кейборд
# resize_keyboard=True Меняем размер клавиатуры до минимального значения
# input_field_placeholder вместо  подсказки значения(write a message)
# main = ReplyKeyboardMarkup(
#    keyboard=[
#       [KeyboardButton(text="Первокурсникам"), KeyboardButton(text="Режим работы")],
#       [KeyboardButton(text="Получить читательский")],
#   ],
#   resize_keyboard=True,
#   input_field_placeholder="Выберите пункт меню",
# )

main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Первокурсникам", callback_data="firstcourse")],
        [
            InlineKeyboardButton(text="Режим работы", callback_data="worktime"),
            InlineKeyboardButton(
                text="Получить читательский", callback_data="get_reader_cart"
            ),
        ],
    ]
)

settings = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Зарегистрироваться",
                url="https://forms.yandex.ru/u/64337fae02848f1e65e96c3c/",
            )
        ]
    ]
)

# значения билдера
roles = ["Сотрудник ТГУ", "Студент ТГУ", "Сторонний пользователь"]


async def Reply_roles():
    keyboard = ReplyKeyboardBuilder()
    for role in roles:
        keyboard.add(KeyboardButton(text=role))
    return keyboard.adjust(2).as_markup()


async def Inline_roles():
    keyboard = InlineKeyboardBuilder()
    for role in roles:
        keyboard.add(InlineKeyboardButton(text=role, callback_data=f"role_{role}"))
    return keyboard.adjust(2).as_markup()


# as_markup use always
