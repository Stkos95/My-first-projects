from loader import dp
from aiogram.dispatcher.filters.state import StatesGroup, State

class Weather_current(StatesGroup):
    Q1 = State()

class Weather_forecast(StatesGroup):
    F1 = State()
    F2 = State()



class QuizGame(StatesGroup):
    quiz_1 = State()

