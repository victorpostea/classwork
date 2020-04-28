# This game is based off of a mechanic in the popular game Counter Strike Global Offensive.
# In this game you can open loot boxes called "cases" for a flat rate of $2.49 USD. 
# In each of these lootboxes you can get items ranging from roughly 10 cents to items worth $30,000
# You can also battle your friends.
# I'm making a case battle game where each person playing opens 5 cases and whoever makes more money or loses the least wins!
# Prices are going to be based off of the "Danger Zone Case"
# (NOTE) all items are recieved in "Factory New" condition with prices based off of the steam community market (No Stattrak)

# INSTRUCTIONS
# Each gun has a color association making it more rare as the color goes warmer
# The colors go Blue-Purple-Pink-Red-Gold
# Gun Prices were last updated April 28, 2020
# Everything is in USD 
# Each open 5 cases whoever makes the most wins

import random

player1total = 0
player2total = 0
turns = 0
a = "MP9 | Modest Threat"               #Blue    0.26
b = "Glock-18 | Oxide Blaze"            #Blue    0.42
c = "Nova | Wood Fired"                 #Blue    0.19
d = "M4A4 | Magnesium"                  #Blue    2.11
e = "Sawed-Off | Black Sand"            #Blue    0.23
f = "SG 553 | Danger Close"             #Blue    0.46
g = "Tec-9 | Fubar"                     #Blue    0.64 (Item does not have a "Factory New" resort to "Minimal Wear")
h = "G3SG1 | Scavenger"                 #Purple  0.97
i = "Galil AR | Signal"                 #Purple  1.00
j = "MAC-10 | Pipe Down"                #Purple  1.34
k = "P250 | Nevermore"                  #Purple  1.03
l = "USP-S | Flashback"                 #Purple  1.57
m = "UMP-45 | Momentum"                 #Pink    7.38
n = "Desert Eagle | Mecha Industries"   #Pink    8.88
o = "MP5-SD | Phosphor"                 #Pink    8.66
p = "AK-47 | Asiimov"                   #Red     154.23
q = "AWP | Neo-Noir"                    #Red     49.86
r = "Exceedingly Rare Special Item"     #Gold    400 is average price for a knife from this case

# Blue 80%
# Purple 15%
# Pink 3%
# Red 1%
# Gold 1%
bluestring = "abcdefg"
purplestring = "hijkl"
pinkstring = "mno"
redstring = "pq"
goldstring = "r"

oddslist = [bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, bluestring, purplestring, purplestring, purplestring, purplestring, purplestring, purplestring, purplestring, purplestring, purplestring, purplestring, purplestring, purplestring, purplestring, purplestring, purplestring, pinkstring, pinkstring, pinkstring, redstring, goldstring]


while turns <= 9:

    if turns % 2 == 0:  # even
        print("Player 1's turn")
    else:  # odd
        print("Player 2's turn")

    
    input("Press ""Enter"" to open a danger zone case")
    roll = random.randrange(1, 100)
    color = oddslist[roll]

    gun = random.randrange(1,len(color) + 1)
    coloredgun = color[gun - 1:gun]

    if turns % 2 == 0: #Player 1
        if coloredgun == "a":
            print(f"You got a(n) {a}!")
            player1total += 0.26
        elif coloredgun == "b":
            print(f"You got a(n) {b}!")
            player1total += 0.42
        elif coloredgun == "c":
            print(f"You got a(n) {c}!")
            player1total += 0.19
        elif coloredgun == "d":
            print(f"You got a(n) {d}!")
            player1total += 2.11
        elif coloredgun == "e":
            print(f"You got a(n) {e}!")
            player1total += 0.23
        elif coloredgun == "f":
            print(f"You got a(n) {f}!")
            player1total += 0.46
        elif coloredgun == "g":
            print(f"You got a(n) {g}!")
            player1total += 0.64
        elif coloredgun == "h":
            print(f"You got a(n) {h}!")
            player1total += 0.97
        elif coloredgun == "i":
            print(f"You got a(n) {i}!")
            player1total += 1
        elif coloredgun == "j":
            print(f"You got a(n) {j}!")
            player1total += 1.34
        elif coloredgun == "k":
            print(f"You got a(n) {k}!")
            player1total += 1.03
        elif coloredgun == "l":
            print(f"You got a(n) {l}!")
            player1total += 1.57
        elif coloredgun == "m":
            print(f"You got a(n) {m}!")
            player1total += 7.38
        elif coloredgun == "n":
            print(f"You got a(n) {n}!")
            player1total += 8.88
        elif coloredgun == "o":
            print(f"You got a(n) {o}!")
            player1total += 8.66
        elif coloredgun == "p":
            print(f"You got a(n) {p}!")
            player1total += 154.23
        elif coloredgun == "q":
            print(f"You got a(n) {q}!")
            player1total += 49.86
        elif coloredgun == "r":
            print(f"You got a(n) {r}!")
            player1total += 400
    else: #Player 2
        if coloredgun == "a":
            print(f"You got a(n) {a}!")
            player2total += 0.26
        elif coloredgun == "b":
            print(f"You got a(n) {b}!")
            player2total += 0.42
        elif coloredgun == "c":
            print(f"You got a(n) {c}!")
            player2total += 0.19
        elif coloredgun == "d":
            print(f"You got a(n) {d}!")
            player2total += 2.11
        elif coloredgun == "e":
            print(f"You got a(n) {e}!")
            player2total += 0.23
        elif coloredgun == "f":
            print(f"You got a(n) {f}!")
            player2total += 0.46
        elif coloredgun == "g":
            print(f"You got a(n) {g}!")
            player2total += 0.64
        elif coloredgun == "h":
            print(f"You got a(n) {h}!")
            player2total += 0.97
        elif coloredgun == "i":
            print(f"You got a(n) {i}!")
            player2total += 1
        elif coloredgun == "j":
            print(f"You got a(n) {j}!")
            player2total += 1.34
        elif coloredgun == "k":
            print(f"You got a(n) {k}!")
            player2total += 1.03
        elif coloredgun == "l":
            print(f"You got a(n) {l}!")
            player2total += 1.57
        elif coloredgun == "m":
            print(f"You got a(n) {m}!")
            player2total += 7.38
        elif coloredgun == "n":
            print(f"You got a(n) {n}!")
            player2total += 8.88
        elif coloredgun == "o":
            print(f"You got a(n) {o}!")
            player2total += 8.66
        elif coloredgun == "p":
            print(f"You got a(n) {p}!")
            player2total += 154.23
        elif coloredgun == "q":
            print(f"You got a(n) {q}!")
            player2total += 49.86
        elif coloredgun == "r":
            print(f"You got a(n) {r}!")
            player2total += 400


    turns += 1

        
print(f"Player 1 made ${player1total} and spent $12.45, Player 2 made ${player2total} and also spent $12.45!")
if player1total > player2total:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
