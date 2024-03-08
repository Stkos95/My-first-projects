import requests
import json
from typing import NamedTuple
from tg_bot.misc.joinfootball_api.query_statements import QUERY_ALL_PLAYERS
# Файл используется для нахождения дублей игроков на сайте.


headers = {
'Api-Key': 'jn46S5a8AJ3A4EJrek5aTRpepngErQtGEdCkD6dYd8gJJmvzhcLmryd1an6JnhTg'
}


file_to_save = NamedTuple('file_to_save', men='men_doubles.txt', women='women_doubles.txt')

query = QUERY_ALL_PLAYERS

r = requests.post(url='https://api.joinsport.io/graphql', headers=headers, json={'query': query})

players = json.loads(r.text)

players = players['data']['frontend']['players']['data']
# prepared_players = [attribute for player in players for attribute in players if attribute.endswith('name')]
prepared_players = [[value for key, value in player.items() if key.endswith('name')] for player in players]


# print(len(prepared_players))

# name_players = list(map(lambda x: ' '.join(x.values()).strip(), players))
name_players = list(map(lambda x: ' '.join(x).strip(), prepared_players))

doubles = []

for i in name_players:
    if name_players.count(i) > 1:
        doubles.append(i)

doubles_set = set(doubles)



# doubles = []
# for i in range(len(name_players)):
#     for j in range(i+1, len(name_players) - 1):
#         if name_players[i] == name_players[j]:
#             doubles.append(name_players[i])
#             break
# print(len(doubles))
# doubles_set_2 = set(doubles)
# print(len(doubles_set_2))
file_to_save_women = 'doubles_women_1.txt'
with open(file_to_save_women, 'w') as file: # choose file to save
    for i in doubles_set:
        file.write(i + '\n')
#

