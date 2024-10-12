from tkinter import*
from tkinter import messagebox

#function code
def bNine(number):
    display.insert(END,number)
def bEight(number):
    display.insert(END,number)
def bSeven(number):
    display.insert(END,number)
def bSix(number):
    display.insert(END,number)
def bFive(number):
    display.insert(END,number)
def bFour(number):
    display.insert(END,number)
def bThree(number):
    display.insert(END,number)
def bTwo(number):
    display.insert(END,number)
def bOne(number):
    display.insert(END,number)
def bZero(number):
    display.insert(END,number)

def handleDotPress(cal):
    display.insert(END,cal)

def clickPlus(cal):
    display.insert(END,cal)
def clickMax(cal):
    display.insert(END,cal)
def clickMin(cal):
    display.insert(END,cal)
def clickDiv(cal):
    display.insert(END,cal)



def answer():
    expression = display.get()
    try:
        result = eval(expression)  # Safely evaluate the expression
        display.delete(0, END)
        display.insert(END, str(result))  # Display the result in the entry box
    except ZeroDivisionError:
        messagebox.showerror('error',("a number can;t devid by zero....!!!"))
    except SyntaxError:
        messagebox.showerror('error',("invalid  calculation"))




def Clear():
    display.delete(0, END)

#interface code
root=Tk()
root.title('calculator')
root.geometry('300x300')
root.config(bg='brown')
root.resizable(0,0)







display=Entry(root,font=('arial,14,bold'),width=25)
display.grid(row=0,column=0,padx=35,pady=8,columnspan=4)

b9 = Button(root,text=(9),font=('times new romen',14,'bold'),width=4,cursor='hand2',relief=GROOVE,command=lambda:bNine('9'))
b9.grid(row=1,column=0)

b8 = Button(root,text=(8),font=('times new romen',14,'bold'),width=4,cursor='hand2',relief=GROOVE,command=lambda:bEight('8'))
b8.grid(row=1,column=1)

b7 = Button(root,text=(7),font=('times new romen',14,'bold'),width=4,cursor='hand2',relief=GROOVE,command=lambda:bSeven('7'))
b7.grid(row=1,column=2)

bPlus = Button(root,text='+',font=('times new romen',14,'bold'),width=4,cursor='hand2',relief=GROOVE,command=lambda:clickPlus('+'),bg='orange',fg='white')
bPlus.grid(row=1,column=3)


b6 = Button(root,text=(6),font=('times new romen',14,'bold'),width=4,cursor='hand2',relief=GROOVE,command=lambda:bSix('6'))
b6.grid(row=2,column=0,pady=5)

b5 = Button(root,text=(5),font=('times new romen',14,'bold'),width=4,cursor='hand2',relief=GROOVE,command=lambda:bFive('5'))
b5.grid(row=2,column=1,pady=5)

b4 = Button(root,text=(4),font=('times new romen',14,'bold'),width=4,cursor='hand2',relief=GROOVE,command=lambda:bFour('4'))
b4.grid(row=2,column=2,pady=5)

bMin = Button(root,text='-',font=('times new romen',14,'bold'),width=4,cursor='hand2',relief=GROOVE,command=lambda:clickMin('-'),bg='orange',fg='white')
bMin.grid(row=2,column=3,pady=5)

b3= Button(root,text=(3),font=('times new romen',14,'bold'),width=4,cursor='hand2',relief=GROOVE,command=lambda:bThree('3'))
b3.grid(row=3,column=0,pady=5)

b2 = Button(root,text=(2),font=('times new romen',14,'bold'),width=4,cursor='hand2',relief=GROOVE,command=lambda:bTwo('2'))
b2.grid(row=3,column=1,pady=5)

b1 = Button(root,text=(1),font=('times new romen',14,'bold'),width=4,cursor='hand2',relief=GROOVE,command=lambda:bOne('1'))
b1.grid(row=3,column=2,pady=5)

bMax = Button(root,text='*',font=('times new romen',14,'bold'),width=4,cursor='hand2',relief=GROOVE,command=lambda:clickMax('*'),bg='orange',fg='white')
bMax.grid(row=3,column=3,pady=5)

b0= Button(root,text=(0),font=('times new romen',14,'bold'),width=4,cursor='hand2',relief=GROOVE,command=lambda:bZero('0'))
b0.grid(row=4,column=0,pady=5)

bDot = Button(root,text=('.'),font=('times new romen',14,'bold'),width=4,cursor='hand2',relief=GROOVE,command=lambda:handleDotPress('.'))
bDot.grid(row=4,column=1,pady=5)

bClear = Button(root,text=('C'),font=('times new romen',14,'bold'),width=4,cursor='hand2',relief=GROOVE,command=Clear)
bClear.grid(row=4,column=2,pady=5)

bDiv = Button(root,text='/',font=('times new romen',14,'bold'),width=4,cursor='hand2',relief=GROOVE,command=lambda:clickDiv('/'),bg='orange',fg='white')
bDiv.grid(row=4,column=3,pady=5)

bEqual = Button(root,text='=',font=('times new romen',14,'bold'),width=20,cursor='hand2',relief=GROOVE,command=answer,bg='orange',fg='white')
bEqual.grid(row=5,column=0,pady=5,columnspan=4)




root.mainloop()

