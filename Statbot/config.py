from environs import Env
from typing import List
from pprint import pprint
from dataclasses import dataclass
env = Env()

env.read_env()

token = env.str("TOKEN")

admin = env.int("ADMINS")



actions_team_analitic = {
    "Первый тайм": {
        'передача✅': 0,
        'передача❌': 0,
        'Прием мяча✅': 0,
        'Прием мяча❌': 0,
        'удар✅': 0,
        'удар❌': 0,
        'Обводка✅': 0,
        "Обводка❌": 0,
        "ЖК": 0,
        "КК": 0,
        "🛡Перехват✅": 0,
        "🛡Перехват❌": 0,
        "🛡Отбор✅": 0,
        "🛡Отбор❌": 0,
        "Угловые": 0,
        "Голевые моменты": 0,
        "Штрафные удары": 0,
        "Подборы": 0,
        "Потери": 0

    },
    "Второй тайм": {
        'передача✅': 0,
        'передача❌': 0,
        'Прием мяча✅': 0,
        'Прием мяча❌': 0,
        'удар✅': 0,
        'удар❌': 0,
        'Обводка✅': 0,
        "Обводка❌": 0,
        "ЖК": 0,
        "КК": 0,
        "🛡Перехват✅": 0,
        "🛡Перехват❌": 0,
        "🛡Отбор✅": 0,
        "🛡Отбор❌": 0,
        "Угловые": 0,
        "Голевые моменты": 0,
        "Штрафные удары": 0,
        "Подборы": 0,
        "Потери": 0

    },
}

personal_template = {
    "Оборона": {"Сопр-назад": 0,
                "Сопр-назад❌": 0,
                "Сопр-поперек": 0,
                "Сопр-поперек❌": 0,
                "Сопр-вперед": 0,
                "Сопр-вперед❌": 0,
                "Назад": 0,
                "Назад❌": 0,
                "Поперек": 0,
                "Поперек❌": 0,
                "Вперед": 0,
                "Вперед❌": 0,
                'Обводка✅': 0,
                "Обводка❌": 0,
                "Отбор✅": 0,
                "Отбор❌": 0,
                "Перехват✅": 0,
                "Перехват❌": 0,

                },
    "Середина": {"Сопр-назад": 0,
                "Сопр-назад❌": 0,
                "Сопр-поперек": 0,
                "Сопр-поперек❌": 0,
                "Сопр-вперед": 0,
                "Сопр-вперед❌": 0,
                "Назад": 0,
                "Назад❌": 0,
                "Поперек": 0,
                "Поперек❌": 0,
                "Вперед": 0,
                "Вперед❌": 0,
                'Обводка✅': 0,
                "Обводка❌": 0,
                "Отбор✅": 0,
                "Отбор❌": 0,
                "Перехват✅": 0,
                "Перехват❌": 0,

                 },
    "Атака": {"Сопр-назад": 0,
              "Сопр-поперек": 0,
              "Сопр-вперед": 0,
              "Назад": 0,
              "Поперек": 0,
              "Вперед": 0,
              "Сопр-назад❌": 0,
              "Сопр-поперек❌": 0,
              "Сопр-вперед❌": 0,
              "Назад❌": 0,
              "Поперек❌": 0,
              "Вперед❌": 0,
              'Обводка✅': 0,
              "Обводка❌": 0,
              "Перехват✅": 0,
              "Перехват❌": 0,
              "Отбор✅": 0,
              "Отбор❌": 0,

              },
    "Удары": {
        "из-за штрафной": 0,
        "из-за штрафной❌": 0,
        "ИЗ штрафной": 0,
        "ИЗ штрафной❌": 0
    },
    "Прочее": {"Потери мяча": 0,
               "Подбор мяча": 0,
               "Угловые": 0,
               "Штрафные": 0,
               "Прием мяча": 0,
               "Прием мяча❌": 0,



    }
}


# actions = {
# "С сопротивлением": {
#
#         },
#         "Без сопротивления": {
#
#         },
#         'Обводка✅': 0,
#         "Обводка❌": 0,
#         "🛡Перехват✅": 0,
#         "🛡Перехват❌": 0,
#         "🛡Отбор✅": 0,
#         "🛡Отбор❌": 0
#
# }
#
# actions = {
#
#     'Обводка✅': 0,
#     "Обводка❌": 0,
#     "🛡Перехват✅": 0,
#     "🛡Перехват❌": 0,
#     "🛡Отбор✅": 0,
#     "🛡Отбор❌": 0,
#     "Сопр-назад": 0,
#     "Сопр-поперек": 0,
#     "Сопр-вперед": 0,
#     "Назад": 0,
#     "Поперек": 0,
#     "Вперед": 0,
#
# }
#
# passes = ["Назад", "Поперек", "Вперед"]
# for i in personal_template:
#     if i != "Другие действия":
#         personal_template[i] = actions

# for zone in personal_template:
#     for action in personal_template[zone]:
#         if isinstance(personal_template[zone][action], dict):
#
#             for k in passes:
#                 personal_template[zone][action][k] = 0

# pprint(personal_template)

# {'Другие действия': {},
#  'Зона атаки': {'Без сопротивления': {'Вперед': 0, 'Назад': 0, 'Поперек': 0},
#                 'Обводка✅': 0,
#                 'Обводка❌': 0,
#                 'С сопротивлением': {'Вперед': 0, 'Назад': 0, 'Поперек': 0},
#                 '🛡Отбор✅': 0,
#                 '🛡Отбор❌': 0,
#                 '🛡Перехват✅': 0,
#                 '🛡Перехват❌': 0},
#  'Зона обороны': {'Без сопротивления': {'Вперед': 0, 'Назад': 0, 'Поперек': 0},
#                   'Обводка✅': 0,
#                   'Обводка❌': 0,
#                   'С сопротивлением': {'Вперед': 0, 'Назад': 0, 'Поперек': 0},
#                   '🛡Отбор✅': 0,
#                   '🛡Отбор❌': 0,
#                   '🛡Перехват✅': 0,
#                   '🛡Перехват❌': 0},
#  'Зона средняя': {'Без сопротивления': {'Вперед': 0, 'Назад': 0, 'Поперек': 0},
#                   'Обводка✅': 0,
#                   'Обводка❌': 0,
#                   'С сопротивлением': {'Вперед': 0, 'Назад': 0, 'Поперек': 0},
#                   '🛡Отбор✅': 0,
#                   '🛡Отбор❌': 0,
#                   '🛡Перехват✅': 0,
#                   '🛡Перехват❌': 0}}


class Activities:
    def __init__(self, data):
        self.datas = data


datas = {'Второй тайм': {'Атака': {'Вперед': 0,
                                   'Назад': 0,
                                   'Обводка✅': 0,
                                   'Обводка❌': 0,
                                   'Поперек': 0,
                                   'Сопр-вперед': 0,
                                   'Сопр-назад': 0,
                                   'Сопр-поперек': 0,
                                   '🛡Отбор✅': 0,
                                   '🛡Отбор❌': 0,
                                   '🛡Перехват✅': 0,
                                   '🛡Перехват❌': 0},
                         'Оборона': {'Вперед': 0,
                                     'Назад': 0,
                                     'Обводка✅': 0,
                                     'Обводка❌': 0,
                                     'Поперек': 0,
                                     'Сопр-вперед': 0,
                                     'Сопр-назад': 0,
                                     'Сопр-поперек': 0,
                                     '🛡Отбор✅': 0,
                                     '🛡Отбор❌': 0,
                                     '🛡Перехват✅': 0,
                                     '🛡Перехват❌': 0},
                         'Прочее': {},
                         'Середина': {'Вперед': 0,
                                      'Назад': 0,
                                      'Обводка✅': 0,
                                      'Обводка❌': 0,
                                      'Поперек': 0,
                                      'Сопр-вперед': 0,
                                      'Сопр-назад': 0,
                                      'Сопр-поперек': 0,
                                      '🛡Отбор✅': 0,
                                      '🛡Отбор❌': 0,
                                      '🛡Перехват✅': 0,
                                      '🛡Перехват❌': 0}},
         'Первый тайм': {'Атака': {'Вперед': 1,
                                   'Назад': 0,
                                   'Обводка✅': 0,
                                   'Обводка❌': 0,
                                   'Поперек': 0,
                                   'Сопр-вперед': 0,
                                   'Сопр-назад': 0,
                                   'Сопр-поперек': 0,
                                   '🛡Отбор✅': 1,
                                   '🛡Отбор❌': 0,
                                   '🛡Перехват✅': 0,
                                   '🛡Перехват❌': 0},
                         'Оборона': {'Вперед': 0,
                                     'Назад': 0,
                                     'Обводка✅': 0,
                                     'Обводка❌': 0,
                                     'Поперек': 0,
                                     'Сопр-вперед': 0,
                                     'Сопр-назад': 0,
                                     'Сопр-поперек': 0,
                                     '🛡Отбор✅': 0,
                                     '🛡Отбор❌': 0,
                                     '🛡Перехват✅': 0,
                                     '🛡Перехват❌': 0},
                         'Прочее': {},
                         'Середина': {'Вперед': 0,
                                      'Назад': 0,
                                      'Обводка✅': 0,
                                      'Обводка❌': 0,
                                      'Поперек': 0,
                                      'Сопр-вперед': 0,
                                      'Сопр-назад': 0,
                                      'Сопр-поперек': 0,
                                      '🛡Отбор✅': 0,
                                      '🛡Отбор❌': 0,
                                      '🛡Перехват✅': 0,
                                      '🛡Перехват❌': 0}}}


