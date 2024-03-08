from environs import Env
import json
import requests

env=Env()
env.read_env()

token=env.str('TOKEN')
admins=env.list('ADMINS')


'''Для погоды'''
API_KEY =env.str("API_TOKEN")
link = f'http://api.openweathermap.org/data/2.5/'
lang = 'ru'
link_city='http://api.openweathermap.org/geo/1.0/direct'

'''Для викторины'''
# token_quiz=env.str('TOKEN_QUIZ')
link_quiz=env.str("LINK_QUIZ")


# link_token=env.str('TOKEN_LINK')
# request = requests.get(url=link_quiz).json()
# token_quiz = request['token']
link_token ='https://opentdb.com/api_token.php?command=request'
