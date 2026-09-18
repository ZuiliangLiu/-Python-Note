import random

#● ┌ ─ ┐ │ └ ┘
total = 0
"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"
dice_art = {1:("┌─────────┐",
               "│         │",
               "│    ●    │",
               "│         │",
               "└─────────┘"),
            2:("┌─────────┐",
               "│ ●       │",
               "│         │",
               "│       ● │",
               "└─────────┘"),
            3:("┌─────────┐",
               "│ ●       │",
               "│    ●    │",
               "│       ● │",
               "└─────────┘"),
            4:("┌─────────┐",
               "│ ●     ● │",
               "│         │",
               "│ ●     ● │",
               "└─────────┘"),
            5:("┌─────────┐",
               "│ ●     ● │",
               "│    ●    │",
               "│ ●     ● │",
               "└─────────┘"),
            6:("┌─────────┐",
               "│ ●     ● │",
               "│ ●     ● │",
               "│ ●     ● │",
               "└─────────┘")}

die_num =int(input("How many dice do you want to roll?:"))

dice = []
for number in range(die_num):
    dice_value = random.randint(1, 6)
    dice.append(dice_value)
for art_num in range(die_num):
    for picture in dice_art.get(dice[art_num]):
        print(picture)

for value in dice:
    total +=value

print(f"You final total score is {total}")

