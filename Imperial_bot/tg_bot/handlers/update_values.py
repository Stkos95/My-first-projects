from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tg_bot.databases.database import DataBase
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from tg_bot.FSM.states import UpdateValues


def check_id(db: DataBase, table, check_id):
    id = db.select_one(table=table, what_to_see='id')
    id = [i[0] for i in id]
    return check_id in id


async def chooce_table_update(message: types.Message, state: FSMContext):
    await message.answer('Выбери таблицу:', reply_markup=ReplyKeyboardMarkup([
        [
            KeyboardButton('Months'),
            KeyboardButton('GamesPayments')
        ],
        [
            KeyboardButton('Players')
        ]
    ],
        resize_keyboard=True))

    await UpdateValues.first()



async def update_values(message: types.Message, state: FSMContext):
    table = message.text
    await state.update_data(table=table)
    await message.answer('Укажи id записи, куда вставить данные:', reply_markup=ReplyKeyboardRemove())
    await UpdateValues.next()


async def update_enter_id(message: types.Message, state: FSMContext):
    id = int(message.text)
    db = DataBase()
    datas = await state.get_data()
    table = datas['table']
    print(id)
    print(table)
    if not check_id(db,table=table, check_id=id):
        await message.answer('Некорректный id, укажи другой...')
        return
    await message.answer('Введи данные для добавления:')
    await state.update_data(id=id)
    await UpdateValues.value.set()



async def entering_values(message: types.Message, state: FSMContext):
    db = DataBase()
    data = await state.get_data()
    id = data['id']
    table = data['table']
    value = message.text
    db.update(table, value, id)
    await message.answer('Данные обновлены!')
    await state.finish()


async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Отменено!')

def register_update(dp: Dispatcher):
    dp.register_message_handler(chooce_table_update, commands='update', is_admin=True)
    dp.register_message_handler(update_values, state=UpdateValues.table)
    dp.register_message_handler(update_enter_id, state=UpdateValues.id)
    dp.register_message_handler(entering_values, state=UpdateValues.value)




