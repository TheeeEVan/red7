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

def tutorial():
	clear()
	print(f"{styles['bold']}Tutorial{styles['reset']}")
	print(f"{styles['bold']}The Cards:{styles['reset']}")
	print("There are 49 cards")
	print("Every card is assigned a number from 1-7")
	print("Every card is assigned a number (red, orange, yellow, green, blue, indigo, violet)")
	input()

if __name__ == "__main__":
	tutorial()