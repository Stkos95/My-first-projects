import os
from misc.database.db import Session
from misc.database.models import User
from sqlalchemy import select


#сделать чтобы был выбор лиги, а затем поиск в соответствующей папке согласно лиге.
def get_templates(dir_path):
    d = os.listdir(f"/home/konstantin/my_python/PycharmProjects/Statbot/templates/{dir_path}")
    return d


def add_data_to_db(data):
    with Session() as session:
        session.add(
            User(
                name=data
            )
        )
        session.commit()
    

def get_data_from_db():
    with Session() as session:
        stm = select(User.id, User.name)
        d = session.execute(stm).all()

    return d
