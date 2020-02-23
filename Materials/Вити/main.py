import tkinter
import tkinter.ttk
from tkinter import messagebox
import Gauss
import SQRTMethod



class CustomMenu(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        root_window.title('Решение СЛАУ')
        #root_window.iconbitmap("main.ico")
        root_window.geometry("630x350")
        root_window.resizable(0, 0)
        root_window.config(background ="#373A68" )
        self.first_frame= tkinter.Frame(root_window, bg = "#A3A3D7")
        self.first_frame.grid(ipadx=315, ipady=175)
        self.second_frame = tkinter.Frame(root_window, bg = "#A3A3D7")
        self.third_frame = tkinter.Frame(root_window, bg = "#A3A3D7")
        self.fourth_frame = tkinter.Frame(root_window, bg="#A3A3D7")
        self.create_widgets_in_first_frame()


    def create_widgets_in_first_frame(self):
        w = tkinter.Label(self.first_frame, text="Курсовой проект\n\nПрограмма для решения СЛАУ методами Гаусса\n и квадратного корня",
                              font=("Helvetica", 18), justify=tkinter.CENTER, bg = "#A3A3D7")
        w.place(relx=.5, rely=.3, anchor="c")
        w1 = tkinter.Label(self.first_frame, text="Укажите количество уравнений:", font=("Helvetica", 11), bg = "#A3A3D7")
        w1.place(x=150, y=300, anchor="c")
        self.combobox = tkinter.ttk.Combobox(self.first_frame, state="readonly", values=[u"1", u"2", u"3", u"4",u"5", u"6"], height=6, width=10 )
        self.combobox.set(u"1")
        self.combobox.place(x=320, y=300, anchor="c")
        but2 = tkinter.Button(self.first_frame, text="Продолжить",  background="#373A68",
                                                   font=("Helvetica", 11), fg="White", command=self.call_second_frame_on_top)
        but2.place(x=460, y=300, height=50, width=120, anchor="c")

    def create_widgets_in_second_frame(self):
        self.entryArray = []
        coordy = -10
        for i in range (0,self.num):
            self.entryArray.append([])
            coordy+=35
            coordx = 40
            for j in range(0, self.num+1):
                self.entryArray[i].append(tkinter.Entry(self.second_frame, width=7))
                self.entryArray[i][j].insert("0", 0)
                self.entryArray[i][j].place(x =coordx, y = coordy, anchor="center")

                if (j == self.num-1):
                    tkinter.Label(self.second_frame, text="*X"+str(j)+" =",
                              font=("Helvetica", 11), justify=tkinter.CENTER, bg = "#A3A3D7" ).place(x =coordx+45, y = coordy, anchor="center")
                if (j < self.num - 1):
                    tkinter.Label(self.second_frame, text="*X" + str(j) + " +",
                                  font=("Helvetica", 11), justify=tkinter.CENTER, bg="#A3A3D7").place(x=coordx + 45,
                                                                                                      y=coordy,
                                                                                                      anchor="center")

                coordx+=91

        second_window_back_button = tkinter.Button(self.second_frame, text="Назад", background="#373A68",
                                                   font=("Helvetica", 11), fg="White",
                                                   command=self.call_first_frame_on_top)
        second_window_back_button.place(x=188, y=300, height=50, width=120, anchor="c")

        Gauss_button = tkinter.Button(self.second_frame, text="Gauss", background="#373A68",
                                                   font=("Helvetica", 11), fg="White", command=self.toGauss)
        Gauss_button.place(x=308, y=300, height=50, width=120, anchor="c")

        SQRT_button = tkinter.Button(self.second_frame, text="SQRT", background="#373A68",
                                                   font=("Helvetica", 11), fg="White", command=self.toSQRTMethod)
        SQRT_button.place(x=428, y=300, height=50, width=120, anchor="c")

    def create_widgets_in_third_frame(self):
        # Create the label for the frame
        third_window_label = tkinter.Label(self.third_frame, text="Решения СЛАУ методом Гаусса",
                              font=("Helvetica", 18), justify=tkinter.CENTER, background="#A3A3D7")
        third_window_label.place(relx=.5, rely=.1, anchor="c")
        self.answerArray =[]
        coordy = 40
        for i in range(0,self.num):
            coordy += 35
            stringt = "X[" + str(i) + "] =" + str(self.gaussAnswer[i])
            self.answerArray.append(tkinter.Label(self.third_frame, text =stringt, font=("Helvetica", 18), bg = "#A3A3D7" ))
            self.answerArray[i].place(x = 300, y = coordy, anchor="c" )
        # Create the button for the frame
        third_window_back_button = tkinter.Button(self.third_frame, text = "Назад", background="#373A68",
                                                   font=("Helvetica", 11), fg="White", command = self.call_second_frame_on_top)
        third_window_back_button.place(x=188, y=300, height=50, width=120, anchor="c")

    def create_widgets_in_fourth_frame(self):
        # Create the label for the frame
        fourth_window_label = tkinter.Label(self.fourth_frame, text="Решения СЛАУ методом квадратного корня",
                              font=("Helvetica", 18), justify=tkinter.CENTER, background="#A3A3D7")
        fourth_window_label.place(relx=.5, rely=.1, anchor="c")
        self.answerArray =[]
        coordy = 40
        for i in range(0,self.num):
            coordy += 35
            stringt = "X[" + str(i) + "] =" + str(self.SQRTAnswer[i])
            self.answerArray.append(tkinter.Label(self.fourth_frame, text =stringt, font=("Helvetica", 18), bg = "#A3A3D7" ))
            self.answerArray[i].place(x = 300, y = coordy, anchor="c" )
        # Create the button for the frame
        fourth_window_back_button = tkinter.Button(self.fourth_frame, text = "Назад", background="#373A68",
                                                   font=("Helvetica", 11), fg="White", command = self.call_second_frame_on_top)
        fourth_window_back_button.place(x=188, y=300, height=50, width=120, anchor="c")

    def call_first_frame_on_top(self):
        self.second_frame.destroy()
        self.first_frame.grid(ipadx=315, ipady=175)

    def call_second_frame_on_top(self):
        self.num = int(self.combobox.get())
        self.first_frame.grid_forget()
        self.third_frame.destroy()
        self.fourth_frame.destroy()
        self.second_frame = tkinter.Frame(root_window, bg = "#A3A3D7")
        self.second_frame.grid(ipadx=315, ipady=175)
        self.create_widgets_in_second_frame()


    def call_third_frame_on_top(self):
        self.second_frame.grid_forget()
        self.third_frame = tkinter.Frame(root_window,bg = "#A3A3D7")
        self.third_frame.grid(ipadx=315, ipady=175)
        self.create_widgets_in_third_frame()

    def call_fourth_frame_on_top(self):
        self.second_frame.grid_forget()
        self.fourth_frame = tkinter.Frame(root_window,bg = "#A3A3D7")
        self.fourth_frame.grid(ipadx=315, ipady=175)
        self.create_widgets_in_fourth_frame()


    def toGauss(self):
        error =0
        for i in range(0, self.num):
            for j in range(0, self.num + 1):
                try:
                    float(self.entryArray[i][j].get())
                    self.entryArray[i][j].config(background="White")
                except:
                    error = 1
                    self.entryArray[i][j].config(background="Red")
        if error == 0:
            self.forGauss = []
            for i in range(0, self.num):
                self.forGauss.append([])
                for j in range(0, self.num + 1):
                        self.forGauss[i].append(float(self.entryArray[i][j].get()))
            try:
                self.gaussAnswer = Gauss.Gauss(self.forGauss,self.num)
                self.call_third_frame_on_top()
            except:
                messagebox.showerror("Ошибка", "Решений этим методом нет!")

        else:
            messagebox.showerror("Ошибка", "Недопустимые значения")

    def toSQRTMethod(self):

        error = 0
        for i in range(0, self.num):
            for j in range(0, self.num + 1):
                try:
                    float(self.entryArray[i][j].get())
                    self.entryArray[i][j].config(background="White")
                except:
                    error = 1
                    self.entryArray[i][j].config(background="Red")
        if error == 0:
            self.forSQRT = []
            self.columnB = []
            for i in range(0, self.num):
                self.forSQRT.append([])
                self.columnB.append(float(self.entryArray[i][self.num].get()))
                for j in range(0, self.num):
                    if (self.entryArray[i][j].get() != self.entryArray[j][i].get()):
                        error = 1
                        self.entryArray[i][j].config(background="Blue")
                        self.entryArray[j][i].config(background="Blue")
                    else:
                        self.entryArray[i][j].config(background="White")
                        self.forSQRT[i].append(float(self.entryArray[i][j].get()))
            if error == 0:
                try:
                    self.SQRTAnswer = SQRTMethod.SQRTMethod(self.forSQRT, self.columnB, self.num)
                    self.call_fourth_frame_on_top()
                except:
                    messagebox.showerror("Ошибка", "Решений этим методом нет!")
            else:
                messagebox.showerror("Ошибка", "Матрица не симметрична!")
        else:
            messagebox.showerror("Ошибка", "Недопустимые значения")




    def quit_program(self):
        root_window.destroy()



if __name__ == '__main__':

   root_window = tkinter.Tk()
   run = CustomMenu(root_window)
   root_window.mainloop()