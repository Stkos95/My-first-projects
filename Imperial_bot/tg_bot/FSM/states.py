from aiogram.dispatcher.filters.state import StatesGroup, State


class add_month_states(StatesGroup):
    S_1 = State()
    S_2 = State()


class UpdateValues(StatesGroup):
    table = State()
    id = State()
    value = State()