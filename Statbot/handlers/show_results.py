from aiogram import types
from loader import dp
from processing.count_statistic_after_match import operating_func
from keyboards.kb_fabric import statistic_callback
from keyboards.kb_fabric import chooce_type_callback
from list_of_actions import act
from keyboards.reply import leagues, templates
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from states import SummaryStates
from processing.transfer_result import transfer_results
from aiogram.dispatcher import FSMContext
from misc.image_process.test import TextToImage
from config import admin
import datetime
from datas import ALIGN
import os
from io import BytesIO

from misc.funcs import get_data_from_db
from handlers.statistic import ready_1_1
from states.fsm import EditStatistic


@dp.message_handler(commands='edit')
async def get_data_from_db_start(message: types.Message, state: FSMContext):
    datas = get_data_from_db()
    # answer = '\n----------------------\n'.join(f'{data.id}) {data.name}' for data in datas)
    answer = '\n----------------------\n'.join(f'{data[0]}) {data[1]}' for data in datas[-5:])
    await message.answer(answer)
    await state.update_data(datas=datas)
    await EditStatistic.Edit_data.set()
    # await ready_1_1(message, state)

@dp.message_handler(state=EditStatistic.Edit_data)
async def get_data_from_db_start(message: types.Message, state: FSMContext):
    num = int(message.text)
    async with state.proxy() as data:
        my_data = data['datas'][num-1]
        data['datas'] = my_data
    await ready_1_1(message, state)


