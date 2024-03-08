import asyncio
import logging
from tg_bot.config import load_config
from aiogram import Bot
from tg_bot.commands import set_commands
from tg_bot.filters.admin import AdminCheck
from tg_bot.handlers.players_handlers import register
from tg_bot.handlers.update_values import register_update
from tg_bot.handlers.remove_handlers import register_remove
from tg_bot.handlers.get_info_handlers import register_info_handlers
from tg_bot.handlers.add_records_handlers import register_records
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram import Dispatcher

logger = logging.getLogger(__name__)


def register_all_filters(dp):
    dp.filters_factory.bind(AdminCheck)


def register_all_handlers(dp):
    register(dp)
    register_info_handlers(dp)
    register_records(dp)
    register_remove(dp)
    register_update(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s'
    )
    config = load_config()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    bot['config'] = config
    register_all_filters(dp)
    register_all_handlers(dp)
    await set_commands(bot)

    try:
        await dp.start_polling()
    finally:
        await bot.get_session()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):

        logger.error("Bot stopped")
