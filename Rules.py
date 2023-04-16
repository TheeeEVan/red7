from Graphics import clear

styles = {
    "red": "\033[38;2;255;0;0m",
    "orange": "\033[38;2;255;128;0m",
    "yellow": "\033[38;2;255;255;0m",
    "green": "\033[38;2;0;255;0m",
    "blue": "\033[38;2;23;103;189m",
    "indigo": "\033[38;2;68;0;255m", 
    "violet": "\033[38;2;255;0;255m",
    "bold": "\033[1m",
    "reset": "\033[0m"
}

rules = {
    "red": "Highest Card",
    "orange": "Cards of One Number",
    "yellow": "Cards of One Color",
    "green": "Even Cards",
    "blue": "Cards of All Different Colors",
    "indigo": "Cards That Form a Run",
    "violet": "Cards Below 4"
}

# pretty much just a copy of rules.md
def tutorial():
    clear()
    print(f"{styles['bold']}Tutorial{styles['reset']} (Press Enter To Continue)")
    # cards
    print(f"{styles['bold']}The Cards:{styles['reset']}")
    print("There are 49 cards")
    print("Every card is assigned a number from 1-7")
    print(f"Every card is assigned a color ({styles['red']}red, {styles['orange']}orange, {styles['yellow']}yellow, {styles['green']}green, {styles['blue']}blue, {styles['indigo']}indigo, {styles['violet']}pink{styles['reset']})")
    input()
    clear()
    # card worth
    print(f"{styles['bold']}Tutorial{styles['reset']} (Press Enter To Continue)")
    print(f"{styles['bold']}Card Worth:{styles['reset']}")
    print(f"When comparing two cards, the card with the highest number will always be worth more.\nHowever, if both cards have the same number, the color which appears first in a rainbow ({styles['red']}red, {styles['orange']}orange, {styles['yellow']}yellow, {styles['green']}green, {styles['blue']}blue, {styles['indigo']}indigo, {styles['violet']}pink{styles['reset']}) is worth more.\nFor example a {styles['green']}Green 6{styles['reset']} is worth more than a {styles['blue']}Blue 6{styles['reset']}. This makes the {styles['red']}Red 7{styles['reset']} the highest valued card, and the {styles['violet']}Pink 1{styles['reset']} the lowest valued card.")
    input()
    clear()
    # winning
    print(f"{styles['bold']}Tutorial{styles['reset']} (Press Enter To Continue)")
    print(f"{styles['bold']}Winning:{styles['reset']}")
    print("At the end of every turn you must be winning. This is how to determine who is winning:\n")
    print("First, determine the current rule. The current rule is determined by the color of the card currently on top of the canvas. The rules for each color are:\n")
    for key in rules.keys():
        print(styles[key] + rules[key] + styles['reset'])
    print("\nNext, determine which player has the most cards that follow the current rule. If there is a tie, whoever has the highest card which follows the rule, wins.")
    input()
    clear()
    # a turn
    print(f"{styles['bold']}Tutorial{styles['reset']} (Press Enter To Continue)")
    print(f"{styles['bold']}A Turn:{styles['reset']}")
    print("Every turn you must do 1 of 4 things:\n")
    print("1. Add a card to your pallete\n2. Add a card to the canvas\n3. Add a card to your pallete and then a card to the canvas\n4. Do nothing (This means you lose)\n")
    print("If you are not winning at the end of your turn, you are out and have lost.")
    input()
    clear()
    
if __name__ == "__main__":
    tutorial()