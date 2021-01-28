
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************''')

print("\t\t\t""*********Welcome to the Treasure Island Game.*********""\n""You have to find the Treasure.")

choice1 = input("You are in a Deserted Island. Which path do you want to take? Left, Right or Straight?""\n")

if choice1 == "left":
    choice2 = input("You have come near a shore and found a boat. You also can climb cliff. What do you want to do? Type 'Swim' to swim or type 'Climb' to climb.""\n")
    if choice2 == "swim":
        print(input("You decided to swim and got surrounded by sharks.""\n""Game Over!"))
    if choice2 == "climb":
        print (input("You have Climbed Cliff and found a rope! You climbed down and found the Treasure!""\n""Congratulations! You Won!"))
if choice1 == "straight":
    path_choice2 = input("You fell into a hole and woke up in a Dungeon. You saw 3 Doors. Red, Blue and Black! Which door do you want to open?""\n")
    if path_choice2 == "red":
        print(input("You opened the Red Door and got attacked by a Angry Bear.""\n""Game Over!"))
    if path_choice2 == "blue":
        print(input("You opened the Blue Door and found the Treasure.""\n""Congratulation! You Won!"))
    if path_choice2 == "black":
        print (input("You opened the Black Door and got attacked by a Anaconda!""\n""Game Over!"))
if choice1 == "right":
    print(input("You fell into a swamp and got eaten by a Crocodile""\n""Game Over!"))