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
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass


class Actions(Base):
    __tablename__ = 'actions'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    real_name: Mapped[Optional[str]]
    keyboards: Mapped[List['KeyboardsAndActions']] = relationship(back_populates='action')


class Keyboards(Base):
    __tablename__ = 'keyboards'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    actions: Mapped[List['KeyboardsAndActions']] = relationship(back_populates='kb')


class KeyboardsAndActions(Base):
    __tablename__ = 'keyboard_actions'
    kb_id: Mapped[int] = mapped_column(ForeignKey('keyboards.id'), primary_key=True)
    action_id: Mapped[int] = mapped_column(ForeignKey('actions.id'), primary_key=True)
    kb: Mapped['Keyboards'] = relationship(back_populates='actions')
    action: Mapped['Actions'] = relationship(back_populates='keyboards')


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[JSON] = mapped_column(JSON)
