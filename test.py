import tkinter as tk
#
def reconf_canvas(event):
    canv.configure(scrollregion=canv.bbox('all'))
#
root = tk.Tk()
root.geometry("400x400+100+100")
#
canv = tk.Canvas(root, width=200, height=200)
canv.grid(row=0, column=0)
#
frm = tk.Frame(canv)
frm.pack()
#
scr = tk.Scrollbar(root)
scr.grid(row=0, column=1, sticky="ns")
scr["command"] = canv.yview
canv["yscrollcommand"] = scr.set
canv.create_window((0,0), window=frm, anchor="nw")
frm.bind("<Configure>", reconf_canvas)
#
for i in range(20):
    but = tk.Button(frm, text=u"Кнопка %01d" % i)
    but.pack()
#
root.mainloop()