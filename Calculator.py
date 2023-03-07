from tkinter import*
root= Tk()
root.title('LEPLA :-: Calculator')

#for the entry of numbers blank
e=Entry(root, width=39, borderwidth=5, bg='#97B299', fg='#2D4030')
e.grid(row=1, column=0, columnspan=5, padx=15, pady=15)

#for the icon
root.iconbitmap('D:/Icons/bush.ico')

#for the status bar
status= Label(root, text='root : WELCOME TO LEPLA : MAKING TOMORROW BRIGHTER\Calculator', bd=2, relief=SUNKEN, bg='#F5AD8C')

#function for addition and reverting the numbers and deleting after
def buttonadd(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))

#function for clearing the whole equation
def buttonclear():
    e.delete(0, END)

#function getting the first number for addition
def buttonaddadddef():
    firstnumber=e.get()
    global f_num
    f_num=int(firstnumber)
    e.delete(0, END)

#function getting the second number for addition
def buttonaddequaldef():
    secondnumber=e.get()
    e.delete(0, END)
    e.insert(0, str(f_num + int(secondnumber)))

#making buttons on the calculator
button1= Button(root, text='1', padx=60, pady=20, command=lambda: buttonadd(1), bg='#97B299', fg='#2D4030')
button2= Button(root, text='2', padx=60, pady=20, command=lambda: buttonadd(2), bg='#97B299', fg='#2D4030')
button3= Button(root, text='3', padx=61, pady=20, command=lambda: buttonadd(3), bg='#97B299', fg='#2D4030')
button4= Button(root, text='4', padx=60, pady=20, command=lambda: buttonadd(4), bg='#97B299', fg='#2D4030')
button5= Button(root, text='5', padx=60, pady=20, command=lambda: buttonadd(5), bg='#97B299', fg='#2D4030')
button6= Button(root, text='6', padx=61, pady=20, command=lambda: buttonadd(6), bg='#97B299', fg='#2D4030')
button7= Button(root, text='7', padx=60, pady=20, command=lambda: buttonadd(7), bg='#97B299', fg='#2D4030')
button8= Button(root, text='8', padx=60, pady=20, command=lambda: buttonadd(8), bg='#97B299', fg='#2D4030')
button9= Button(root, text='9', padx=61, pady=20, command=lambda: buttonadd(9), bg='#97B299', fg='#2D4030')
button0= Button(root, text='0', padx=60, pady=20, command=lambda: buttonadd(0), bg='#97B299', fg='#2D4030')
buttonaddi= Button(root, text='+', padx=60, pady=20, command=buttonaddadddef, bg='#97B299', fg='#2D4030')
buttonequal= Button(root,text='=', padx=129, pady=20, command=buttonaddequaldef, bg='#97B299', fg='#2D4030')
buttonclear= Button(root,text='CLEAR', padx=115, pady=20, command=buttonclear, bg='#97B299', fg='#2D4030')


#puting the buttons on the grid using the tkinter grid system for 5th row
button1.grid(row=4 ,column=0)
button2.grid(row=4 ,column=1)
button3.grid(row=4 ,column=2)

#puting the buttons on the grid using the tkinter grid system for 4th row
button4.grid(row=3 ,column=0)
button5.grid(row=3 ,column=1)
button6.grid(row=3 ,column=2)

#puting the buttons on the grid using the tkinter grid system for 3th row
button7.grid(row=2 ,column=0)
button8.grid(row=2 ,column=1)
button9.grid(row=2 ,column=2)

#puting the buttons on the grid using the tkinter grid system for 6th row
button0.grid(row=5 ,column=0)
buttonclear.grid(row=5 ,column=1, columnspan=2)

#puting the buttons on the grid using the tkinter grid system for 7th row
buttonaddi.grid(row=6 ,column=0)
buttonequal.grid(row=6 ,column=1, columnspan=2)

#status bar grid.
status.grid(row=0, column=0, columnspan=3, sticky=W+E)

#the background of window
root.configure(bg='#E7D7CB')
root.mainloop()
