from tkinter import *
from PIL import Image, ImageTk
from random import randint


root = Tk()
root.title("Rock Scissors Paper")
root.configure(background="#9b59b6")


rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))


user_score = 0
computer_score = 0
round_counter = 0


user_label = Label(root, image=scissor_img, bg="#9b59b6")
comp_label = Label(root, image=scissor_img_comp, bg="#9b59b6")
comp_label.grid(row=1, column=1, padx=20, pady=20)
user_label.grid(row=1, column=3, padx=20, pady=20)

playerScore = Label(root, text=user_score, font=("Arial", 40, "bold"), bg="#9b59b6", fg="white")
computerScore = Label(root, text=computer_score, font=("Arial", 40, "bold"), bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=2)
playerScore.grid(row=1, column=4)

user_indicator = Label(root, font=("Arial", 20, "bold"), text=": USER :", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=("Arial", 20, "bold"), text=": COMPUTER :", bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=4, padx=20)
comp_indicator.grid(row=0, column=2, padx=20)

msg = Label(root, font=("Arial", 20, "bold"), bg="#9b59b6", fg="white")
msg.grid(row=3, column=2, columnspan=2, pady=20)

round_label = Label(root, font=("Arial", 16, "bold"), text="Rounds Played: 0", bg="#9b59b6", fg="white")
round_label.grid(row=4, column=2, columnspan=2, pady=10)


def updateMessage(x):
    msg['text'] = x


def updateUserScore():
    global user_score
    user_score += 1
    playerScore.config(text=str(user_score))

def updateCompScore():
    global computer_score
    computer_score += 1
    computerScore.config(text=str(computer_score))


def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lose!!!")
            updateCompScore()
        else:
            updateMessage("You win!!!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You lose!!!")
            updateCompScore()
        else:
            updateMessage("You win!!!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You lose!!!")
            updateCompScore()
        else:
            updateMessage("You win!!!")
            updateUserScore()


def updateChoice(x):
    global round_counter
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)
    
    round_counter += 1
    round_label.config(text=f"Rounds Played: {round_counter}")


choices = ["rock", "paper", "scissor"]


rock = Button(root, width=20, height=2, font=("Arial", 10, "bold"), text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock"))
rock.grid(row=2, column=1, padx=10, pady=10)
paper = Button(root, width=20, height=2, font=("Arial", 10, "bold"), text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("paper"))
paper.grid(row=2, column=2, padx=10, pady=10)
scissor = Button(root, width=20, height=2, font=("Arial", 10, "bold"), text="SCISSOR",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor"))
scissor.grid(row=2, column=3, padx=10, pady=10)


def reset_game():
    global user_score, computer_score, round_counter
    user_score = 0
    computer_score = 0
    round_counter = 0
    playerScore.config(text=str(user_score))
    computerScore.config(text=str(computer_score))
    round_label.config(text=f"Rounds Played: {round_counter}")
    user_label.configure(image=scissor_img)
    comp_label.configure(image=scissor_img_comp)
    updateMessage("Make your choice!")


reset_button = Button(root, text="Reset Game", font=("Arial", 12, "bold"), bg="#2ECC71", fg="white", command=reset_game)
reset_button.grid(row=5, column=2, pady=20)


root.mainloop()