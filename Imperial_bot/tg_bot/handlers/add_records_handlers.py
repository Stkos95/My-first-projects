from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tg_bot.databases.database import DataBase
from tg_bot.keyboards.inline import start_records_bk, generate_kb_game_payments
from tg_bot.keyboards.callbackdatas import start_records_callback, game_payments_callback
from tg_bot.FSM import add_month_states


# Оплатил месяц Май Грачев Илья 500 (описание, если есть)

async def add_records_start(message: types.Message):
    await message.answer('что добавить?', reply_markup=start_records_bk)

async def add_record_month(call: types.CallbackQuery, state: FSMContext, callback_data:dict):
    await call.answer()
    await call.message.answer("Укажи в формате : Месяц Фамилия Имя Сумма, Комментарий (если необходимо) КОММЕНТАРИЙ ОТДЕЛИТЬ ЗАПЯТОЙ!!!!!!!")
    await add_month_states.first()


async def add_record_month_1(message: types.Message, state: FSMContext):
    month, second_name, name, summa, *description = message.text.split()
    description = '-' if not description else ' '.join(description)
    db = DataBase()
    db.add_record_month(month, second_name, name, summa, description )
    await message.answer('запись в бд успешно сделана')
    await state.finish()

async def create_game(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer('Укажи название игры и описание через запятую, если нужно')
    await state.set_state('create')

async def create_game_1(message: types.Message, state: FSMContext):
    mes = message.text.split(',')
    game = mes[0].strip()
    try:
        description = mes[1]
    except:
        description = '-'

    db = DataBase()
    db.create_game(game, description)
    await message.answer('запись в бд успешно сделана')
    await state.finish()


async def add_game_payment(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer()
    db = DataBase()
    data = db.select_one('Games', 'game')
    await call.message.answer('Оплата за какую игру?', reply_markup=generate_kb_game_payments(data))



async def add_game_payment_1(call: types.CallbackQuery, state:FSMContext, callback_data: dict):
    game = callback_data['match']
    async with state.proxy() as data:
        data['game'] = game
    await call.message.answer(f'Выбрана оплата за игру {game}\nВведи данные в формате Фамилия Имя сумма, описание')
    await state.set_state('payment_game')

async def add_game_payment_2(message: types.Message, state: FSMContext):
    second_name, name, summa, *description = message.text.split()
    description = '-' if not description else description

    db = DataBase()
    async with state.proxy() as data:
        match = data['game']
    db.add_record_game(match ,second_name, name, summa, description)
    await message.answer('Запись создана успешно!')
    await state.finish()




def register_records(dp: Dispatcher):
    dp.register_message_handler(add_records_start, is_admin=True, commands='add' )
    dp.register_callback_query_handler(add_record_month, start_records_callback.filter(add='month'))
    dp.register_message_handler(add_record_month_1, state=add_month_states.S_1)
    dp.register_callback_query_handler(create_game, start_records_callback.filter(add='create_game'))
    dp.register_message_handler(create_game_1, state='create', is_admin=True)
    dp.register_callback_query_handler(add_game_payment, start_records_callback.filter(add='game'))
    dp.register_callback_query_handler(add_game_payment_1, game_payments_callback.filter())
    dp.register_message_handler(add_game_payment_2, state='payment_game')