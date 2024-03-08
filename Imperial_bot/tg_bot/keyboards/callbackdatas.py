from aiogram.utils.callback_data import CallbackData


get_info_callback = CallbackData('information', 'type', 'detailedby')
advanced_info_callback = CallbackData('kind','bywhat', 'search', 'type')

start_records_callback = CallbackData('type', 'add')
game_payments_callback = CallbackData('game', 'match')
