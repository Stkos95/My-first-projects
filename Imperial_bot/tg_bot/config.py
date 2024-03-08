from dataclasses import dataclass
from typing import List
from environs import Env

@dataclass
class TgBot:
    token: str
    admin_ids: List[int]
    use_redis: bool




@dataclass
class Config:
    tg_bot: TgBot

def load_config(path:str = None):
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env.str("TOKEN"),
            admin_ids=list(map(int,env.list("ADMINS"))),
            use_redis=False
        )
    )

