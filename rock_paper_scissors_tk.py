import random
from tkinter import Button, Entry, Label, StringVar, Tk

window = Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x200")

choices = ["rock", "paper", "scissors"]

user_choice = StringVar()
Label(window, text="Enter rock, paper, or scissors:").pack()
Entry(window, textvariable=user_choice).pack()


result = StringVar()


def play():
    user = user_choice.get().lower()

    if user not in choices:
        result.set("Invalid choice. Please enter rock, paper, or scissors.")
        return

    ai = random.choice(choices)
    if user == ai:
        result.set(f"It's a tie! You both chose {user}.")
    elif user == "rock" and ai == "scissors":
        result.set("You win! Rock beats scissors.")
    elif user == "paper" and ai == "rock":
        result.set("You win! Paper beats rock.")
    elif user == "scissors" and ai == "paper":
        result.set("You win! Scissors beats paper.")
    else:
        result.set(f"You lose! {ai} beats {user}.")


def reset():
    user_choice.set("")
    result.set("")


def exit():
    window.destroy()


Label(window, textvariable=result).pack()
Button(window, text="Play", command=play).pack()
Button(window, text="Reset", command=reset).pack()

window.mainloop()
