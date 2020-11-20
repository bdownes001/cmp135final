# Brian Downes
# CMP-135-D01
# December 13th 2020
# https://github.com/bdownes001/cmp135final
import random
from collections import Counter

users_favorite = []
player_win = 0
ai_win = 0
tie_win = 0
weapon_type = ["r", "p", "s"]


def game_instructions():
    print("-----------------------------------\n\t\t\t\tHelp\n-----------------------------------")
    print("Use the terminal to enter a weapon")
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
    used_weapons = Counter(users_favorite)
    print("GAME OVER!\nThanks For Playing!")
    print("==============================")
    print(f"Player wins: {player_win}")
    print(f"Computer wins: {ai_win}")
    print(f"Tie games: {tie_win}")
    print(f"Weapons used:")
    for w in used_weapons:  # Loop though used_weapon list
        print(f"{w} : {used_weapons[w]}")


game_menu()

while True:
    ai_weapon = random.choice(weapon_type)

    # Cheat to see AI's choice
    print(f"CHEAT: {ai_weapon}")

    player_weapon = str(input("Which Weapon do you choose: ")).lower()
    users_favorite.append(player_weapon)  # Append weapon to user_favorite weapon list

    if player_weapon == 'q':
        users_favorite.pop()
        game_over()
        break
    elif player_weapon == 'help':
        users_favorite.pop()
        game_instructions()
    elif player_weapon == ai_weapon:
        print(f"\nYour choice {player_weapon}\nComputer choice: {ai_weapon}.\nTIE\n")
        tie_win += 1
    elif player_weapon == 'r':  # Player chooses Rock
        if ai_weapon == 'p':  # AI chooses Paper
            print(f"\nYour choice {player_weapon}\nComputer choice: {ai_weapon}.\nYou LOSE\n")
            ai_win += 1
        else:
            print(f"\nYour choice {player_weapon}\nComputer choice: {ai_weapon}.\nYou WIN\n")
            player_win += 1
    elif player_weapon == 'p':  # Player chooses Paper
        if ai_weapon == 's':  # AI chooses Scissor
            print(f"\nYour choice {player_weapon}\nComputer choice: {ai_weapon}.\nYou LOSE\n")
            ai_win += 1
        else:
            print(f"\nYour choice {player_weapon}\nComputer choice: {ai_weapon}.\nYou WIN\n")
            player_win += 1
    elif player_weapon == 's':  # Player chooses Scissor
        if ai_weapon == 'r':  # AI chooses Rock
            print(f"\nYour choice {player_weapon}\nComputer choice: {ai_weapon}.\nYou LOSE\n")
            ai_win += 1
        else:
            print(f"\nYour choice {player_weapon}\nComputer choice: {ai_weapon}.\nYou WIN\n")
            player_win += 1
    else:
        print("Not an option. Try again")
        users_favorite.pop()


