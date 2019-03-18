# Created by: Yusuf Moussa
# Created on: 22 Feb 2019
# Created for: ICS3U
# Daily Assignment Unit 3-01
# This is a guessing game program

from tkinter import *
import random


root = Tk()
root.geometry("400x200")
var = StringVar()

Label(root, text= "Welcome to the guessing game").pack()
Label(root, text= "Type in a number and press submit").pack()
Label(root, text= "Press the reset button to play again").pack()

computer_guess = random.randint(1, 100)

def game():
    user_guess = int(T_box.get())
    
    if user_guess == computer_guess:
        Label(root, text= "Correct").pack()
    elif user_guess < computer_guess:
        Label(root, text= "Higher").pack()
    elif user_guess > computer_guess:
        Label(root, text= "Lower").pack()
    else:
        Label(root, text= "Error").pack()     
        
def reset():
    global computer_guess
    computer_guess = random.randint(1, 100)
    Label(root, text= "Game has reset. Play again").pack()
                   

T_box = Entry(root)
T_box.pack()

sub_but = Button()
sub_but ["text"] = "Submit"
sub_but ["command"] = game
sub_but.pack()

reset_but = Button()
reset_but ["text"] = "Reset"
reset_but ["command"] = reset
reset_but.pack()

root.mainloop()




