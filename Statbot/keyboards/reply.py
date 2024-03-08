from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from dataclasses import dataclass
from typing import List




@dataclass
class Leagues:
    names: List[str]
    callbacks: List[str]

    def generate_kb_reply(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        for name, callback in zip(self.names, self.callbacks):
            keyboard.add(KeyboardButton(text=name ))
        return keyboard
    
    def generate_kb_inline(self):
        kb = InlineKeyboardMarkup()
        for name, callback in zip(self.names, self.callbacks):
            kb.add(InlineKeyboardButton(text=name, callback_data=callback))
        return kb



leagues = Leagues(
    names = ['Лига 5х5'],
    callbacks=['league5x5']
).generate_kb_inline()


templates = Leagues(
    names = ['Готовый шаблон', "Пустой шаблон"],
    callbacks=['aa', 'dd']
).generate_kb_reply()

