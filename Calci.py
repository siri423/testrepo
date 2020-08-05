from tkinter import *
import math
import parser
import tkinter.messagebox

window = Tk()

exp = ""

# Gets the requested values of the height and widht.
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)
 
# Gets both half the screen width/height and window width/height
positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
window.geometry("+{}+{}".format(325, 225))

window.configure(background = "ivory3")

#window.geometry("325x125")

def press(num):
    global exp
    exp = exp + str(num)
    e1_val.set(exp)


def converter():
    try:
        global exp
        total = str(eval(exp))
        e1_val.set(total)
        exp = ""
    except NameError:
        exp = "math." + exp
        t = str(eval(exp))
        e1_val.set(t)
        exp = ""
        #e1_val.set("error")
        #exp = ""
    
def clear():
    try:
        global exp
        exp = exp[:-1]
        e1_val.set(exp)
    except:
        pass

def clearExp():
    try:
        global exp
        exp = ""
        e1_val.set(exp)
    except:
        pass
    

l1= Label(window , text = "Calculator", height = 1 , width = 36)
l1.grid(row = 0 , column = 0 , columnspan = 4 , pady = 5)

e1_val = StringVar()
e1 = Entry(window , textvariable = e1_val , width = 43)
e1.grid(row = 1 , column = 0 , columnspan = 4 , pady = 5)


b1 = Button(window, text = " C " , command = clear, height = 1 , width = 7)
b1.grid(row = 2 , column = 0 , pady = 5 , padx = 5)

b2 = Button(window, text = "AC" , command = clearExp, height = 1 , width = 7)
b2.grid(row = 2 , column = 1 , pady = 5 ,padx = 5)

b3 = Button(window, text = " / " , command = lambda : press("/"), height = 1 , width = 7)
b3.grid(row = 2 , column = 2 , pady = 5 , padx = 5)

b4 = Button(window, text = " X " , command = lambda : press("*"), height = 1 , width = 7)
b4.grid(row = 2 , column = 3 , pady = 5,padx = 5)

b5 = Button(window, text = " 7 " , command = lambda : press(7), height = 1 , width = 7)
b5.grid(row = 3 , column = 0 , pady = 5 , padx = 5)

b6 = Button(window, text = " 8 " , command = lambda : press(8), height = 1 , width = 7)
b6.grid(row = 3 , column = 1 , pady = 5 , padx = 5)

b7 = Button(window, text = " 9 " , command = lambda : press(9), height = 1 , width = 7)
b7.grid(row = 3 , column = 2 , pady = 5 , padx = 5)

b8 = Button(window, text = " - " , command = lambda : press("-"), height = 1 , width = 7)
b8.grid(row = 3 , column = 3 , pady = 5 , padx = 5)

b9 = Button(window, text = " 4 " , command = lambda : press(4), height = 1 , width = 7)
b9.grid(row = 4 , column = 0 , pady = 5 , padx = 5)

b10 = Button(window, text = " 5 " , command = lambda : press(5), height = 1 , width = 7)
b10.grid(row = 4 , column = 1 , pady = 5 , padx = 5)

b11 = Button(window, text = " 6 " , command = lambda : press(6), height = 1 , width = 7)
b11.grid(row = 4 , column = 2 , pady = 5 , padx = 5)

b12 = Button(window, text = " + " , command = lambda : press("+"), height = 1 , width = 7)
b12.grid(row = 4 , column = 3 , pady = 5 , padx = 5)

b13 = Button(window, text = " 1 " , command = lambda : press(1), height = 1 , width = 7)
b13.grid(row = 5 , column = 0 , pady = 5 , padx = 5)

b14 = Button(window, text = " 2 " , command = lambda : press(2), height = 1 , width = 7)
b14.grid(row = 5 , column = 1 , pady = 5 , padx = 5)

b15 = Button(window, text = " 3 " , command = lambda : press(3), height = 1 , width = 7)
b15.grid(row = 5 , column = 2 , pady = 5 , padx = 5)

b16 = Button(window, text = "+/-" , command = lambda : press("+/-"), height = 1 , width = 7)
b16.grid(row = 5 , column = 3 , pady = 5 , padx = 5)

b17 = Button(window, text = "      0      " , command = lambda : press(0), height = 1 , width = 17)
b17.grid(row = 6 , column = 0 , columnspan = 2 , pady = 5 , padx = 5)

b18 = Button(window, text = "  .  " , command = lambda : press("."), height = 1 , width = 7)
b18.grid(row = 6 , column = 2 , pady = 5 , padx = 5)

b19 = Button(window, text = "  =  " , command = converter, height = 1 , width = 7)
b19.grid(row = 6 , column = 3 , pady = 5 , padx = 5)

#trigonometric functions

b20 = Button(window, text = "  sin  " , command = lambda : press("sin"), height = 1 , width = 7)
b20.grid(row = 7 , column = 0 , pady = 5 , padx = 5)

b21 = Button(window, text = "  cos  " , command = lambda : press("cos"), height = 1 , width = 7)
b21.grid(row = 7 , column = 1 , pady = 5 , padx = 5)

b22 = Button(window, text = "  tan  " , command = lambda : press("tan"), height = 1 , width = 7)
b22.grid(row = 7 , column = 2 , pady = 5 , padx = 5)

b23 = Button(window, text = "  sinh  " , command = lambda : press("sinh"), height = 1 , width = 7)
b23.grid(row = 7 , column = 3 , pady = 5 , padx = 5)

b24 = Button(window, text = "  cosh  " , command = lambda : press("cosh"), height = 1 , width = 7)
b24.grid(row = 8 , column = 0 , pady = 5 , padx = 5)

b25 = Button(window, text = "  tanh " , command = lambda : press("tanh"), height = 1 , width = 7)
b25.grid(row = 8 , column = 1 , pady = 5 , padx = 5)

b21 = Button(window, text = "  (  " , command = lambda : press("("), height = 1 , width = 7)
b21.grid(row = 8 , column = 2 , pady = 5 , padx = 5)

b22 = Button(window, text = "  )  " , command = lambda : press(")"), height = 1 , width = 7)
b22.grid(row = 8 , column = 3 , pady = 5 , padx = 5)

b23 = Button(window, text = "  pi  " , command = lambda : press("pi"), height = 1 , width = 7)
b23.grid(row = 9 , column = 0 , pady = 5 , padx = 5)

b24 = Button(window, text = "  square  " , command = lambda : press("**2"), height = 1 , width = 7)
b24.grid(row = 9 , column = 1 , pady = 5 , padx = 5)

b25 = Button(window, text = "  cube  " , command = lambda : press("**3"), height = 1 , width = 7)
b25.grid(row = 9 , column = 2 , pady = 5 , padx = 5)

b26 = Button(window, text = "  10^x  " , command = lambda : press("10**"), height = 1 , width = 7)
b26.grid(row = 9 , column = 3 , pady = 5 , padx = 5)

b27 = Button(window, text = "  x^y  " , command = lambda : press("**"), height = 1 , width = 7)
b27.grid(row = 10 , column = 0 , pady = 5 , padx = 5)

b28 = Button(window, text = "   sqrt " , command = lambda : press("sqrt"), height = 1 , width = 7)
b28.grid(row = 10 , column = 1 , pady = 5 , padx = 5)

b29 = Button(window, text = "  cuberoot  " , command = lambda : press("**1/3"), height = 1 , width = 7)
b29.grid(row = 10 , column = 2 , pady = 5 , padx = 5)

b30 = Button(window, text = "  1/x  " , command = lambda : press("1/"), height = 1 , width = 7)
b30.grid(row = 10 , column = 3 , pady = 5 , padx = 5)

b31 = Button(window, text = "  e  " , command = lambda : press("e"), height = 1 , width = 7)
b31.grid(row = 11 , column = 0 , pady = 5 , padx = 5)

b32 = Button(window, text = "x root y" , command = lambda : press("**1/"), height = 1 , width = 7)
b32.grid(row = 11 , column = 1 , pady = 5 , padx = 5)

b33 = Button(window, text = "  ln  " , command = lambda : press("log"), height = 1 , width = 7)
b33.grid(row = 11 , column = 2 , pady = 5 , padx = 5)

window.mainloop()