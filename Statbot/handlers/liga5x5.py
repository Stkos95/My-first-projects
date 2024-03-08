from aiogram import types
from loader import dp



@dp.callback_query_handler(chooce_type_callback.filter(type='summary'))
async def description(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer('Укажи опознавательные знаки для обоих команд:')

    await SummaryStates.First_state.set()
    # await SummaryStates.Team_signs.set()




    async with state.proxy() as data:
