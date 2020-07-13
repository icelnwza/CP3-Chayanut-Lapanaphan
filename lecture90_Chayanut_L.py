from tkinter import *
import math


def calBMI(event):
    resultCal = float(BoxWeight.get())/(math.pow(float(BoxHeight.get())/100,2))
    if resultCal >= 30:
        print("อ้วนมากกกก",resultCal)
        labelResult.configure(text="อ้วนมากกกก",font = ("Angsana,10"),fg = "red")
    elif resultCal < 30 and resultCal >=25:
        print("อ้วน", resultCal)
        labelResult.configure(text="อ้วน", font=("Angsana,10"),fg = "red")
    elif resultCal < 25 and resultCal >= 23:
        print("น้ำหนักเกิน", resultCal)
        labelResult.configure(text="น้ำหนักเกิน", font=("Angsana,10"),fg = "red")
    elif resultCal < 23 and resultCal >= 18.6:
        print("น้ำหนักเหมาะสม", resultCal)
        labelResult.configure(text="น้ำหนักเหมาะสม", font=("Angsana,10"),fg = "red")
    else:
        print("ผอมเกิน", resultCal)
        labelResult.configure(text="ผอมเกิน", font=("Angsana,10"),fg = "red")


mainWindow = Tk()
lablelHeight = Label(text="ส่วนสูง (Cm.)",font = ("Angsana,12"))
lablelHeight.grid(row = 0,column =0)
BoxHeight = Entry(mainWindow)
BoxHeight.grid(row = 0,column = 1)

lableWeight = Label(text="น้ำหนัก (Kg.)",font = ("Angsana,12"))
lableWeight.grid(row = 1,column = 0)
BoxWeight = Entry(mainWindow)
BoxWeight.grid(row = 1,column = 1)

button = Button(text = "คำนวณ",font = ("Angsana,12"))
button.bind('<Button-1>', calBMI)
button.grid(row = 2)

labelResult=Label(mainWindow)
labelResult.grid(row = 2,column = 1)

mainWindow.mainloop()