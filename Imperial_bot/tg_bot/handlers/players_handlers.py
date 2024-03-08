from aiogram import types, Dispatcher, Bot
from tg_bot.config import load_config
from aiogram.dispatcher import FSMContext
from tg_bot.commands import set_commands
from tg_bot.databases.database import DataBase, Player
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageTextIsEmpty
import aiogram.utils.markdown as md
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


async def testing_creating(message: types.Message, state: FSMContext):
    db = DataBase('tg_bot/databases/players.db')
    db.create_player_table()
    await message.answer('База создана успешно!')


async def add_player(message: types.Message, state: FSMContext):
    await message.answer(
        'Вы выбрали добавить игрока, введите в формате: <b>Фамилия Имя</b> <i>Комментарий</i>!\nПосле окончания ввода, нажми "Готово"',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text='Готово')
                ]
            ],
            resize_keyboard=True

        ))
    await state.set_state('test_1')  # поменять и сделать нормальный стэйт
    db = DataBase()
    await state.update_data(db=db)


async def add_player_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        db = data['db']
    text = message.text.split()
    print(text)
    if len(text) < 2:

        await message.answer('Некорректное количество данных')
    else:
        names = text[:2]
        try:
            description = ' '.join(text[2:])
            print(f'{description=}')
            db.add_player(*names, description)
        except:

            db.add_player(*names)






async def finish(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Готово!', reply_markup=ReplyKeyboardRemove())



async def watch_all(message: types.Message, state: FSMContext):
    data = DataBase().select_one('Players', ('id, Second_name', 'name', 'description'))

    data = list(map(lambda i: list(map(lambda x: str(x), i)), data))
    print(data)
    players = '\n'.join([f'{player[0]}) <b>{" ".join(player[1:-1])}</b>: {player[-1]}' for player in data])
    try:
        await message.answer(players)
    except MessageTextIsEmpty:

        await message.answer(md.hitalic('Список игроков пуст!'))


async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Отменено!', reply_markup=ReplyKeyboardRemove())

def register(dp: Dispatcher):
    dp.register_message_handler(cancel, commands='cancel', state='*')
    dp.register_message_handler(callback=finish, text='Готово', state='*')
    dp.register_message_handler(callback=testing_creating, commands='players')
    dp.register_message_handler(callback=add_player, commands='add_player')
    # dp.register_message_handler(callback=remove_player, commands='remove_player')
    # dp.register_message_handler(callback=remove_player_1, state='remove_1')
    dp.register_message_handler(callback=add_player_1, state='test_1')
    dp.register_message_handler(callback=watch_all, commands='all_players')
