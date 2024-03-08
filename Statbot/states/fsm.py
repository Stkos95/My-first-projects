from aiogram.dispatcher.filters.state import StatesGroup, State


# class SummaryStates(StatesGroup):
#     Zero_state = State()
#     First_state = State()
#     Second_state = State()

class SummaryStates(StatesGroup):
    Team_signs = State()
    First_state = State()
    Second_state = State()
    League_choose = State()
    Third_state = State()


class TeamAnalytic(StatesGroup):
    Zero_state = State()
    First_state = State()
    Second_state = State()

class PersonalStatisticStates(StatesGroup):
    Zero_state = State()
    First_state = State()
    Second_state = State()


class CreateTemplate(StatesGroup):
    League = State()
    Logo_1 = State()
    Second_state = State()

class EditStatistic(StatesGroup):
    Edit_data = State()