from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from sqlalchemy import Table, Column, Integer, String, JSON
from .models import Base, Keyboards, KeyboardsAndActions, Actions

# class Base(DeclarativeBase):
#     pass


# URLDATABASE = f'postgresql+psycopg2://konstantin:123321@localhost/test_json?client_encoding=utf8'
URLDATABASE = f'postgresql+psycopg2://konstantin:123321@localhost/test_json'



engine = create_engine(URLDATABASE)
Base.metadata.create_all(engine)

Session = sessionmaker(engine)

data = {'передача✅': 0, 'передача❌': 0, 'удар✅': 0, 'удар❌': 0, 'Обводка✅': 0, 'Обводка❌': 0, 'Перехваты': 0, 'Фолы': 0,
        'ЖК': 0, 'КК': 0, 'Угловые': 0, 'ГОЛ!!!⚽⚽⚽': 0}

# with Session() as session:
#     session.add(
#         User(
#         name = data
#         )
#     )
#     session.commit()

# stm = select(User.id, User.name)
# d = session.execute(stm).all()

# print(d)


# kbs = [
#     Keyboards(name='short'),
#     Keyboards(name='standart'),
#     Keyboards(name='long'),
# ]

# acts = [
#     Actions(name='Удар'),
#     Actions(name='передача'),
#     Actions(name='Фол'),
#
# ]
actions = ['Удар',
           'передача',
           # 'Фол'
           ]

if __name__ == '__main__':
    with Session() as session:
        # for act in actions:
        #     statement = select(Actions.id).where(Actions.name == act)
        #     d = session.execute(statement).scalars().first()
        #     print(d)
        #     session.add(KeyboardsAndActions(kb_id=2, action_id=d))
        # session.commit()
        statement = select(KeyboardsAndActions).where(KeyboardsAndActions.kb.has(Keyboards.name == 'standart'))
        d = session.execute(statement).scalars().all()
        for i in d:
            print(i.action.name)



    #
    # session.add_all(acts)
    # session.commit()
