# Import libraries
from tkinter import *
from tkinter import ttk

# Colors
black = '#292827'
gray = '#333230'
orange = '#f5b70f'
white = '#feffff'

window = Tk()
window.resizable(width=False, height=False)
window.title("Calculadora")

# Window configuration
window.geometry('471x517') # width and height
window.config(bg=black)

# Frames
frame_display = Frame(window, width=471, height=100, bg=black)
frame_display.grid(row=0, column=0)

frame_buttons = Frame(window, width=471, height=418, bg=black)
frame_buttons.grid(row=1, column=0)

# Logic
all_values = ''
def entry(event):
    global all_values 
    all_values += str(event)
    values.set(all_values)

def calculate():
    try:
        global all_values
        all_values = all_values.replace('x', '*')
        all_values = all_values.replace('÷', '/')
        result = eval(all_values)
        values.set(result)
        all_values = str(result)
    except ZeroDivisionError:
        values.set('Zero divison')
        all_values = ''
    except SyntaxError:
        values.set('Invalid equation')
        all_values = ''

def cleard():
    global all_values
    all_values = ''
    values.set('')
    
# Labels
values = StringVar()
app_label = Label(frame_display, textvariable=values, width=21, height=3, bg=black, fg=white, font='Ivy 18 bold', padx=7, relief=FLAT, anchor='e', justify=RIGHT)
app_label.place(x=0, y=0)

# Buttons
# Row 1
clear = Button(frame_buttons, command=cleard, text='C', width=18, height=3, bg=gray, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
clear.place(x=0, y=1)
module = Button(frame_buttons, command=lambda: entry('%'), text='%', width=7, height=3, bg=gray, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
module.place(x=234, y=1)
div = Button(frame_buttons, command=lambda: entry('÷'), text='÷', width=7, height=3, bg=orange, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
div.place(x=351, y=1)
# Row 2
seven = Button(frame_buttons, command=lambda: entry('7'), text='7', width=7, height=3, bg=gray, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
seven.place(x=0, y=84)
eight = Button(frame_buttons, command=lambda: entry('8'), text='8', width=7, height=3, bg=gray, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
eight.place(x=117, y=84)
nine = Button(frame_buttons, command=lambda: entry('9'), text='9', width=7, height=3, bg=gray, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
nine.place(x=234, y=84)
times = Button(frame_buttons, command=lambda: entry('x'), text='x', width=7, height=3, bg=orange, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
times.place(x=351, y=84)
# Row 3
four = Button(frame_buttons, command=lambda: entry('4'), text='4', width=7, height=3, bg=gray, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
four.place(x=0, y=167)
five = Button(frame_buttons, command=lambda: entry('5'), text='5', width=7, height=3, bg=gray, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
five.place(x=117, y=167)
six = Button(frame_buttons, command=lambda: entry('6'), text='6', width=7, height=3, bg=gray, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
six.place(x=234, y=167)
minus = Button(frame_buttons, command=lambda: entry('-'), text='-', width=7, height=3, bg=orange, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
minus.place(x=351, y=167)
# Row 4
one = Button(frame_buttons, command=lambda: entry('1'), text='1', width=7, height=3, bg=gray, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
one.place(x=0, y=250)
two = Button(frame_buttons, command=lambda: entry('2'), text='2', width=7, height=3, bg=gray, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
two.place(x=117, y=250)
three = Button(frame_buttons, command=lambda: entry('3'), text='3', width=7, height=3, bg=gray, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
three.place(x=234, y=250)
plus = Button(frame_buttons, command=lambda: entry('+'), text='+', width=7, height=3, bg=orange, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
plus.place(x=351, y=250)
# Row 5
zero = Button(frame_buttons, command=lambda: entry('0'), text='0', width=18, height=3, bg=gray, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
zero.place(x=0, y=333)
dot = Button(frame_buttons, command=lambda: entry('.'), text='.', width=7, height=3, bg=gray, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
dot.place(x=234, y=333)
atrib = Button(frame_buttons, command=calculate, text='=', width=7, height=3, bg=orange, fg=white, font='Ivy 11 bold', relief=RAISED, overrelief=RIDGE)
atrib.place(x=351, y=333)

# Execute
window.mainloop()