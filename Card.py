'''
Card.py - Contains the card class for the red 7 game
'''

# constants
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

class Card:
    '''
    A class used to represent a red 7 Card
    ===============
    
    Attributes
    -----------
    color : str
        the color of the card 
    number : int
        the number value of the card
    '''
    # store given color and number in self
    def __init__(self, color, number):
        # validate color and number allowing for easier debugging 
        if not color in colors:
            raise ValueError("Invalid color")
        if number < 1 or number > 7:
            raise ValueError("Invalid number")
        
        self.color = color
        self.number = number
        self.inplay = True

    # COMPARATIVE LOGIC: (if Card1 > Card2 then Card1 has higher value than Card 2)
    
    # the logic when using > on the class
    def __gt__(self, other):
        # check for none
        if other is None:
            return True
        # if theres a bigger number it will always be worth more
        elif self.number > other.number:
            return True
        # in the case that numbers are equal than we need to compare colors
        elif self.number == other.number:
            # using our list of colors we can use the indexs to determine if a card is worth more
            if colors.index(self.color) < colors.index(other.color):
                return True
            else:
                return False
        else:
            return False

    # the logic when using < on the class
    def __lt__(self, other):
        if other is None:
            return False
        # if theres a smaller number it will always be worth less
        elif self.number > other.number:
            return False
        # in the case that numbers are equal than we need to compare colors
        elif self.number == other.number:
            # using our list of colors we can use the indexs to determine if a card is worth less
            if colors.index(self.color) < colors.index(other.color):
                return False
            else:
                return True
        else:
            return True

# represents the playing red card used to start the canvas
# it has to extend card so it's a valid card to be added to a Pile
class PlayingRed(Card):
    def __init__(self):
        self.color = "red"
        self.number = " "

    # we shouldn't use comparitve operators on this card
    def __gt__(self):
        raise TypeError
    def __lt__(self):
        raise TypeError