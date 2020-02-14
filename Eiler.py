"""Метод Эйлера"""
from zamena import zamena
def Eiler(x, x_last, y, h, uravn):
    res = []
    while x <= x_last:
        uravn_res = eval(zamena(x, y, uravn))
        y_del = h*uravn_res
        res.append([x, y, uravn_res, y_del])
        y += y_del
        x += h
    return res
