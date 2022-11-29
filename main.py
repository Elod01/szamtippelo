import random
import tkinter
from tkinter import *
import tkinter.messagebox

r = [-1]
tippek = [0]

def imput_csekk(imput):

    try:
        var=int(imput)
        if var <= 0:
            tkinter.messagebox.showinfo("Hiba", "Írjon be egy 0-nál nagyobb számot!")
        else:
            ntry1["state"] = DISABLED
            bttn1["state"] = DISABLED
            ntry2["state"] = NORMAL
            bttn2["state"] = NORMAL
            max = int(ntry1.get())
            r[0] = random.randint(0, max)
    except:
        tkinter.messagebox.showinfo("Hiba", "Számot írjon be!")

def tippsz_csekk(tippsz):
    try:
        var=int(tippsz)
        if var < 0:
            lbl3.config(text="Írjon be pozitív számot!")
        else:
            if var == r[0]:
                tippek[0] += 1
                lbl3.config(text="")
                ntry1["state"] = NORMAL
                bttn1["state"] = NORMAL
                ntry1.delete(0, END)
                ntry2.delete(0, END)
                ntry2["state"] = DISABLED
                bttn2["state"] = DISABLED
                meszidzs="Tippek száma: "+str(tippek[0])
                tkinter.messagebox.showinfo("Helyes válasz!", meszidzs)
                tippek[0] = 0
            elif var > r[0]:
                tippek[0] += 1
                lbl3.config(text="Kevesebb!")
            elif var < r[0]:
                tippek[0] += 1
                lbl3.config(text="Több!")
    except:
        lbl3.config(text="Számot írjon be")


ablak = tkinter.Tk()
ablak.title("Számtippelő")

keret = tkinter.Frame(ablak)
keret.pack()

lbl1 = tkinter.Label(keret, text='Írjon be egy számot!')
lbl1.grid(row=0, column=0)

ntry1 = tkinter.Entry(keret)
ntry1.grid(row=0, column=1)

bttn1 = tkinter.Button(keret, text='Választ', background='white', command=lambda: imput_csekk(ntry1.get()))
bttn1.grid(row=0,column=3)

lbl2 = tkinter.Label(keret, text='Tippeljen egy számra!')
lbl2.grid(row=1, column=0)

ntry2 = tkinter.Entry(keret, state=DISABLED)
ntry2.grid(row=1, column=1)

bttn2 = tkinter.Button(keret, text='Tipp', background='white', command=lambda: tippsz_csekk(ntry2.get()), state=DISABLED)
bttn2.grid(row=1, column=3)

lbl3 = tkinter.Label(keret, text='')
lbl3.grid(row=2, columnspan=2)

ablak.mainloop()