from tkinter import *
from tkinter import messagebox
import random as r
top = Tk()
top.geometry('336x400')
top.resizable(0, 0)
bef = Label(top, text = 'BEFORE ENTERING THE GAME')
ore = Label(top, text = 'PLEASE MENTION YOUR...')
bef.grid(row = 1, column = 1)
ore.grid(row = 2, column = 1)
name =Label(top, text = "Name")
name.grid(row = 3, column = 0)
name_entry = Entry(top, width = 30)
name_entry.grid(row = 3, column=1)
score=2


def button(frame):  # Function to define a button
    b = Button(frame, padx = 1, bg = "papaya whip", width = 3, text = "", font = ('arial', 40, 'bold'),
               relief = "sunken", bd = 5)
    return b


def change_a():  # Function to change the operand for the next player
    global a
    for i in ['O', 'X']:
        if not (i == a):
            a = i
            break


def reset():  # Resets the game
    global a
    for i in range(3):
        for j in range(3):
            b[i][j]["text"] = " "
            b[i][j]["state"] = NORMAL
    a = r.choice(['O', 'X'])


def check():  # Checks for victory or Draw
    global score
    for i in range(3):
        if b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] == a or b[0][i]["text"] == b[1][i]["text"]\
                == b[2][i]["text"] == a:
            messagebox.showinfo("Congrats!!", "'" + name_entry.get() + " ' has won")
            score+=1
            reset()
    if b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == a or b[0][2]["text"] == b[1][1]["text"] \
            == b[2][0]["text"] == a:
        messagebox.showinfo("Congrats!!", "'" + a + "' has won")

        reset()
    elif b[0][0]["state"] == b[0][1]["state"] == b[0][2]["state"] == b[1][0]["state"] == b[1][1]["state"]\
            == b[1][2]["state"] == b[2][0]["state"] == b[2][1]["state"] == b[2][2]["state"] == DISABLED:
        messagebox.showinfo("Tied!!", "The match ended in a draw")
        reset()


def click(row, col):

    b[row][col].config(text = a, state = DISABLED, disabledforeground = colour[a])
    check()
    change_a()
    label.config(text = a + "'s Chance")


# ##############   Main Program #################
def main():

    root = Toplevel()  # Window defined
    root.title("Tic-Tac-Toe")  # Title given
    root.geometry('336x400')
    root.resizable(0, 0)
    global a
    global b
    global colour
    global label
    a = r.choice(['O', 'X'])  # Two operators defined
    colour = {'O': "deep sky blue", 'X': "lawn green"}
    b = [[], [], []]
    for i in range(3):
        for j in range(3):
            b[i].append(button(root))
            b[i][j].config(command = lambda row=i, col=j: click(row, col))
            b[i][j].grid(row = i, column = j)
    label = Label(root, text = a + "'s Chance", font = ('arial', 10, 'bold'))
    label.grid(row = 3, column = 0, columnspan = 3)
    score_label = Label(root, text = name_entry.get()+' ' + 'SCORE:'+ str(score))
    score_label.grid(row = 4, column=0,columnspan=3)

    root.mainloop()


another_page = Button(top, text = 'Next', command=main)
another_page.grid(row = 8, column = 4)
top.mainloop()