"""
Модуль вспомогательных функций для методов решения.
"""
def check_znaki(x, x_last, y, h):
    """
    Возвращает количество знаков, которое должно быть после запятой у результата.
    """
    string = [str(x), str(x_last), str(y), str(h)]
    kol = [len(s.split('.')[1]) for s in string]
    return max(kol)

def zamena(x, y, uravn):
    """
    Заменяет строковые значения x и y на значения float.
    """
    uravn = uravn.replace('y', str(y))
    uravn = uravn.replace('x', str(x))
    uravn = uravn.replace('^', '**')
    return uravn
