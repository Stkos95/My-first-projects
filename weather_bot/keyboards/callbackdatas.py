from aiogram.utils.callback_data import CallbackData


time_callback = CallbackData('type', 'time')

choose_type = CallbackData('type_weather', 'choose_one')

task_callback =CallbackData("buy", "id_item")
like_callback = CallbackData("rate", "marks")