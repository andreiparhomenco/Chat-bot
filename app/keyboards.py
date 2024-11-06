from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

# создаем кнопки клавитуры с помошью реплай кейборд
# Меняем размер клавиатуры до минимального значения
# текст вместо  подсказки значения(write a message)
main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Первокурсникам"), KeyboardButton(text="Режим работы")],
        [KeyboardButton(text="Получить читательский")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню",
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
