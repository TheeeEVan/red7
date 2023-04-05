# import modules
from Pile import Pile, DrawPile
from Card import PlayingRed
from Graphics import Board, clear
from Winner import check_winner
import time

# constants
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
    print("Before starting please resize your console so you only see one line\n(press enter to continue)")
    print("─"*77)
    # enter to continue
    input()
    # clear screen
    clear()
    
def welcome():
    '''
    Welcomes user to the game
    '''
    # TODO: Make this better!!!
    print("Welcome to...")
    time.sleep(2)
    clear()
    print('''
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
                                                        ''')
    print("\n\n\033[1mEnsure you read the readme to learn how to play the game before starting!\033[0m")
    print("(Press enter to start the game)")
    input()

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
        print("(1) Move a card to pallete\n(2) Move a card to canvas\n(3) Move a card to pallete and canvas\n(4) End turn and Lose")
        if invalid:
            print(f"{styles['red'] + styles['bold']}Invalid Move!{styles['reset']} After that move you would be losing...")
        # continue looping until user gives valid option
        while True:
            # get user input
            action = input("? ")

            # check for valid input
            if action.isnumeric():
                if int(action) > 0 and int(action) < 5:
                    # return int of input
                    return int(action)
            # since function didn't return input is invalid
            # reprint board and instructions adding invalid message
            board.reprint()
            print(f"{styles['bold']}It's your turn! Current Rule:{styles['reset']} {styles[canvas.cards[0].color]}{rules[canvas.cards[0].color]}{styles['reset']}\n")
            print("(1) Move a card to pallete\n(2) Move a card to canvas\n(3) Move a card to pallete and canvas\n(4) End turn")
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

        # TODO: check for winner when all rules implemented
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
    
            if check_winner(palletes, canvas) == 0:
                return True
            else:
                hand.add_card(palletes[0].remove_card(len(palletes[0].cards) - 1), choice1)
                hand.add_card(canvas.remove_card(), choice2)
                return False
            
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
            return False
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
    
    playing = [True, True, True, True]
    while True:

        if playing.count(True) > 1:   
            if playing[0] and playing.count(True) > 1:
                playing[0] = user_turn(hands[0], palletes, canvas)
                if not playing[0]:
                    palletes[0].inplay = False
            for i in range(1, 4):
                if playing[i] and playing.count(True) > 1:
                    playing[i] = com_turn(hands[i], palletes, canvas, i)
                    if not playing[i]:
                        palletes[i].inplay = False
            board.draw()
        else:
            print(f"Player {playing.index(True) + 1} wins!")
            break
round()