import requests
import json
from dataclasses import dataclass
from typing import List
from tg_bot.misc.joinfootball_api.query_statements import QUERY_ALL_PLAYERS, QUERY_ALL_TEAMS
from config import load_config
from data_models import Player, Team

config = load_config()

TOKEN_MEN = config.joinsport.token

# Файл используется в проверке игроков в процессе добавления в команду.





# add methods to get lists of all teams, tournaments and so on
class JoinSportApi:
    '''
    class gets connection to Joinsport api and allow to get list of all players/teams/tournaments
    in database.
    '''
    URL = 'https://api.joinsport.io/graphql'
    headers = {'Api-key': TOKEN_MEN}

    def _make_request(self, q: str, var: None | str = None):
        data = {'query': q}
        if var:
            data.update(variables=var)
        r = requests.post(self.URL, headers=self.headers, json=data)
        return json.loads(r.text)



class Teams(JoinSportApi):
    def get_all_teams_list(self) -> List[Team]:
        r = self._make_request()



class Players(JoinSportApi):

    def get_all_players_list(self) -> List[Player]:
        r = self._make_request(QUERY_ALL_PLAYERS)
        players = r['data']['frontend']['players']['data']
        all_players = [Player(
                id=player.get('player_id'),
                full_name=' '.join([player[i].strip() for i in player if i.endswith('name')]),
                birthday = player.get('birthday'),
                photo = player.get('photo')
                    ) for player in players]
        return all_players

    def find_player(self, fio: str) -> List[Player]:
        """
        method is used to check the player exists or not.

        :param fio: fio of player you check
        :return list of Player class or empty list
        """

        players = self.get_all_players_list()
        fio_splitted = fio.split()
        players_copy = players.copy()
        for name in fio_splitted:
            for player in players:
                if name not in player.full_name:
                    players_copy.remove(player)
            players = players_copy[:]
        return players_copy











if __name__ == '__main__':

    d = Players()
    z = d.find_player('sdfsdf')
    print(z)
