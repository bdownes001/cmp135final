# Brian Downes
# CMP-135-D01
# December 13th 2020
import random

print("Rock (r), Paper (p), Scissors (s) Game.")
print("Enter 'q' to exit game.")
Weapons = ["r", "p", "s"]

while True:
    AI_Weapon = random.choice(Weapons)
    # CHEAT TO SEE AI WEAPON
    print(f"Computer chooses: {AI_Weapon}")
    Player_Weapon = str(input("Which Weapon do you choose: "))
    if Player_Weapon.lower() == 'q':
        break
    elif Player_Weapon.lower() == AI_Weapon:
        print("Tie")
    elif Player_Weapon.lower() == 'r':  # Player chooses Rock
        if AI_Weapon == 'p':  # AI chooses Paper
            print("You LOSE")
        else:
            print("You WIN")
    elif Player_Weapon.lower() == 'p':  # Player chooses Paper
        if AI_Weapon == 's':  # AI chooses Scissor
            print("You LOSE")
        else:
            print("You WIN")
    elif Player_Weapon.lower() == 's':  # Player chooses Scissor
        if AI_Weapon == 'r':  # AI chooses Rock
            print("You LOSE")
        else:
            print("You WIN")
    else:
        print("Not a weapon. Try again")

