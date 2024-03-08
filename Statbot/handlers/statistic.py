from aiogram import types
from loader import dp
from processing.count_statistic_after_match import operating_func
from keyboards.kb_fabric import statistic_callback
from keyboards.kb_fabric import chooce_type_callback
from list_of_actions import act
from keyboards.reply import leagues, templates
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from states import SummaryStates
from processing.transfer_result import transfer_results, transfer_results_short_template
from aiogram.dispatcher import FSMContext
from misc.image_process.test import TextToImage
from config import admin
import datetime
from datas import ALIGN
import os
from io import BytesIO
from misc.funcs import add_data_to_db


# ALIGN = (2,2,2,2,1,2,1)
def kb_1_summary(datas, what_half = 1):
    key_1 = InlineKeyboardMarkup(row_width=3)

    b = [InlineKeyboardButton(text=f"{key} ({value})",
                                 callback_data=statistic_callback.new(action=key, team=what_half)) for key, value in datas.items()]
    start = 0
    if not ALIGN:
        key_1.add(*b)
    else:
        for i in ALIGN:
            # key_1.row(*b[start : start + i])
            start += i
    
    return key_1




# @dp.callback_query_handler(chooce_type_callback.filter(type='summary'))
# async def description(call: types.CallbackQuery, state: FSMContext):
#     await call.answer()
#     await call.message.answer('Выбери лигу!', reply_markup=leagues)



@dp.callback_query_handler(chooce_type_callback.filter(type='summary'))
async def description(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer('Укажи играющие команды через дефис, пример: Команда 1 - Команда 2:', reply_markup=types.ReplyKeyboardRemove())

    await SummaryStates.First_state.set()
    # await SummaryStates.Team_signs.set()



@dp.callback_query_handler(statistic_callback.filter(team="1"),
                           state=[SummaryStates.First_state, SummaryStates.Second_state])
async def count_statistic_1(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    value = callback_data['action']


    async with state.proxy() as data:
        operating_func(data=data['Команда 1'], value=value)
        await call.message.edit_reply_markup(reply_markup=kb_1_summary(data['Команда 1']))
    await call.answer("work")


@dp.callback_query_handler(statistic_callback.filter(team="2"),
                           state=[SummaryStates.First_state, SummaryStates.Second_state])
async def count_statistic_2(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    value = callback_data['action']
    async with state.proxy() as data:
        operating_func(data=data['Команда 2'], value=value)
        await call.message.edit_reply_markup(reply_markup=kb_1_summary(data['Команда 2'], 2))
    await call.answer("work")


@dp.message_handler(text="Второй", state=SummaryStates.First_state)
async def second_half(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data["result_1"] = {
            '1': data['Команда 1'],
            '2': data['Команда 2']
        }
        data['Команда 1'] = act()
        data['Команда 2'] = act()
        await message.answer("Второй тайм!", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Готово')]], resize_keyboard=True))
        await message.answer("Первая команда:",
                             reply_markup=kb_1_summary(data['Команда 1']))
        await message.answer("Вторая команда:", reply_markup=kb_1_summary(data['Команда 2'], 2))

        await SummaryStates.Second_state.set()


#сделать чтобы был выбор лиги, а затем поиск в соответствующей папке согласно лиге.
def get_templates(dir_path):
    d = os.listdir(f"/home/konstantin/my_python/PycharmProjects/Statbot/templates/{dir_path}")
    return d

@dp.message_handler(text="Готово", state=SummaryStates.Second_state)
async def ready(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        first_half_result = data["result_1"]
        second_half_result = {
            '1': data['Команда 1'],
            '2': data['Команда 2']
        }
        result = {
                '1_half': first_half_result,
                '2_half': second_half_result
            }
    add_data_to_db(result)
    # #     first_half_result = data["result_1"]
    # #     second_half_result = {
    # #         '1': data['Команда 1'],
    # #         '2': data['Команда 2']
    # #     }
    # #     result = {
    # #             '1_half': transfer_results_short_template(first_half_result),
    # #             '2_half': transfer_results_short_template(second_half_result)
    # #         }
    # # add_data_to_db(result)
    await message.answer('Выбери как делать шаблон:', reply_markup=templates)



@dp.message_handler(text='Готовый шаблон', state='*')
async def ready_1_1(message: types.Message, state: FSMContext):
    await message.answer('Выбери лигу:', reply_markup=leagues)
    await SummaryStates.League_choose.set()



@dp.callback_query_handler(state=SummaryStates.League_choose)
async def ready_1(call: types.CallbackQuery, state: FSMContext):
    dir_path = call.data.strip()

    templates = get_templates(f'frames/{dir_path}')
    z = [f'{ind + 1}) {template}' for ind, template in enumerate(templates)]
    await state.update_data(templates=templates)
    answer = '\n'.join(z)
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(1, len(z)+1):
        kb.add(KeyboardButton(text=i))
    await call.message.answer(answer, reply_markup=kb)

    # await message.answer('Введи название файла:')
    await SummaryStates.Third_state.set()


@dp.message_handler(state=SummaryStates.Third_state)
async def template_chocen(message: types.Message, state: FSMContext):
    number = int(message.text)
    async with state.proxy() as data:
        template = data['templates'][number - 1]
        new_data = data.get('datas')
        if new_data:
            new_data = new_data[1]
            first_half_result = new_data["1_half"]
            second_half_result = new_data['2_half']
        else:
            first_half_result = data["result_1"]
            second_half_result = {
            '1': data['Команда 1'],
            '2': data['Команда 2']
        }
            result = {
                '1_half': first_half_result,
                '2_half': second_half_result
            }
            # add_data_to_db(result)

        new_list = []
        for half in (first_half_result, second_half_result):
            t = tuple(half[i][j] for i in half for j in half[i] if 'гол' in j.lower())
            new_list.append(t)
        
        # score = {
        #     '1_half': new_list[0],
        #     'result': final_score
        # }
    first_half_score = new_list[0]
    final_score = tuple(map(sum, zip(*new_list)))



    data_first_half = transfer_results(first_half_result)
    data_second_half = transfer_results(second_half_result)
    image = TextToImage(picture=f'templates/frames/league5x5/{template}')
    image.draw_statistic_results(data_first_half, what_half=1)
    image.draw_statistic_results(data_second_half, what_half=2)
    image.draw_final_result(final_score)
    image.draw_first_half_result(first_half_score)
    
    # user_id = int(message.from_user.id)



    timer = str(datetime.datetime.now())
    print(timer)
    image.show()
    save_to = BytesIO()
    image.save(save_to)
    save_to.seek(0)
    await message.answer_document(types.InputFile(save_to, filename=f'{timer}.png'))

    # image.save(f'/home/konstantin/my_python/PycharmProjects/Statbot/results_statistic_png/{timer}.png')
    await state.finish()




@dp.message_handler(text='Отмена' ,state='*')
async def cancel(message: types.Message, state: FSMContext):
    await message.answer("Отменено!")
    await state.finish()

@dp.message_handler(state=SummaryStates.First_state)
async def request_statistic(message: types.Message, state: FSMContext):
    try:
        team_1, team_2 = map(str.strip,message.text.split('-'))
    except:
        team_1, team_2 = "Команда 1", "Команда 2"
    async with state.proxy() as data:
        data['team_1_name'] = team_1
        data['team_2_name'] = team_2
        data['Команда 1'] = act()
        data['Команда 2'] = act()
        print(data['Команда 2'])
        print(type(data['Команда 2']))
        await message.answer(message.text)
        await message.answer("Выбрана послематчевая статистика!")
        await message.answer(f"<b>{team_1}</b>:",
                                  reply_markup=kb_1_summary(data['Команда 1']))
        await message.answer(f"<b>{team_2}</b>:", reply_markup=kb_1_summary(data['Команда 2'], 2))
    await message.answer(text="Когда закончишь первый тайм, нажми на клавиатуре 'Второй', чтобы появилась клавиатура для второго тайма",
                              reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text="Второй")))



