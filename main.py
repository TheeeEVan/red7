'''
red7
'''
# import files
from Pile import Pile, DrawPile
from Card import Card, PlayingRed
from Graphics import Board, clear
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

# list of colors from most value to least
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# empty placeholder Pile
empty_pile = Pile()


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

def check_winner(game_palletes, canvas):
    # checks who is winning the game
    # NOTE: I didn't think that python has a data strucutre called set...
    # in this function a set refers to a list of cards which follow a condition (the current rule)
    
    # functions for all the rules
    def highest_card():
        # creates a list of each players highest card, if pallete is empty sets to None
        highest_cards = [max(i.cards) if i.cards else None for i in palletes]
        # returns the player with the highest card, or None if no one has cards
        return highest_cards.index(max([i for i in highest_cards if i != None])) if highest_cards != [None, None, None, None] else None

    def one_number():
        # this will store the cards that make up the mode of each deck
        sets = []
        
        # calculate the mode of every pallete
        for pallete in palletes:
            values = [[], [], [], [], [], [], []]
    
            # sort cards into their values
            for card in pallete.cards:
                values[card.number - 1].append(card)
            
            # find the list with most cards
            # max stores amount of cards
            # index stores where the list is/number on the cards - 1
            max_mode = 0
            index = None
            # go through every card value
            for value in values:
                # if there's more or the same cards as before, set max_mode to the amount of cards and set index to the value - 1
                # we use >= to adjust for same amounts of cards worth more
                if len(value) >= max_mode:
                    max_mode = len(value)
                    index = values.index(value)
            # add the highest value if there is one otherwise add empty list
            sets.append(values[index]) if max_mode != 0 else sets.append([])

        # get the lengths of each set
        lengths = [len(set) for set in sets]

        # if no one has cards then None, stops first move from just changing canvas
        if max(lengths) == 0:
            return None
        # if theres only one person with the most then return them
        elif lengths.count(max(lengths)) == 1:
            return lengths.index(max(lengths))
        # this means more than one person has the same mode
        else:
            # this case we need to find the highest card of all the highest modes
            ties = [(set, sets.index(set)) for set in sets if len(set) == max(lengths)]
            # stores the highest card found as well as the index of that player
            index = None
            max_card = None
            # go through all players which have tied
            for i in range(len(ties)):
                # if the highest card in their set is higher than the highest card found make that card the highest
                if max(ties[i][0]) > max_card:
                    max_card = max(ties[i][0])
                    index = ties[i][1]
            
            return index

    def one_color():
        # stores sets of one color cards
        sets = []

        for pallete in palletes:
            # list starts as 7 empty lists, each representing a color
            # cards will be sorted into their colors, and the 
            set = [[], [], [], [], [], [], []]
            
    def most_even():
        # stores sets of even cards
        sets = []

        for pallete in palletes:
            set = []

            # go through every card
            for card in pallete.cards:
                if int(card.number) % 2 == 0:
                    set.append(card)

            sets.append(set)

        # first find the lengths of each set
        lengths = [len(set) for set in sets]
    
        # first find the max length
        highest = max(lengths)

        # first check if no one has cards under 4
        if highest == 0:
            return None
        # next if theres only one person with the highest than they won
        elif lengths.count(highest) == 1:
            return lengths.index(highest)
        # this means more than one person has the same amount of cards
        else:
            # find all our ties
            ties = [(set, sets.index(set)) for set in sets if len(set) == highest]

            # find the highest card in ties
            index = None
            max_card = None
            for tie in ties:
                if max(tie[0]) > max_card:
                    max_card = max(tie[0])
                    index = tie[1]

            return index

    def differnt_colors():
        # stores every set
        sets = []

        for pallete in palletes:
            # initiate the set as a list of 7 Nones, each one representing a different color
            # as we find cards with different colors we will replace them with cards
            set = [None, None, None, None, None, None, None]

            for card in pallete.cards:
                # get the index of the cards color
                color_index = colors.index(card.color)

                # check if current card is > than the card used for that color
                if card > set[color_index]:
                    set[color_index] = card
            # add the set, removing all Nones
            sets.append([i for i in set if i != None])

        # get lengths of every set
        lengths = [len(set) for set in sets]

        # find the set with the most cards
        highest = max(lengths)

        # check if players have no cards
        if highest == 0:
            return None
        # check if only one person has the most cards
        elif lengths.count(highest) == 1:
            # reutrn that players
            return lengths.index(highest)
        # otherwise there is a tie
        else:
            # get all ties
            ties = [(set, sets.index(set)) for set in sets if len(set) == highest]

            # find highest card in ties
            index = None
            max_card = None
            for tie in ties:
                if max(tie[0]) > max_card:
                    max_card = max(tie[0])
                    index = tie[1]
                    
            return index
    def under_four():
        # this will store each players cards which are under 4
        sets = []

        for pallete in palletes:
            # this will contain the cards under 4 for each player
            set = []

            # go through every card
            for card in pallete.cards:
                # if the number is < 4 than add it to the players set
                if int(card.number) < 4:
                    set.append(card)
            # now add the players set to the list of sets
            sets.append(set)

        # first find the lengths of each set
        lengths = [len(set) for set in sets]
    
        # first find the max length
        highest = max(lengths)

        # first check if no one has cards under 4
        if highest == 0:
            return None
        # next if theres only one person with the highest than they won
        elif lengths.count(highest) == 1:
            return lengths.index(highest)
        # this means more than one person has the same amount of cards
        else:
            # find all our ties
            ties = [(set, sets.index(set)) for set in sets if len(set) == highest]

            # find the highest card in ties
            index = None
            max_card = None
            for tie in ties:
                if max(tie[0]) > max_card:
                    max_card = max(tie[0])
                    index = tie[1]

            return index
            
    # new palletes list so we can easily remove the palletes out of play without deleting them from board
    palletes = []

    for pallete in game_palletes:
        # check if the pallete is in play
        palletes.append(pallete) if pallete.inplay else palletes.append(empty_pile)
    
    if canvas.cards[0].color == "red":
        return highest_card()
    elif canvas.cards[0].color == "orange":
        return one_number()
    #elif canvas.cards[0].color == "yellow":
        #return one_color()
    elif canvas.cards[0].color == "blue":
        return differnt_colors()
    elif canvas.cards[0].color == "green":
        return most_even()
    elif canvas.cards[0].color == "violet":
        return under_four()
    else:
        return None
def user_turn(hand, palletes, canvas):
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
    while True:
        action = get_action(invalid)
        # user wants to add card to pallete
        if action == 1:
            # pallete will return False if user goes back or makes invalid move so we can restart the loop
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