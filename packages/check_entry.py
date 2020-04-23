from tkinter import messagebox
from packages.methods_funcs import zamena
from math import *
def check_h(h):
    if h > 0:
        return True
    else:
        messagebox.showerror("Неверный ввод", "Шаг должен быть больше 0")
def check_x(x_start, x_last):
    if x_start < x_last:
        return True
    else:
        messagebox.showerror("Неверный ввод", "X начальный должен быть меньше X конечного")
def check_func(x, y, func):
    try:
        eval(zamena(x, y, func))
        return True
    except:
        messagebox.showerror("Неверный ввод", "Функция введена неверно")
def check_predel(x_start, x_last, h):
    if (x_last - x_start)/h < 100:
        return True
    else:
        messagebox.showerror("Ошибка", "Количество итераций превышает 100")