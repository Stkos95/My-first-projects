from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tg_bot.keyboards.callbackdatas import get_info_callback, advanced_info_callback, start_records_callback, game_payments_callback



start_info_kb = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    [
        InlineKeyboardButton(text='Месячная оплата', callback_data='payment_per_month')
    ],
    [
        InlineKeyboardButton(text='Оплата за игры', callback_data='payment_per_game')
    ]])



def get_type(flag, val1='По месяцам', val2='По игрокам'):
    get_typekb = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
        [
            InlineKeyboardButton(text=val1, callback_data=get_info_callback.new(type='bymonths', detailedby=flag))
        ],
        [
            InlineKeyboardButton(text=val2, callback_data=get_info_callback.new(type='byplayers', detailedby=flag))
        ]])
    return get_typekb







def generate_kb_players(data, what_type):
    kb = InlineKeyboardMarkup(row_width=3)
    if data:
        for i in data:
            surname, name = i
            kb.insert(InlineKeyboardButton(text=f'{surname} {name}',
                                           callback_data=advanced_info_callback.new(search=f'{surname} {name}',
                                                                                    bywhat='player',
                                                                                    type=what_type)))
    return kb

def generate_kb_monthly(data, what_type):
    kb = InlineKeyboardMarkup(row_width=3)
    if data:
        for i in data:
            kb.insert(InlineKeyboardButton(text=i[0],
                                           callback_data=advanced_info_callback.new(search=f'{i[0]}',
                                                                                    bywhat='month',
                                                                                    type=what_type)))
    return kb








def generate_kb_game_payments(data):
    kb = InlineKeyboardMarkup()
    if data:
        for i in data:
            kb.insert(InlineKeyboardButton(text=i[0], callback_data=game_payments_callback.new(match=i[0])))
    return kb




start_records_bk = InlineKeyboardMarkup(row_width=5, inline_keyboard=[
    [
        InlineKeyboardButton(text='Оплата за игру', callback_data=start_records_callback.new(add='game')),
        InlineKeyboardButton(text='Оплата за месяц', callback_data=start_records_callback.new(add='month'))
    ],
    [
        InlineKeyboardButton(text='Создать сбор по игре', callback_data=start_records_callback.new(add='create_game'))
    ]
])
