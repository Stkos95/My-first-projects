from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.callbackdatas import time_callback, choose_type

weather = InlineKeyboardMarkup(row_width=2)


weather.add(InlineKeyboardButton(
    text='Узнать погоду',
    callback_data='weather'),
    InlineKeyboardButton(
        text='Игра в викторину',
        callback_data='quiz'
    )
)


weather_choose = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text = 'Узнать текущую погоду',
                                                                   callback_data=choose_type.new(choose_one='current')),

                                              InlineKeyboardButton(text='Узнать прогноз', callback_data=choose_type.new(choose_one='forecast'))
                                          ],
                                          [
                                              InlineKeyboardButton(text='Узнать погоду по геолокации',
                                                                   callback_data=choose_type.new(choose_one='geolocation'))
                                          ]

                                      ]
                                      )



times = InlineKeyboardMarkup(row_width=2,
                             inline_keyboard=[
    [
        InlineKeyboardButton(text='На день(почасовой)',
                             callback_data=time_callback.new(time='hourly')),
        InlineKeyboardButton(text='На неделю',
                             callback_data=time_callback.new(time='daily'))

    ]
]
)
