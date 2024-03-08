from aiogram import Dispatcher, Bot
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import token

bot = Bot(token=token, parse_mode=ParseMode.HTML)
storage = MemoryStorage()


dp = Dispatcher(bot, storage=storage)
