from loader import dp
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp
from aiogram import types
from keyboards.inline import weather


@dp.message_handler(CommandStart())
async def start_func(message: types.Message):
    await message.answer(text=f'Приветствую тебя, {message.from_user.first_name}!!!\n'
                              f'Чтобы получить список доступных команд выбери команду /help '
                              f'или выбери возможности бота', reply_markup=weather)



@dp.message_handler(CommandHelp())
async def help_func(message: types.Message):
    await message.answer('сейчас помогу')

#
# @dp.message_handler()
# async def help_func(message: types.Message):
#     await message.answer(message.text)
