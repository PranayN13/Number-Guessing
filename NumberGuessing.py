from tkinter import *
import random

ws = Tk()
ws.title('PythonGuides')
ws.geometry('600x400')
ws.config(bg='#080304')

ranNum = random.randint(0, 10)
chance = 5
var = IntVar()
disp = StringVar()

def Guess_Number():
    global ranNum
    global chance
    guess_input = var.get()
    if chance > 0:
        if guess_input == ranNum:
            msg = f'You won! {ranNum} is the right answer.'
        elif guess_input > ranNum:
            chance -= 1
            msg = f'{guess_input} is greater. You have {chance} attempt left.'
        elif guess_input < ranNum:
            chance -= 1
            msg = f'{guess_input} is smaller. You have {chance} attempt left.'
        else:
            msg = 'Something went wrong!'
    else:
        msg = f'You Lost! you have {chance} attempt left.'

    disp.set(msg)


Label(
    ws,
    text='Number Guessing Game',
    font=('roboto', 20),
    relief=SOLID,
    padx=10,
    pady=10,
    bg='#E87479'
).pack(pady=(10, 0))

Entry(
    ws,
    textvariable=var,
    font=('roboto', 18)
).pack(pady=(50, 10))

Button(
    ws,
    text='Submit Guess',
    font=('roboto', 18),
    command=Guess_Number
).pack()

Label(
    ws,
    textvariable=disp,
    bg='#000000',
    font=('roboto', 14)
).pack(pady=(20,0))


ws.mainloop()
