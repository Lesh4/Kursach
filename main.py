import tkinter as tk
from Eiler import Eiler
from tkinter import messagebox

"""
TODO: 
1) make windows with interface
    a) first with values and metod`s buttons                 +
    b) result window
2) add check for input values (x, y, h and function)
2) code logic of Eiler
3) code logic of Upgrade Eiler

"""

class Menu(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        root.title("Решение дифференциальных уравнений")
        root.geometry("740x400")
        root.resizable(0, 0)
        root.config(background = "#F5F5DC")
        self.start= tk.Frame(root, bg = "#F5F5DC")
        self.start.grid(ipadx=415, ipady=275)
        self.EilerWindow = tk.Frame(root, bg = "#F5F5DC")
        self.UpgradeEilerWindow = tk.Frame(root, bg = "#F5F5DC")
        self.create_widgets_start()

    def save_entry(self):
        self.x_start = float(self.entry_start_x.get())
        self.x_last = float(self.entry_last_x.get())
        self.y = float(self.entry_y.get())
        self.h = float(self.entry_h.get())
        self.func = self.entry_func.get()
        self.create_EilerWindow()

    def create_widgets_start(self):
        tk.Label(self.start, text = "Решение дифференциальных уравнений", font=("Segoe print", 18), bg = "#F5F5DC").place(x=120, y=30)
        x_lb = tk.Label(self.start, text = "X начальное", font=("Segoe print", 14), bg = "#F5F5DC").place(x=30, y=100)
        self.entry_start_x = tk.Entry(self.start, width=10)
        self.entry_start_x.place(x=190, y =110)

        x_lb = tk.Label(self.start, text = "X конечное", font=("Segoe print", 14), bg = "#F5F5DC").place(x=400, y=100)
        self.entry_last_x = tk.Entry(self.start, width=10)
        self.entry_last_x.place(x=560, y =110)

        y_lb = tk.Label(self.start, text = "Y начальное", font=("Segoe print", 14), bg = "#F5F5DC").place(x=30, y=140)
        self.entry_y = tk.Entry(self.start, width=10)
        self.entry_y.place(x=190, y=150)

        h_lb = tk.Label(self.start, text = "Шаг", font=("Segoe print", 14), bg = "#F5F5DC").place(x=430, y=140)
        self.entry_h = tk.Entry(self.start, width=10)
        self.entry_h.place(x=560, y=150)

        func_lb = tk.Label(self.start, text="Функция вида: y` = f(x;y)", font=("Segoe print", 14), bg = "#F5F5DC").place(x=30, y=240)
        self.entry_func = tk.Entry(self.start, width=35)
        self.entry_func.place(x=45, y = 300, height=50)

        Eiler = tk.Button(self.start, text="Метод Эйлера", command=self.save_entry, font=("Segoe print", 11), bg = "#FAEBD7").place(x=500, y=240)
        UpgradeEiler = tk.Button(self.start, text="Усовершенствованный метод Эйлера", command=self.create_UpgradeEilerWindow, font=("Segoe print", 11), bg = "#FAEBD7").place(x=400, y=300)

    def create_widgets_EilerWindow(self):
        tk.Label(self.EilerWindow, text = "Метод Эйлера", font=("Segoe print", 18), bg = "#F5F5DC").place(x=270, y=30)
        tk.Button(self.EilerWindow, text = "Назад", font=("Segoe print", 11), bg = "#FAEBD7", width = 10, command = self.create_start).place(x=580, y=320)
        Eiler_list = Eiler(self.x_start, self.x_last, self.y, self.h, self.func)
        y = 100
        tk.Label(self.EilerWindow, text = "  x                   y                   y`                   yΔ", bg = "#F5F5DC").place(x=250, y=80)
        for elem in Eiler_list:
            string = ""
            for el in elem:
                if len(str(el)) >= 4:
                    string += str(el)+"             "
                else:
                    string += str(el)+"                "
            tk.Label(self.EilerWindow, text = string, bg = "#F5F5DC").place(x=250, y=y)
            y+=20
    
    def create_widgets_UpgradeEilerWindow(self):
        tk.Label(self.UpgradeEilerWindow, text = "Усовершенствованный метод Эйлера", font=("Segoe print", 18), bg = "#F5F5DC").place(x=135, y=30)
        tk.Button(self.UpgradeEilerWindow, text = "Назад", font=("Segoe print", 11), bg = "#FAEBD7", width = 10, command = self.create_start).place(x=580, y=320)

    def create_start(self):
        self.EilerWindow.destroy()
        self.UpgradeEilerWindow.destroy()
        self.start.grid(ipadx=415, ipady=275)
        self.create_widgets_start()

    def create_EilerWindow(self):
        self.start.grid_forget()
        self.EilerWindow = tk.Frame(root, bg = "#F5F5DC")
        self.EilerWindow.grid(ipadx=415, ipady=275)
        self.create_widgets_EilerWindow()

    def create_UpgradeEilerWindow(self):
        self.start.grid_forget()
        self.UpgradeEilerWindow = tk.Frame(root, bg = "#F5F5DC")
        self.UpgradeEilerWindow.grid(ipadx=415, ipady=275)
        self.create_widgets_UpgradeEilerWindow()


root = tk.Tk()
run = Menu(root)
root.mainloop()
