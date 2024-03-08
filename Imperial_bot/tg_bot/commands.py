from aiogram import types, Bot


async def set_commands(bot: Bot):
    commands = [types.BotCommand(command='add', description='Добавление оплаты'),
                types.BotCommand(command='add_player', description='добавление игрока в команду'),
                types.BotCommand(command='all_players', description='Посмотреть список игроков'),
                types.BotCommand(command='info', description='Посмотреть информацию по оплате'),
                types.BotCommand(command='update', description='Добавить комментарий к существующей записи'),
                types.BotCommand(command='remove_month', description='Удалить запись по месячной оплате'),
                types.BotCommand(command='remove_game', description='Удалить запись по оплате за игру'),
                types.BotCommand(command='remove_game_pay', description='Удалить игру из списка'),
                types.BotCommand(command='remove_player', description='Удалить игрока из команды'),
                types.BotCommand(command='cancel', description='Отмена действия')

                ]
    await bot.set_my_commands(commands=commands)

