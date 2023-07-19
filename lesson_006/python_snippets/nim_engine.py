from random import randint

MAX_BUNCHES = 5
MAX_BUNCHES_SIZE = 20

_holder = {}






def take_from_bunch(position, quantity):
        if position in _holder:
            _holder[position] -= quantity
def put_stones():
    """расположить камни на игровой поверхности"""
    global _holder
    _holder = {}
    for i in range(1, MAX_BUNCHES + 1):
        _holder[i] = randint(1, MAX_BUNCHES_SIZE)


def get_bunches():
    res = []
    for i in sorted(_holder.values()):
        res.append(_holder.values())
    return res


def is_gameover():
    return sum(_holder.values()) == 0