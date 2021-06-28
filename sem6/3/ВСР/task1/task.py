from tkinter import *
import tkinter.messagebox



field = [0, 0, 0, 0, 0, 0, 0, 0, 0] 
XO = 1
numButton = [] 


def close_window(event):
    root.destroy()


def begin(event):
    global butn
    global field
    global numButton
    for b in butn:
        b.config(bg="#84e87c",text = '')
    field = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    numButton = []
    
       
def logic():
    global field
    global numButton
    if len(numButton) == 9:
        tkinter.messagebox.showinfo("Конец игры", "  Ничья!!!  ")
    else:
        end = False
        if field[0] == field[1] == field[2] > 0:
            winner = field[0]
            end = True
        elif field[3] == field[4] == field[5] > 0:
            winner = field[3]
            end = True
        elif field[6] == field[7] == field[8] > 0:
            winner = field[6]
            end = True
        elif field[0] == field[3] == field[6] > 0:
            winner = field[0]
            end = True
        elif field[1] == field[4] == field[7] > 0:
            winner = field[1]
            end = True
        elif field[2] == field[5] == field[8] > 0:
            winner = field[2]
            end = True
        elif field[0] == field[4] == field[8] > 0:
            winner = field[0]
            end = True
        elif field[2] == field[4] == field[6] > 0:
            winner = field[2]
            end = True
        if end:
            if winner == 1:
                user = "Нолик"
            elif winner == 2:
                user = "Крестик"
            tkinter.messagebox.showinfo("Конец игры", "Выиграл " + user)
            begin(None)


def click(button, num):
    global numButton
    if num not in numButton:
        global XO
        if XO == 1:
            button.config(text = 'O\nНолик')
            button.config(bg = '#64dcd1')
            field[num] = XO
            XO = 2
        else:
            button.config(text = 'X\nКрестик')
            button.config(bg = '#f17c80')
            field[num] = XO
            XO = 1
        numButton.append(num)
        logic()





root = Tk()
root.title("Крестики-нолики")
root.geometry("283x257")
root.resizable(False, False)

ris0 = Button(root, width=10, height=5, bg="#84e87c", command=lambda:click(ris0, 0))
ris0.grid(row=0, column=0)
ris1 = Button(root, width=10, height=5, bg="#84e87c", command=lambda:click(ris1, 1))
ris1.grid(row=0, column=1)
ris2 = Button(root, width=10, height=5, bg="#84e87c", command=lambda:click(ris2, 2))
ris2.grid(row=0, column=2)
ris3 = Button(root, width=10, height=5, bg="#84e87c", command=lambda:click(ris3, 3))
ris3.grid(row=1, column=0)
ris4 = Button(root, width=10, height=5, bg="#84e87c", command=lambda:click(ris4, 4))
ris4.grid(row=1, column=1)
ris5 = Button(root, width=10, height=5, bg="#84e87c", command=lambda:click(ris5, 5))
ris5.grid(row=1, column=2)
ris6 = Button(root, width=10, height=5, bg="#84e87c", command=lambda:click(ris6, 6))
ris6.grid(row=2, column=0)
ris7 = Button(root, width=10, height=5, bg="#84e87c", command=lambda:click(ris7, 7))
ris7.grid(row=2, column=1)
ris8 = Button(root, width=10, height=5, bg="#84e87c", command=lambda:click(ris8, 8))
ris8.grid(row=2, column=2)

butn = [ris0, ris1, ris2, ris3, ris4, ris5, ris6, ris7, ris8]

#функциональные клавиши
root.bind('<Escape>', close_window)
root.bind('<F12>', begin)

root.mainloop()