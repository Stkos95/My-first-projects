from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tg_bot.databases.database import DataBase
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
kb_remove = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text='Готово')
                ]
            ],
            resize_keyboard=True

        )

async def remove_month(message: types.Message, state: FSMContext):
    await message.answer('Удаление месячной оплаты, укажи <b>id</b> записи.\nПосле окончания ввода нажми "Готово"', reply_markup=kb_remove)
    await state.set_state('remove')  # поменять и сделать нормальный стэйт
    db = DataBase()

    await state.update_data(db=db, table='Months')




async def remove_player(message: types.Message, state: FSMContext):
    await message.answer('Удаление игрока, укажи его <b>id</b>.\nПосле окончания ввода нажми "Готово"', reply_markup=kb_remove)
    await state.set_state('remove')  # поменять и сделать нормальный стэйт
    db = DataBase()
    await state.update_data(db=db, table='Players')


async def remove_game_payment(message: types.Message, state: FSMContext):
    await message.answer('Удаление платы за игру, укажи <b>id</b> записи.\nПосле окончания ввода нажми "Готово"', reply_markup=kb_remove)
    await state.set_state('remove')  # поменять и сделать нормальный стэйт
    db = DataBase()
    await state.update_data(db=db, table='GamesPayments')



async def remove_game(message: types.Message, state: FSMContext):
    await message.answer('Удаление игры из списка, укажи <b>id</b> записи.\nПосле окончания ввода нажми "Готово"', reply_markup=kb_remove)
    await state.set_state('remove')  # поменять и сделать нормальный стэйт
    db = DataBase()
    await state.update_data(db=db, table='Games')

async def remove_confirm(message: types.Message, state: FSMContext):
    id = message.text

    async with state.proxy() as data:
        table = data['table']
        data['db'].remove(table,id)
    await message.answer(f'Запись успешно удалена!')


def register_remove(dp: Dispatcher):
    dp.register_message_handler(remove_month, commands='remove_month', is_admin=True)
    dp.register_message_handler(remove_game_payment, commands='remove_game_pay', is_admin=True)
    dp.register_message_handler(remove_game, commands='remove_game', is_admin=True)
    dp.register_message_handler(remove_player, commands='remove_player', is_admin=True)
    dp.register_message_handler(remove_confirm, state='remove')
