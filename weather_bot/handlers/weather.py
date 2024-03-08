
from aiogram import types
from loader import dp
import requests
from data.config import API_KEY,link, lang
from FSM import Weather_current, Weather_forecast
from aiogram.dispatcher import FSMContext
from keyboards.inline import weather_choose, times
from keyboards.callbackdatas import time_callback, choose_type
from keyboards.text_buttons import send_geo
import datetime
from data.get_city import get_place
from aiogram.types import ReplyKeyboardRemove
from pprint import pprint

def define_weather(q: str, appid: str = API_KEY,units: str = 'metric', lang: str = lang):
    return requests.get(f'{link}weather', params=locals()).json()

def forecast_weather(exclude: str, lat: str, lon:str, units: str = 'metric', appid: str = API_KEY, lang: str = lang):
    return requests.get(f'{link}onecall', params=locals()).json()




degree_sign = u'\N{DEGREE SIGN}'


@dp.callback_query_handler(text='weather', state=None)
async def choose(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer(text='Что именно интересует?',reply_markup=weather_choose)

@dp.callback_query_handler(choose_type.filter(choose_one='geolocation'), state=None)
async def geo(call: types.CallbackQuery):
    await call.message.answer('Нажмите на кнопку, чтобы передать вашу текущую геолокацию!', reply_markup=send_geo)
    await Weather_current.Q1.set()


@dp.message_handler(content_types=types.ContentType.LOCATION, state=Weather_current.Q1)
async def with_location(message: types.Message, state: FSMContext ):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    try:
        show_weather_one = forecast_weather('minutely,hourly,daily', latitude, longitude)
        text = [f'<b>Информация из One_call_Api</b>',
                f'Текущая температура воздуха: {show_weather_one["current"]["temp"]} {degree_sign}C',
                f'Ощущается как: {show_weather_one["current"]["feels_like"]} {degree_sign}C',
                f'Влажность: {show_weather_one["current"]["humidity"]}%',
                f'Описание погоды: <b>{show_weather_one["current"]["weather"][0]["description"]}</b>']

        await message.answer('\n'.join(text), reply_markup=ReplyKeyboardRemove())
        await state.finish(

        )
    except:
        await message.answer('Попробуйте еще раз, неверное значение =(')
        await state.finish()









@dp.callback_query_handler(choose_type.filter(choose_one='current'), state=None )
@dp.callback_query_handler(choose_type.filter(choose_one='forecast'), state=None )
async def weather_answer(call: types.CallbackQuery, callback_data: dict):
    if callback_data['choose_one'] == 'forecast':
        await Weather_forecast.F1.set()
    elif callback_data['choose_one'] =='current':
        await Weather_current.Q1.set()
    await call.answer()
    await call.message.answer("Укажите город:")





@dp.message_handler(state=Weather_current.Q1)
async def weather_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:

        data['city'] = message.text
        lon = get_place(data['city'])[1]
        lat = get_place(data['city'])[0]
        try:
            show_weather_one = forecast_weather('minutely,hourly,daily',lat,lon)
            text =[f'<b>Информация из One_call_Api</b>',
                    f'Текущая температура воздуха: {show_weather_one["current"]["temp"]} {degree_sign}C',
                    f'Ощущается как: {show_weather_one["current"]["feels_like"]} {degree_sign}C',
                    f'Влажность: {show_weather_one["current"]["humidity"]}%',
                    f'Описание погоды: <b>{show_weather_one["current"]["weather"][0]["description"]}</b>']

            await message.answer('\n'.join(text))
            await state.finish(

            )
        except:
            await message.answer('Попробуйте еще раз, неверное значение =(')
            await state.finish()



@dp.message_handler(state=Weather_forecast.F1)
async def weather_answer(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            place = get_place(message.text)
            data['lat'] = place[0]
            data['lon'] = place[1]

        await message.answer("Прогноз на какой период интересует?:", reply_markup=times)
    except:
        await message.answer(text='Неверное значение, попробуйте еще раз!')
        await state.finish()



@dp.callback_query_handler(time_callback.filter(time='hourly'), state=Weather_forecast.F1)
async def hourly_forecast(call: types.CallbackQuery,state: FSMContext):
    await call.answer()
    async with state.proxy() as data:
        forecast_hour = forecast_weather('minutely,current,daily',data['lat'],data['lon'])
    hours_dict=[]
    pprint(forecast_hour)
    for hour in forecast_hour['hourly']:
        text= f'В {datetime.datetime.fromtimestamp(hour["dt"])} будет {hour["temp"]} градусов,\n' \
              f'ощущается как {hour["feels_like"]},\n' \
              f' в целом будет: {hour["weather"][0]["description"]}'
        while len(hours_dict) < 5:
            hours_dict.append(text)
            break
    try:
        await call.message.answer('\n'.join(hours_dict))
        await state.finish()
    except:
        await call.message.answer("Не удалось получить данные")
        await state.finish()





@dp.callback_query_handler(time_callback.filter(time='daily'), state=Weather_forecast.F1)
async def daily_forecast(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    day_dict =[]
    async with state.proxy() as data:
        forecast_daily = forecast_weather('minutely,hourly,current',data['lat'],data['lon'])
    for day in forecast_daily['daily']:

        text = f' <i>{datetime.datetime.fromtimestamp(day["dt"])}</i>\n' \
               f'будет днем: {day["feels_like"]["day"]} градусов,\n' \
            f'вечером {day["feels_like"]["eve"]} градусов,\n' \
           f'в целом будет: {day["weather"][0]["description"]}\n'
        day_dict.append(text)

    await call.message.answer('\n'.join(day_dict))
    await state.finish()



