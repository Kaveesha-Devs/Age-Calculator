from tkinter import*
from datetime import date 

root = Tk()
root.geometry("800*600")
root.resizable(False,False)
root.title("Age Calculator")

photo=PhotoImage(file="Age calculator.png")
myimage=Label(image=photo)
myimage.pack(padx=15,pady=15)

Label(text="Name",font=23).place(x=200,y=250)
Label(text="Year",font=23).place(x=200,y=300)
Label(text="Month",font=23).place(x=200,y=350)
Label(text="Day",font=23).place(x=200,y=400)

nameValue=StringVar()
YearValue=StringVar()
MonthValue=StringVar()
DayValue=StringVar()

nameEntry=Entry(root,textvariable=nameValue,width=30,bd=3,font=20)
nameEntry.place(x=300,y=250)

YearEntry=Entry(root,textvariable=YearValue,width=30,bd=3,font=20)
YearEntry.place(x=300,y=300)

MonthEntry=Entry(root,textvariable=MonthValue,width=30,bd=3,font=20)
MonthEntry.place(x=300,y=350)

DayEntry=Entry(root,textvariable=DayValue,width=30,bd=3,font=20)
DayEntry.place(x=300,y=400)

root.mainloop()