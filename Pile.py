'''
Pile.py - Contains the Pile class

Pile is used to represent a collection of cards, such as a hand or discard pile
''' 
from Card import Card
from random import randint

# constants
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

class Pile:
    '''
    A class used to represent a collection of cards
    ===============

    Attributes
    -----------
    None

    Methods
    -----------
    add_card(new_card, index)
        Adds a card to the Pile

    remove_card(index = 0)
        Removes a card from the pile, returning the removed card

    shuffle()
        Shuffles the pile
    
    '''
    # create an empty pile
    def __init__(self):
        self.cards = []
        # used on palletes when determining if they should be considered as winner
        self.inplay = True

    # use None as default value becuase self isn't accesible
    def add_card(self, new_card, index = None):
        '''
        Adds a card to the Pile

        Paramaters:
            new_card : Card - The Card to add to the pile
            index : int - The index which to place the Card (defaults to end of the list)
        '''
        
        # if index is None then switch to default value of the end of the list
        if index == None:
            index = len(self.cards)
        # first check if the new_card is a Card object to make debugging easier
        if isinstance(new_card, Card):
            # add to the pile
            self.cards.insert(index, new_card)
        
        # the passed object isn't a Card so throw a TypeError
        else:
            raise TypeError("Non-Card object added to the pile")

    def remove_card(self, index = 0):
        '''
        Removes a card from the pile. Returns Card

        Paramaters:
            index : int - the index which to remove the card from (defaults to 0)
        '''
        # return the removed card
        return self.cards.pop(index)

    def shuffle(self):
        '''
        Shuffles the deck
        '''
        # go through every card
        for i in range(len(self.cards)):
            # get a random card to swap it with
            j = randint(i, len(self.cards) - 1)
            
            # swap the cards
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

class DrawPile(Pile):
    '''
    A Pile object that is initialized with all cards for red7
    '''
    def __init__(self):
        self.cards = []
        for color in colors:
            for number in range(1, 8):
                self.cards.append(Card(color, number))