from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tg_bot.databases.database import DataBase
from tg_bot.keyboards.inline import get_type, start_info_kb, generate_kb_players, \
    generate_kb_monthly
from tg_bot.commands import set_commands
from tg_bot.keyboards.callbackdatas import get_info_callback, advanced_info_callback

async def test_filter(message: types.Message):
    await message.answer("админ фильтр сработал!")



#handler срабатывает при команде /info и присылает клавиатуру с двумя кнопками: оплата за игру и за месяц.
async def start_info(message: types.Message, state: FSMContext):
    await set_commands(message.bot)
    await message.answer('Выбери какая информация интересует?', reply_markup=start_info_kb)


async def info_month_monthly_0(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer('Какая информация интересует? Выбрано оплата за месяцчную',
                              reply_markup=get_type('Months'))


async def info_month_monthly_1(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer()
    await call.message.answer('выбрана информация по месяцу:')
    db = DataBase()
    match callback_data['detailedby']:
        case 'Months':
            data = db.select_one('Months', 'DISTINCT(month)')
            await call.message.answer("какой месяц?", reply_markup=generate_kb_monthly(data, 'Months'))
        case 'GamesPayments':
            data = db.select_one('Games', 'DISTINCT(game)')
            await call.message.answer("Какая игра?", reply_markup=generate_kb_monthly(data, 'GamesPayments'))



# async def info_month_monthly_2(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
#     await call.answer()
#     goal_of_payment = callback_data['search']
#     db = DataBase()
#     data= []
#     what_to_see = ('id','name', 'second_name', 'summa', 'description')
#     text = f'{goal_of_payment}\n'
#     match callback_data['type']:
#         case 'Months':
#             data = db.select_one('Months', what_to_see=what_to_see, month=goal_of_payment)
#         case 'GamesPayments':
#             data = db.select_one('GamesPayments', what_to_see=what_to_see, game=goal_of_payment)
#     for row in data:
#         id, name, surname, summa, description = row
#         text += f'<i>{id}</i>) {surname} {name} - {summa} ({description})\n' if description else f'<i>{id}</i>) {surname} {name} - {summa}\n'
#     await call.message.answer(text)


async def info_month_monthly_2(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer()
    goal_of_payment = callback_data['search']
    print(call.data)
    db = DataBase()
    data= []
    what_to_see = ('id','name', 'second_name', 'summa', 'description')
    text = f'{goal_of_payment}\n'
    match callback_data['type']:
        case 'Months':
            data = db.show_month_info(goal_of_payment)
            print(data)
        case 'GamesPayments':
            data = db.select_one('GamesPayments', what_to_see=what_to_see, game=goal_of_payment)

    for i in data.list_of_records:
        text += f'{i.name} {i.surname} - {i.price} ✅ {i.description if i.description else ""}\n'

    for i in data.players_who_didnt_paid:
        text += f'{i.name} {i.surname} ❌\n'

    # for row in data:
    #     id, name, surname, summa, description = row
    #     text += f'<i>{id}</i>) {surname} {name} - {summa} ({description})\n' if description else f'<i>{id}</i>) {surname} {name} - {summa}\n'
    await call.message.answer(text)



async def info_general_player_0(call: types.CallbackQuery, callback_data: dict):
    await call.answer()
    await call.message.answer('выбрана информация по игроку:')
    chooce = callback_data['detailedby']
    db = DataBase()
    data = db.select_one(chooce, "DISTINCT second_name, name")
    await call.message.answer(text="выбери игрока:", reply_markup=generate_kb_players(data, f'{chooce}'))




async def info_general_player_1(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    chooce = callback_data['type']
    await call.answer()
    surname, name = callback_data['search'].split()
    data = []
    db = DataBase()
    match chooce:
        case 'Months':

            data = db.select_one('Months', ('id','month', 'summa', 'description'), name=name, second_name=surname)

        case 'GamesPayments':
            data = db.select_one('GamesPayments', ('id','game', 'summa', 'description'), name=name, second_name=surname)
    text = f'{surname} {name}\n'
    for row in data:
        id, month, summa, description = row
        text += f'<i>{id}</i>) {month} - {summa} ({description})\n' if description else f'<i>{id}</i>) {month} - {summa}\n'
    await call.message.answer(text)
    await state.finish()



async def info_game_0(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer('Какая информация интересует?Выбрано оплата за игру',
                              reply_markup=get_type('GamesPayments', val1='По играм'))





def register_info_handlers(dp: Dispatcher):
    dp.register_message_handler(start_info,is_admin=True, commands='info')
    dp.register_callback_query_handler(info_month_monthly_0, text='payment_per_month')
    dp.register_callback_query_handler(info_month_monthly_1,
                                       get_info_callback.filter(type='bymonths'))
    dp.register_callback_query_handler(info_month_monthly_2,
                                       advanced_info_callback.filter(bywhat='month'))
    dp.register_callback_query_handler(info_general_player_0,
                                       get_info_callback.filter(type='byplayers'))
    dp.register_callback_query_handler(info_general_player_1, advanced_info_callback.filter(bywhat='player'))
    dp.register_callback_query_handler(info_game_0, text='payment_per_game')
