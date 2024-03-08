from aiogram import types
from loader import dp
from keyboards.task4_kb import task_kb
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.callbackdatas import task_callback, like_callback

list_items = {
    "1":"https://domstrousam.ru/wp-content/uploads/2021/02/mandarin_gorchit.jpg",
    "2": "https://fb.ru/media/i/6/5/3/2/0/2/i/653202.jpg"
}
rate = 0
@dp.message_handler(commands="items")
async def start_items(message: types.Message):
    for key, value in list_items.items():
        await message.answer_photo(photo=value, reply_markup=InlineKeyboardMarkup(row_width=2,inline_keyboard=[
          [
              InlineKeyboardButton(text=f"Купить товар. id - {key}", callback_data=task_callback.new(id_item=key))
          ],
            [
                InlineKeyboardButton(text="👍", callback_data=like_callback.new(marks=1)),
                InlineKeyboardButton(text="👎", callback_data=like_callback.new(marks=-1))
            ],
            [
                InlineKeyboardButton(text='Поделиться с другом', switch_inline_query=key)
            ]
        ]
                                                                                  )
                                   )

@dp.callback_query_handler(task_callback.filter())
async def del_kb(call: types.CallbackQuery, callback_data: dict):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.edit_caption(caption=f'Покупай товар номер {callback_data["id_item"]}')



@dp.callback_query_handler(like_callback.filter(marks="1"))
async def like(call: types.CallbackQuery, callback_data: dict):
    rate = int(callback_data["marks"])
    await call.answer(text =f'Тебе понравился этот товар')


@dp.callback_query_handler(like_callback.filter(marks="-1"))
async def like(call: types.CallbackQuery, callback_data: dict):
    rate = int(callback_data["marks"])
    await call.answer(text =f'Тебе не понравился этот товар')