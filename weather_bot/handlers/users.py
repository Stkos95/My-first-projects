from loader import dp
from aiogram import types




@dp.message_handler(content_types=types.ContentType.AUDIO)
async def content(message: types.Message):
    await message.answer_audio(audio = message.audio.file_id)