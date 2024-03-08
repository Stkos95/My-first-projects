from aiogram import types
from loader import dp
from processing.count_statistic_after_match import operating_func
from keyboards.kb_fabric import statistic_callback
from keyboards.kb_fabric import chooce_type_callback
from list_of_actions import act
from keyboards.reply import leagues, templates
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from states.fsm import CreateTemplate
from processing.transfer_result import transfer_results
from aiogram.dispatcher import FSMContext
from misc.image_process.test import TextToImage
from config import admin
import datetime
from datas import ALIGN
import os
from io import BytesIO
from misc.funcs import get_templates




@dp.message_handler(commands='create_template')
async def create_template_start(message: types.Message, state: FSMContext):
    await message.answer('Выбери заготовку:')
    templates = get_templates('raw_templates/')
    answer = '\n'.join(f'{ind + 1}) {temp}' for ind, temp in enumerate(templates))
    await state.update_data(templates=templates)
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(1, len(templates) + 1):
        kb.add(KeyboardButton(text=str(i)))
    await message.answer(answer, reply_markup=kb)
    await CreateTemplate.League.set()


@dp.message_handler(state=CreateTemplate.League)
async def chooce_number_template(message: types.Message, state: FSMContext):
    number = int(message.text)
    async with state.proxy() as data:
        template = data['templates'][number - 1]
        print(template)
    await state.update_data(template=f'/home/konstantin/my_python/PycharmProjects/Statbot/templates/raw_templates/{template}')
    await message.answer('Пришлите Логотип для 1 команды:')
    await CreateTemplate.Logo_1.set()



# Сделать 2 типа данных: документ и текст, если текст, то выбирать из папки...
@dp.message_handler(state=CreateTemplate.League, content_type=types.Document)
async def logo_team_1(message: types.Message, state: FSMContext):
    document = message.document
