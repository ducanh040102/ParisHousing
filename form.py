from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import main
import tkinter as tk

sqrtM = 0
numOfRoom = 0
yard = 0
pool = 0
floors = 0
cityCode = 0
cityPartRange = 0
previousOwners = 0
made = 0
isNewBuilt = 0
isStormProtector = 0
basement = 0
attic = 0
garage = 0
hasStoRoom = 0
hasGuestRoom = 0

def helloCallBack():
    sqrtM = en1.get()
    numOfRoom = en2.get()
    yard = varY.get()
    pool = varP.get()
    floors = en5.get()
    cityCode = en6.get()
    cityPartRange = en7.get()
    previousOwners = en8.get()
    made = en9.get()
    isNewBuilt = varB.get()
    isStormProtector = varS.get()
    basement = en12.get()
    attic = en13.get()
    garage = en14.get()
    hasStoRoom = varSR.get()
    hasGuestRoom = en16.get()

    messagebox.showinfo("Prediction","Price: " + main.predict(sqrtM, numOfRoom, yard, pool, floors, cityCode, cityPartRange, previousOwners, made, isNewBuilt, isStormProtector, basement, attic, garage, hasStoRoom, hasGuestRoom))

base = Tk()
base.geometry("700x540")
base.title("Paris Housing")

lb0 = Label(base, text="Paris House Price Prediction", width=25, font=("arial", 24))
lb0.place(x=120, y=40)

lb1 = Label(base, text="Square Meters", width=20, font=("arial", 12))
lb1.place(x=20, y=120)
en1 = Entry(base)
en1.place(x=200, y=120)

lb2 = Label(base, text="Number Of Rooms", width=20, font=("arial", 12))
lb2.place(x=19, y=160)
en2 = Entry(base)
en2.place(x=200, y=160)

lb3 = Label(base, text="Has Yard", width=20, font=("arial", 12))
lb3.place(x=5, y=200)
varY = IntVar()
Radiobutton(base, text="Yes", padx=5, variable=varY, value=1).place(x=180, y=200)
Radiobutton(base, text="No", padx=10, variable=varY, value=0).place(x=240, y=200)

lb4 = Label(base, text="Has Pool", width=20, font=("arial", 12))
lb4.place(x=5, y=240)
varP = IntVar()
Radiobutton(base, text="Yes", padx=5, variable=varP, value=1).place(x=180, y=240)
Radiobutton(base, text="No", padx=10, variable=varP, value=0).place(x=240, y=240)


lb5 = Label(base, text="Floors", width=20, font=("arial", 12))
lb5.place(x=19, y=280)
en5 = Entry(base)
en5.place(x=200, y=280)

lb6 = Label(base, text="City Code", width=20, font=("arial", 12))
lb6.place(x=19, y=320)
en6 = Entry(base)
en6.place(x=200, y=320)

lb7 = Label(base, text="City Part Range", width=20, font=("arial", 12))
lb7.place(x=19, y=360)
en7 = Entry(base)
en7.place(x=200, y=360)

lb8 = Label(base, text="Number Of Previous \n Owners", width=20, font=("arial", 12))
lb8.place(x=19, y=400)
en8 = Entry(base)
en8.place(x=200, y=400)

lb9 = Label(base, text="Made", width=20, font=("arial", 12))
lb9.place(x=340, y=120)
en9 = Entry(base)
en9.place(x=520, y=120)

lb10 = Label(base, text="Is New Built", width=20, font=("arial", 12))
lb10.place(x=340, y=160)
varB = IntVar()
Radiobutton(base, text="Yes", padx=5, variable=varB, value=1).place(x=520, y=160)
Radiobutton(base, text="No", padx=10, variable=varB, value=0).place(x=580, y=160)

lb11 = Label(base, text="Has Storm Protector", width=20, font=("arial", 12))
lb11.place(x=340, y=200)
varS = IntVar()
Radiobutton(base, text="Yes", padx=5, variable=varS, value=1).place(x=520, y=200)
Radiobutton(base, text="No", padx=10, variable=varS, value=0).place(x=580, y=200)

lb12 = Label(base, text="Basement", width=20, font=("arial", 12))
lb12.place(x=340, y=240)
en12 = Entry(base)
en12.place(x=520, y=240)

lb13 = Label(base, text="Attic", width=20, font=("arial", 12))
lb13.place(x=340, y=280)
en13 = Entry(base)
en13.place(x=520, y=280)

lb14 = Label(base, text="Garage", width=20, font=("arial", 12))
lb14.place(x=340, y=320)
en14 = Entry(base)
en14.place(x=520, y=320)

lb15 = Label(base, text="Has Storage Room", width=20, font=("arial", 12))
lb15.place(x=340, y=360)
varSR = IntVar()
Radiobutton(base, text="Yes", padx=5, variable=varSR, value=1).place(x=520, y=360)
Radiobutton(base, text="No", padx=10, variable=varSR, value=0).place(x=580, y=360)

lb16 = Label(base, text="Number of Guest \n Room", width=20, font=("arial", 12))
lb16.place(x=340, y=400)
en16 = Entry(base)
en16.place(x=520, y=400)

ttk.Button(base, text="Predict",command=helloCallBack, width=10).place(x=300, y=480)

base.mainloop()