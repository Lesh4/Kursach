"""Метод Эйлера"""
from math import *
from zamena import zamena

def Eiler(x, x_last, y, h, uravn):
    res = []
    while x <= x_last:
        uravn_res = eval(zamena(x, y, uravn))
        y_del = h*uravn_res
        res.append([float(format(x, ".4f")), float(format(y, ".4f")), float(format(uravn_res, ".4f")), float(format(y_del, ".4f"))])
        y += y_del
        x += h
    return res
