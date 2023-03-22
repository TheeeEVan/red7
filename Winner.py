from Pile import Pile

# list of colors from most value to least
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# empty placeholder Pile
empty_pile = Pile()

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

            for card in pallete.cards:
                set[colors.index(card.color)].append(card)

            lengths = [len(color) for color in set]
            max_cards = max(lengths)

            if max_cards == 0:
                sets.append([])
            elif lengths.count(max_cards) == 1:
                sets.append(set[lengths.index(max_cards)])
            else:
                ties = [color for color in set if len(color) == max_cards]
                higher_card = [max(tie) for tie in ties]
                sets.append(ties[higher_card.index(max(higher_card))])
        
        lengths = [len(set) for set in sets]

        if max(lengths) == 0:
            return None
        elif lengths.count(max(lengths)) == 1:
            return lengths.index(max(lengths))
        else:
            ties = [(set, sets.index(set)) for set in sets if len(set) == max(lengths)]

            index = None
            max_card = None

            for tie in ties:
                if max(tie[0]) > max_card:
                    max_card = max(tie[0])
                    index = tie[1]

            return index
        
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
        
    def form_run():
        return None

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
    elif canvas.cards[0].color == "yellow":
        return one_color()
    elif canvas.cards[0].color == "green":
        return most_even()
    elif canvas.cards[0].color == "blue":
        return differnt_colors()
    elif canvas.cards[0].color == "indigo":
        return form_run()
    elif canvas.cards[0].color == "violet":
        return under_four()
    else:
        return None