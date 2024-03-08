from dataclasses import dataclass
from typing import NamedTuple




# @dataclass()
class Player(NamedTuple):
    id: str
    full_name: str
    birthday: str
    photo: str


@dataclass
class Team:
    pass


@dataclass
class Tournament:
    pass



