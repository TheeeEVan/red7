# import modules
from Pile import Pile, DrawPile
from Card import PlayingRed
from Graphics import Board, clear
from Winner import check_winner
from Rules import tutorial
import time

# constants

title = '''
                                                 ,----, 
                                               .'   .`| 
\033[38;2;255;0;0m,-.----.\033[0m                                    .'   .'   ; 
\033[38;2;255;0;0m\    /  \                  ,---,\033[0m          ,---, '    .' 
\033[38;2;255;0;0m;   :    \               ,---.'| \033[0m         |   :     ./  
\033[38;2;255;0;0m|   | .\ :               |   | : \033[0m         ;   | .'  /   
\033[38;2;255;0;0m.   : |: |    ,---.      |   | | \033[0m         `---' /  ;    
\033[38;2;255;0;0m|   |  \ :   /     \   ,--.__| | \033[0m           /  ;  /     
\033[38;2;255;0;0m|   : .  /  /    /  | /   ,'   | \033[0m          ;  /  /      
\033[38;2;255;0;0m;   | |  \ .    ' / |.   '  /  | \033[0m         /  /  /       
\033[38;2;255;0;0m|   | ;\  \'    ;   /|'   ; |:  | \033[0m       ./__;  /        
\033[38;2;255;0;0m:   ' | \.''   |  / ||   | '/  ' \033[0m       |   : /         
\033[38;2;255;0;0m:   : :-'  |   :    ||   :    :| \033[0m       ;   |/          
\033[38;2;255;0;0m|   |.'     \   \  /  \   \  /   \033[0m       `---'           
\033[38;2;255;0;0m`---'        `----'    `----'    \033[0m                       
                                                        '''

# contains strings for the rules
rules = {
    "red": "Highest Card",
    "orange": "Cards of One Number",
    "yellow": "Cards of One Color",
    "green": "Even Cards",
    "blue": "Cards of All Different Colors",
    "indigo": "Cards That Form a Run",
    "violet": "Cards Below 4"
}

# contains ansi style escapes for coloring and styling text
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


def check_size():
    '''
    Allows user to resize console to ensure the entire game will fit
    '''
    # prints 77 character line to allow user to resize console so the game will fit without wrapping
    clear()
    print("Before starting please resize your console so you only see one horizontal line\n(press enter to continue)")
    print("─"*77)
    # enter to continue
    input()
    # clear screen
    clear()
    
def welcome():
    '''
    Welcomes user to the game
    '''
    print("Welcome to...")
    time.sleep(1.5)
    clear()
    print(title)
    print("\n\n\033[1mEnsure you read the readme to learn how to play the game before starting!\033[0m")
    print("(Press enter to start the game)")
    input()

def leave():
    '''Ends the game before someone wins'''
    clear()
    quit()

def user_turn(hand, palletes, canvas):
    '''
    Runs a users turn
    '''
    def get_action(invalid):
        '''
        returns users selected action as int
        '''
        # draw board and inital options
        board.draw()
        print(f"{styles['bold']}It's your turn! Current Rule:{styles['reset']} {styles[canvas.cards[0].color]}{rules[canvas.cards[0].color]}{styles['reset']}\n")
        print("(1) Move a card to pallete              (5) Show Rules\n(2) Move a card to canvas               (6) Shuffle your hand\n(3) Move a card to pallete and canvas   (7) Quit\n(4) End turn and Lose")
        if invalid:
            print(f"{styles['red'] + styles['bold']}Invalid Move!{styles['reset']} After that move you would be losing...")
        # continue looping until user gives valid option
        while True:
            # get user input
            action = input("? ")

            # check for valid input
            if action.isnumeric():
                if int(action) > 0 and int(action) < 8:
                    # return int of input
                    return int(action)
            # since function didn't return input is invalid
            # reprint board and instructions adding invalid message
            board.reprint()
            print(f"{styles['bold']}It's your turn! Current Rule:{styles['reset']} {styles[canvas.cards[0].color]}{rules[canvas.cards[0].color]}{styles['reset']}\n")
            print("(1) Move a card to pallete              (5) Show Rules\n(2) Move a card to canvas               (6) Shuffle your hand\n(3) Move a card to pallete and canvas   (7) Quit\n(4) End turn and Lose")
            print(f"{styles['red'] + styles['bold']}Invalid Input!{styles['reset']}")

    def get_card(message):
        '''
        Allows user to choose a card from their deck, returning the int of it's index in Pile.cards
        '''
        # print context and valid options
        print(message)
        print("(Enter the number below the desired card, or 0 to go back)")

        # continue looping until valid choice
        while True:
            # get users choice
            choice = input("? ")

            if choice.isnumeric():
                # check for 0
                if int(choice) == 0:
                    # -1 signals go back
                    return -1
                # check if the converted choice is within range of the hand
                elif int(choice) > 0 and int(choice) < 8:
                    if convert_index(int(choice) - 1) >= 0 and convert_index(int(choice) - 1) < len(hand.cards) + 1:
                        # return index of the card
                        return convert_index(int(choice) - 1)
            # since no return input must be invalid
            # reprint board and add invald input message
            board.reprint()
            print(f"{styles['bold']}It's your turn! Current Rule:{styles['reset']} {styles[canvas.cards[0].color]}{rules[canvas.cards[0].color]}{styles['reset']}\n")
            print(message)
            print("(Enter the number below the desired card, or 0 to go back)")
            print(f"{styles['red'] + styles['bold']}Invalid Input!{styles['reset']}")
    
    def convert_index(index):
        '''
        Converts selected index on board to index in hand because of card swapping when drawing board
        '''
        # this is manual cause theres no way to calculate
        return index
            
    # move card to pallete
    def add_pallete():
        '''
        Allows a user to choose a card from their deck to add to their pallete
        '''
        # reprint board
        board.reprint()
        # print turn message again to allow user to see current rule
        print(f"{styles['bold']}It's your turn! Current Rule:{styles['reset']} {styles[canvas.cards[0].color]}{rules[canvas.cards[0].color]}{styles['reset']}\n")

        # get users card
        choice = get_card("Which card would you like to add to your pallete?")

        # check for go back
        if choice == -1:
            # false signals to go back
            return False

        # remove the selected card from hand and add it to pallete
        palletes[0].add_card(hand.remove_card(choice))

        # ensure user is winning after move
        if check_winner(palletes, canvas) == 0:
            return True
        else:
            # otherwise undo added card
            hand.add_card(palletes[0].remove_card(len(palletes[0].cards) - 1), choice)
            # returning falase signals to add invalid move message
            return False

    def add_canvas():
        '''
        Lets the user choose a card from their deck to add to the canvas
        '''
        # reprint board
        board.reprint()
        # print turn message again to allow user to see current rule
        print(f"{styles['bold']}It's your turn! Current Rule:{styles['reset']} {styles[canvas.cards[0].color]}{rules[canvas.cards[0].color]}{styles['reset']}\n")
    
        # get users card
        choice = get_card("Which card would you like to add to the canvas?")
        
        # check for go back
        if choice == -1:
            return False

        # add card to start of canvas
        canvas.add_card(hand.remove_card(choice), 0)

        # check if player is winning
        if check_winner(palletes, canvas) == 0:
            return True
        else:
            hand.add_card(canvas.remove_card(), choice)
            return False
    # start by getting the users action
    def add_both():
        '''
        Let's the user choose two cards from their deck, one for the pallete, one for the canvas
        '''
        if len(hand.cards) > 1:
            # reprint board
            board.reprint()
            # print turn message again to allow user to see current rule
            print(f"{styles['bold']}It's your turn! Current Rule:{styles['reset']} {styles[canvas.cards[0].color]}{rules[canvas.cards[0].color]}{styles['reset']}\n")
    
            # get users card
            choice1 = get_card("Which card would you like to add to your pallete?")
            
            # check for go back
            if choice1 == -1:
                # false signals to go back
                return False
    
            # remove the selected card from hand and add it to pallete
            palletes[0].add_card(hand.remove_card(choice1))
    
            # reprint board
            board.draw()
            # print turn message again to allow user to see current rule
            print(f"{styles['bold']}It's your turn! Current Rule:{styles['reset']} {styles[canvas.cards[0].color]}{rules[canvas.cards[0].color]}{styles['reset']}\n")
        
            # get users card
            choice2 = get_card("Which card would you like to add to the canvas?")
            
            # check for go back
            if choice2 == -1:
                hand.add_card(palletes[0].remove_card(len(palletes[0].cards) - 1), choice1)
                return False
    
            # add card to start of canvas
            canvas.add_card(hand.remove_card(choice2), 0)
    
            # check if user is winning
            if check_winner(palletes, canvas) == 0:
                return True
            else:
                # if user isn't winning, add the cards back to the hand
                hand.add_card(canvas.remove_card(), choice2)
                # finds the last card in the pallete and puts it back in the deck
                hand.add_card(palletes[0].remove_card(len(palletes[0].cards) - 1), choice1)
                # user didn't make valid move so return False
                return False

    def print_rules():
        # reprint board
        board.reprint()
        # 
        print(f"{styles['bold']}All Rules:{styles['reset']} (press enter to continue)")
        for key in rules.keys():
            print(styles[key] + rules[key] + styles['reset'])
        input()

    # the requirements are to have to be able to shuffle the deck but I decided not to use the deck
    # this just uses the shuffle function on the users hand to show that it would be possible since its the same class as the deck
    def shuffle_hand():
        hand.shuffle()
        board.draw()


    invalid = False
    # ask user for their action until valid move
    while True:
        action = get_action(invalid)
        # go through all possible actions, running the correct function for each
        # functions return True if valid move
        # 1 - Add to pallete
        # 2 - Add to canvas
        # 3 - Add to both
        # 4 - End Turn
        # 5 - Print Rules
        # 6 - Shuffle Deck
        # 7 - Quit Game
        if action == 1:
            if add_pallete():
                return True
            else:
                invalid = True
        elif action == 2:
            if add_canvas():
                return True
            else:
                invalid = True
        elif action == 3:
            if add_both():
                return True
            else:
                invalid = True
        elif action == 4:
            # returning false signals that player lost
            return False
        elif action == 5:
            print_rules()
        elif action == 6:
            shuffle_hand()
        elif action == 7:
            leave()
def com_turn(hand, palletes, canvas, index):
    # computers algorithm
    # 1. check for valid card to pallete
    # 2. check for valid card to canvas
    # 3. check for valid both

    # start by going through every card and seeing if its a valid move to put in pallete
    for i in range(len(hand.cards)):
        palletes[index].add_card(hand.remove_card(i))

        if check_winner(palletes, canvas) == index:
            return True
        else:
            hand.add_card(palletes[index].remove_card(len(palletes[index].cards) - 1), i)

    # same but to the canvas
    for i in range(len(hand.cards)):
        canvas.add_card(hand.remove_card(i), 0)

        if check_winner(palletes, canvas) == index:
            return True
        else:
            hand.add_card(canvas.remove_card())

    # check if theres enough cards to move 2 cards
    if len(hand.cards) > 1:
        # now we check every card getting added to pallete again
        for i in range(len(hand.cards)):
            palletes[index].add_card(hand.remove_card(i))
    
            # but now we also check every card going to canvas as well
            for j in range(len(hand.cards)):
                canvas.add_card(hand.remove_card(j), 0)
    
                # now check for winner
                if check_winner(palletes, canvas) == index:
                    return True
                else:
                    hand.add_card(canvas.remove_card())
            # since we finished the for loop no move was found so undo the pallete
            hand.add_card(palletes[index].remove_card(len(palletes[index].cards) - 1), i)
    
    # no moves found
    return False
    
def round():
    # make the board class global so we don't have to pass it to every function
    global board
    # intialize all piles
    draw_pile = DrawPile()
    canvas = Pile()
    # adds the playing red card to canvas to set first rule
    canvas.add_card(PlayingRed())

    
    # we'll make 4 piles in an array for hands, 0 is player, all others are respective computers
    hands = [Pile(), Pile(), Pile(), Pile()]

    # same thing for palletes
    palletes = [Pile(), Pile(), Pile(), Pile()]

    # create the board for renderer
    board = Board(hands, palletes, draw_pile, canvas)
    
    # start by shuffling the draw pile
    draw_pile.shuffle()
    
    # deal 7 cards to each player, simulating real deal by alternating players every card
    for i in range(7):
        for j in range(4):
            hands[j].add_card(draw_pile.remove_card())
    
    # this keeps track of which players are still in the game
    playing = [True, True, True, True]

    # continue playing until game is over
    while True:
        # check if more than one person is still in the game
        if playing.count(True) > 1:   
            # user's turn:
            # check if user is still in
            if playing[0] and playing.count(True) > 1:
                # run users turn
                # user_turn will return True or False depending on if the user is winning or not
                playing[0] = user_turn(hands[0], palletes, canvas)
                # if user is out, set their pallete state to not be in play, as well as their cards
                if not playing[0]:
                    palletes[0].inplay = False
                    for card in hands[0].cards:
                                    card.inplay = False
            # loop through computers, (same as player except use i to reference the current computer) (player 2, 3 and 4)
            for i in range(1, 4):
                board.draw()
                print("Computers are playing...")
                if playing[i] and playing.count(True) > 1:
                    # waiting helps to make it easier to see what is happening
                    time.sleep(1)
                    playing[i] = com_turn(hands[i], palletes, canvas, i)
                    if not playing[i]:
                        palletes[i].inplay = False

                        for card in hands[i].cards:
                            card.inplay = False
        else:
            board.draw()
            print(f"{styles['bold']}Player {playing.index(True) + 1} wins!{styles['reset']}")
            # destroy the board cause its global and memory is bad
            del board
            if playing.index(True) == 0:
                return True
            return False

if __name__ == "__main__":
    '''main game loop'''
    # check size of users terminal
    check_size()
    # welcome the user
    welcome()

    # main loop condition
    playing = True
    # tracks players total wins
    wins = 0

    while playing:
        clear()
        print(title)
        print(f"You have won {styles['bold']}{wins}{styles['reset']} games this session\n")

        invalid = True
        action = ""

        while invalid:
            print("What would you like to do?")
            print("(1) Start a game\n(2) Learn how to play\n(3) Quit")
            action = input("")

            if action.isnumeric():
                action = int(action)
                if action > 0 and action < 4:
                    invalid = False
                else:
                    clear()
                    print(title)
                    print(f"You have won {styles['bold']}{wins}{styles['reset']} games this session\n")
                    print(f"{styles['bold']}{styles['red']}Invalid input...{styles['reset']}\n")
            else:
                clear()
                print(title)
                print(f"You have won {styles['bold']}{wins}{styles['reset']} games this session\n")
                print(f"{styles['bold']}{styles['red']}Invalid input...{styles['reset']}\n")
        
        if action == 1:
            invalid = False
            # round will return true if user wins so we can just put it in if statement
            if round():
                wins += 1
            time.sleep(4)
        elif action == 2:
            invalid = False
            tutorial()
        elif action == 3:
            leave()
