from aiogram.dispatcher.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp
from aiogram import types

@dp.inline_handler(text="Привет")
async def hello_query(query: types.InlineQuery):
    await query.answer(
        results=[],
    switch_pm_text="hello_its_me",
    switch_pm_parameter="hello")


@dp.inline_handler(text="Кот")
async def cats(query: types.InlineQuery):
    await query.answer(results=[
        types.InlineQueryResultArticle(
            id="4",
            title="Общая информация о котах",
            input_message_content=types.InputTextMessageContent(
                message_text="https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%88%D0%BA%D0%B0"

            ),
            url="https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%88%D0%BA%D0%B0",

            thumb_url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Cat_eyes_2007-1.jpg/1200px-Cat_eyes_2007-1.jpg"

        ),
        types.InlineQueryResultVideo(
            id="10",
            title="Видео о котах",
            video_url="https://www.youtube.com/watch?v=V7SrzqGdNmI",
            mime_type='video/mp4',
            caption="Смешное видео о котах!",
            description="Смешное видео о котах.",
            thumb_url="https://img1.goodfon.ru/original/3200x1200/4/3c/kot-ryzhiy-ushi-vzglyad-poloski.jpg"

        )
    ])


@dp.message_handler(CommandStart(deep_link="hello"))
async def start_deep(message: types.Message):
    await message.answer("И тебе привет",reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Переходи сюда!!!", switch_inline_query='Dog')
        ]
    ]
    ))


# @dp.inline_handler(text="")
# async def empty_query(query: types.InlineQuery):
#     await query.answer(results=[
#         types.InlineQueryResultArticle(
#             id='1',
#             title="Привет, введи что-нибудь",
#             input_message_content=types.InputTextMessageContent(
#                 message_text="не обязательно жать на кнопку"
#             )
#         )
#     ]
#     )


