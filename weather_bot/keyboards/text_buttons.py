from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


send_geo = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='Узнать геопозицию', request_location=True )
        ]
    ],resize_keyboard=True
)