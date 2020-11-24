# Brian Downes
# CMP-135-D01
# December 13th 2020
# https://github.com/bdownes001/cmp135final
import random


player_weapons = {'r': 0, 'p': 0, 's': 0}
player_win = 0
cpu_win = 0
tie_win = 0
weapon_type = ["r", "p", "s"]


def game_instructions():
    print("-----------------------------------\n\t\tHelp\n-----------------------------------")
    print("Use the terminal to enter a weapon")
    print("'r' for Rock. 'p' for Paper and 's'\nfor Scissor")
    print("To quit the game, enter 'q' to exit")
    print("-----------------------------------\n")


def game_menu():
    print("-----------------------------------\n\t\tMenu\n-----------------------------------")
    print("Welcome to Rock, Paper, Scissor.")
    print("Enter 'help' for game instructions.")
    print("Enter 'q' to exit game.")
    print("-----------------------------------\n")


def game_over():
    print("GAME OVER!\nThanks For Playing!")
    print("==============================")
    print(f"Player wins: {player_win}")
    print(f"Computer wins: {cpu_win}")
    print(f"Tie games: {tie_win}")
    print(f"Weapons used:")
    for k, v in player_weapons.items():
        print(f"{k}: {v}")


def get_player_choice():
    player = str(input("Which Weapon do you choose: ")).lower()
    # Keep track of weapons used
    if player == 'r':
        player_weapons['r'] += 1
    elif player == 'p':
        player_weapons['p'] += 1
    elif player == 's':
        player_weapons['s'] += 1

    return player


def get_cpu_random_choice():
    cpu_choice = random.choice(weapon_type)
    return cpu_choice


def get_cpu_choice():
    cpu_choice = get_cpu_random_choice()
    # Cheat to see computers choice
    # print(f"CHEAT: {cpu}")
    # ---------------------------------CPU choice based on Players history(hopefully)-----------------------------------
    if player_weapons['r'] == 0 and player_weapons['p'] == 0 and player_weapons['s'] == 0:  # I don't think I need you
        return get_cpu_random_choice()  # might delete
    else:
        if player_weapons['r'] > player_weapons['p'] and player_weapons['r'] > player_weapons['s']:
            cpu_choice = 'p'
            return cpu_choice
        elif player_weapons['p'] > player_weapons['r'] and player_weapons['p'] > player_weapons['s']:
            cpu_choice = 's'
            return cpu_choice
        elif player_weapons['s'] > player_weapons['p'] and player_weapons['s'] > player_weapons['r']:
            cpu_choice = 'r'
            return cpu_choice
        return cpu_choice


def game_start():
    while True:
        global cpu_win, player_win, tie_win  # Are we not already global outside this function???????
        player_weapon = get_player_choice()
        cpu_weapon = get_cpu_choice()

        if player_weapon == 'q':
            game_over()
            break
        elif player_weapon == 'help':
            game_instructions()
        # --------------------------------------------Lose--------------------------------------
        elif player_weapon == 'r' and cpu_weapon == 'p':
            print(f"\nYour choice: {player_weapon}\nComputer choice: {cpu_weapon}.\nYou LOSE\n")
            cpu_win += 1
        elif player_weapon == 'p' and cpu_weapon == 's':
            print(f"\nYour choice: {player_weapon}\nComputer choice: {cpu_weapon}.\nYou LOSE\n")
            cpu_win += 1
        elif player_weapon == 's' and cpu_weapon == 'r':
            print(f"\nYour choice: {player_weapon}\nComputer choice: {cpu_weapon}.\nYou LOSE\n")
            cpu_win += 1
        # --------------------------------------------Win--------------------------------------
        elif player_weapon == 'r' and cpu_weapon == 's':
            print(f"\nYour choice: {player_weapon}\nComputer choice: {cpu_weapon}.\nYou WIN\n")
            player_win += 1
        elif player_weapon == 'p' and cpu_weapon == 'r':
            print(f"\nYour choice: {player_weapon}\nComputer choice: {cpu_weapon}.\nYou WIN\n")
            player_win += 1
        elif player_weapon == 's' and cpu_weapon == 'p':
            print(f"\nYour choice: {player_weapon}\nComputer choice: {cpu_weapon}.\nYou WIN\n")
            player_win += 1
        # --------------------------------------------Tie--------------------------------------
        elif player_weapon == cpu_weapon:
            print(f"\nYour choice: {player_weapon}\nComputer choice: {cpu_weapon}.\nTIE\n")
            tie_win += 1
        else:
            print("Not an option. Try again")


game_menu()
game_start()
