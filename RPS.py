# Brian Downes
# CMP-135-D01
# December 13th 2020
# https://github.com/bdownes001/cmp135final
import random

Player_win = 0
AI_win = 0
tie_win = 0
Weapons = ["r", "p", "s"]


def game_instructions():
    print("-----------------------------------\n\t\t\t\tHelp\n-----------------------------------")
    print("'r' for Rock. 'p' for Paper and 's'\nfor Scissor")
    print("To quit the game, enter 'q' to exit")
    print("-----------------------------------\n")


def game_menu():
    print("-----------------------------------\n\t\t\t\tMenu\n-----------------------------------")
    print("Rock, Paper, Scissor.")
    print("Enter 'help' for game instructions.")
    print("Enter 'q' to exit game.")
    print("-----------------------------------\n")


def game_over():
    print("GAME OVER!\nThanks For Playing!")
    print("==============================")
    print(f"Player wins: {Player_win}")
    print(f"Computer wins: {AI_win}")
    print(f"Tie games: {tie_win}")


game_menu()

while True:
    # Menu
    AI_Weapon = random.choice(Weapons)
    # Cheat to see AI's choice
    print(f"CHEAT: {AI_Weapon}")
    Player_Weapon = str(input("Which Weapon do you choose: ")).lower()
    if Player_Weapon == 'q':
        game_over()
        break
    elif Player_Weapon == 'help':
        game_instructions()
    elif Player_Weapon == AI_Weapon:
        print(f"\nYour choice {Player_Weapon}\nComputer choice: {AI_Weapon}.\nTIE\n")
        tie_win += 1
    elif Player_Weapon == 'r':  # Player chooses Rock
        if AI_Weapon == 'p':  # AI chooses Paper
            print(f"\nYour choice {Player_Weapon}\nComputer choice: {AI_Weapon}.\nYou LOSE\n")
            AI_win += 1
        else:
            print(f"\nYour choice {Player_Weapon}\nComputer choice: {AI_Weapon}.\nYou WIN\n")
            Player_win += 1
    elif Player_Weapon == 'p':  # Player chooses Paper
        if AI_Weapon == 's':  # AI chooses Scissor
            print(f"\nYour choice {Player_Weapon}\nComputer choice: {AI_Weapon}.\nYou LOSE\n")
            AI_win += 1
        else:
            print(f"\nYour choice {Player_Weapon}\nComputer choice: {AI_Weapon}.\nYou WIN\n")
            Player_win += 1
    elif Player_Weapon == 's':  # Player chooses Scissor
        if AI_Weapon == 'r':  # AI chooses Rock
            print(f"\nYour choice {Player_Weapon}\nComputer choice: {AI_Weapon}.\nYou LOSE\n")
            AI_win += 1
        else:
            print(f"\nYour choice {Player_Weapon}\nComputer choice: {AI_Weapon}.\nYou WIN\n")
            Player_win += 1
    else:
        print("Not a weapon. Try again")
