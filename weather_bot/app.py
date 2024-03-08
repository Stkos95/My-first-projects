from loader import dp
from aiogram import executor
import handlers
from other.start_end_funcs import start_admin_func


if __name__ =="__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=start_admin_func)