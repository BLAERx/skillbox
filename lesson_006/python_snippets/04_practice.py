from nim_engine import put_stones, get_bunches, take_from_bunch, is_gameover
from termcolor.termcolor import cprint, colored

put_stones()
user_number = 1
while True:
    cprint('Текущая позиция', color='green')
    cprint(get_bunches(), color='green')
    user_color = 'blue' if user_number == 1 else 'yellow'
    cprint('Ход игрока {}'.format(user_number), color=user_color)
    pos = input(colored('Откуда берём?', color=user_color))
    qua = input(colored(('Сколько берём'), color=user_color))
    take_from_bunch(position=int(pos), quantity=int(qua))
    if is_gameover():
        break
    user_number = 2 if user_number == 1 else 1

cprint('Выиграл игрок номер {}'.format(user_number), color='red')

