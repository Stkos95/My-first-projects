from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.callbackdatas import task_callback, like_callback
task_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купить товар",callback_data=task_callback.new(id_item='321'))
    ],
    [
        InlineKeyboardButton(text="👍", callback_data=like_callback.new(marks="1")),
        InlineKeyboardButton(text="👎", callback_data=like_callback.new(marks=-1))
    ],
    [
        InlineKeyboardButton(text='Поделиться с другом',switch_inline_query='321')
    ]
])