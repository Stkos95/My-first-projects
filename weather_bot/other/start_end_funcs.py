from aiogram import Dispatcher
from data.config import admins



async def start_admin_func(dp: Dispatcher):
    for admin in admins:
        await dp.bot.send_message(chat_id=admin, text="Погодный бот готов к работе!!!")
