import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title('Andrew Kahuma Simple Calculator')
window.geometry('430x550+90+160')
window.resizable(False, False)
window.configure(bg='#17161b')

eqtn = ""

def show(value):
    global eqtn
    eqtn+=value
    label_result.config(text=eqtn)
    
def clear():
    global eqtn
    eqtn=""
    label_result.config(text=eqtn)
    
def equal():
    global eqtn
    result =""
    if eqtn != "":
        try:
            result = eval(eqtn)
        except:
            result = "Error"
            eqtn= ""
    label_result.config(text=result)

label_result = Label(window, width=25, height=2, text="", font=('arial', 30))
label_result.pack()

Button(window, text="C", width=4, height=1, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#3697f5',command=lambda: clear()).place(x=10, y=100)
Button(window, text="/", width=4, height=1, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#2a2d36', command=lambda: show("/")).place(x=110, y=100)
Button(window, text="%", width=4, height=1, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#2a2d36', command=lambda: show("%")).place(x=210, y=100)
Button(window, text="*", width=4, height=1, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#2a2d36', command=lambda: show("*")).place(x=320, y=100)

Button(window, text="7", width=4, height=1, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#2a2d36', command=lambda: show("7")).place(x=10, y=190)
Button(window, text="8", width=4, height=1, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#2a2d36', command=lambda: show("8")).place(x=110, y=190)
Button(window, text="9", width=4, height=1, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#2a2d36', command=lambda: show("9")).place(x=210, y=190)
Button(window, text="-", width=4, height=1, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#2a2d36', command=lambda: show("-")).place(x=320, y=190)

Button(window, text="4", width=4, height=1, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#2a2d36', command=lambda: show("4")).place(x=10, y=280)
Button(window, text="5", width=4, height=1, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#2a2d36', command=lambda: show("5")).place(x=110, y=280)
Button(window, text="6", width=4, height=1, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#2a2d36', command=lambda: show("6")).place(x=210, y=280)
Button(window, text="+", width=4, height=1, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#2a2d36', command=lambda: show("+")).place(x=320, y=280)

Button(window, text="1", width=4, height=1, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#2a2d36', command=lambda: show("1")).place(x=10, y=370)
Button(window, text="2", width=4, height=1, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#2a2d36', command=lambda: show("2")).place(x=110, y=370)
Button(window, text="3", width=4, height=1, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#2a2d36', command=lambda: show("3")).place(x=210, y=370)
Button(window, text="0", width=9, height=1, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#2a2d36', command=lambda: show("0")).place(x=10, y=460)

Button(window, text=".", width=4, height=1, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#2a2d36', command=lambda: show(".")).place(x=210, y=460)
Button(window, text="=", width=4, height=3, font=('arial',30,"bold"), bd= 1,  fg='#fff', bg = '#fe9037', command=lambda: equal()).place(x=320, y=370)


window.mainloop()