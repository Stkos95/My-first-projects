
from dataclasses import dataclass


@dataclass
class Actions:
    actual_names: str
    keyboard_names: str


New_template = Actions(
    actual_names=("Точные удары",
                    "Удары мимо",
                    "Точные передачи",
                    "Точные передачи в атаке",
                    "Владение в атаке"
                    "Успешный дриблинг в атаке",
                    "Отборы и перехваты",
                    "Гол"
                    ),
    keyboard_names=( 'удар✅',
                  'удар❌',
                  'передача✅',
                  'Передачи в атакующей зоне✅',
                  'Обводка АТАКА✅',
                  "Отбор/перехват",
                  'ГОЛ!!!⚽⚽⚽',
                  )
)




def transfer_results(results: dict[str:dict]):
    passession_common = sum(results[i][j] for i in results for j in results[i] if j.startswith("передача"))
    first_team = True
    print(f'{passession_common=}')
    tmp = {}
    for teams in results:
        team = results[teams]
        shoots_all = sum([team[i] for i in team if i.startswith('удар')])
        try:
            percent_shoots = team['удар✅'] / shoots_all * 100
        except ZeroDivisionError:
            percent_shoots = 0
        pass_all = sum([team[i] for i in team if i.startswith('передача')])
        try:
            percent_pass = team['передача✅'] / pass_all * 100
        except ZeroDivisionError:
            percent_pass = 0
        obvodka_all = sum([team[i] for i in team if i.startswith('Обводка')])
        if first_team:
            ball_posession = round(sum(team[i] for i in team if i.startswith("передача")) /passession_common * 100)
            first_team = False
        else:
            ball_posession = 100 - ball_posession

        tmp[teams] = {"Удары всего/в створ/точность": f'{shoots_all}/{team.get("удар✅")}/{round(percent_shoots)}%',
                      "Передачи всего/Успешные/точность": f'{pass_all}/{team.get("передача✅")}/{round(percent_pass)}%',
                     # "Процент точных передач": f'{round(percent_pass)}',
                      "Владение мячом": f'{ball_posession}%',
                      "Обводка всего/Обводка точная": f'{obvodka_all}/{team.get("Обводка✅")}',
                      "Отборы/перехват": f'{team.get("Перехваты")}',
                      "Фолы": f'{team.get("Фолы")}',
                      "Карточки": f'{team.get("ЖК")}/{team.get("КК")}',
                      "Угловые": f'{team.get("Угловые")}'
                      }
    return tmp


def transfer_results_short_template(results: dict[str:dict]):
    # passession_common = sum(results[i][j] for i in results for j in results[i] if j.startswith("передача"))
    first_team = True
    # print(f'{passession_common=}')
    tmp = {}
    for teams in results:
        team = results[teams]
        shoots_all = sum([team[i] for i in team if i.startswith('удар')])
        # try:
        #     percent_shoots = team['удар✅'] / shoots_all * 100
        # except ZeroDivisionError:
        #     percent_shoots = 0
        
        pass_accurate_atack = team.get('Передачи в атакующей зоне✅')
        pass_accurate_all = team.get('передача✅') + pass_accurate_atack
        dribling = team.get('Обводка АТАКА✅')
        defencive = team.get("Отбор/перехват")
        try:
            possession = round(pass_accurate_atack / pass_accurate_all)
        except ZeroDivisionError:
            possession = 0
        # obvodka_all = sum([team[i] for i in team if i.startswith('Обводка')])
        # if first_team:
        #     ball_posession = round(sum(team[i] for i in team if i.startswith("передача")) /passession_common * 100)
        #     first_team = False
        # else:
        #     ball_posession = 100 - ball_posession

        tmp[teams] = { "Удары всего/в створ": f'{shoots_all}/{team.get("удар✅")}',
                      'Передачи всего': pass_accurate_all ,
                      'передачи атака': pass_accurate_atack,
                      'vladenie': possession,
                    
                      'обводка': dribling,
                      'defencive': defencive
                      }
    return tmp