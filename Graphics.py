'''
Graphics.py - Handles all visual elements of the game
'''

import os, sys

# constants
# hidden color is for hidden cards and applys no style
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "hidden"]
styles = ["\033[38;2;255;0;0m", "\033[38;2;255;128;0m", "\033[38;2;255;255;0m", "\033[38;2;0;255;0m", "\033[38;2;23;103;189m", "\033[38;2;68;0;255m", "\033[38;2;255;0;255m", ""]
reset = "\033[0m"

# returns an array with the individual lines of the card so we can render them side to side easily
render_card = lambda color, number : [f"{styles[colors.index(color)]}┌─────┐{reset}", f"{styles[colors.index(color)]}│     │{reset}", f"{styles[colors.index(color)]}│  {number}  │{reset}", f"{styles[colors.index(color)]}│     │{reset}", f"{styles[colors.index(color)]}└─────┘{reset}",]

# draws a empty space for card
empty_card = ["       ", "       ", "       ", "       ", "       "]

class Board:
    '''
    Represents the visual playing area of the game
    '''
    def __init__(self, hands, palletes, draw_pile, canvas):
        self.player_hand, self.com1_hand, self.com2_hand, self.com3_hand = hands
        self.player_pallete, self.com1_pallete, self.com2_pallete, self.com3_pallete = palletes
        self.draw_pile = draw_pile
        self.canvas = canvas
        # this stores the current board output for easier reprinting
        self.cache = ""
    def draw(self):
        # start by clearing screen
        clear()
        self.cache = ""
        # in order to draw the cards correctly we need to determine what every line in the console should look like
        # as we determine this they will get stored in lines
        lines = []
        
        # in order to keep cards centered we need to have a priority for where cards will be placed
        # this is the order
        # 6 4 2 1 3 5 7

        # to acheive this we'll fill an array with all the cards in order, filling the rest with placeholder empty card
        # we'll then swap them to follow this desired order using our swap() function
        
        # use copy to avoid changing the actual hand
        temp_pile = self.com2_hand.cards.copy()

        # i will keep track of how many placeholders we need
        i = len(temp_pile)

        # continue adding place holders until there are 7 cards
        while i < 7:
            # None will represent our placeholder
            temp_pile.append(None)
            i += 1
        
        # use the swap function to move cards
        swap(temp_pile)

        # also add padding for the vertical cards
        temp_pile[:0] = [None, None]
        temp_pile.extend([None, None])

        # go through every card in our temp hand
        for card in temp_pile:
            # if placeholder than set to an empty card
            # otherwise draw as hidden card
            if card == None:
                lines.append(empty_card)
            # check if we should draw red x
            elif not card.inplay:
                lines.append(render_card("red", "X"))
            else:
                lines.append(render_card("hidden", "?"))

        self._print_row(lines)
        # reset lines
        lines = []

        # same as above but for the pallete (meaning we dont draw the cards as hidden)
        # set temp_pile to a copy of the computers pallete
        temp_pile = self.com2_pallete.cards.copy()

        # used to determine how many placeholders to add
        i = len(temp_pile)

        # if theres less than 7 cards we fill the remaining spots with placeholders
        while i <  7:
            temp_pile.append(None)
            i += 1

        # swap all the cards to follow priority
        swap(temp_pile)

        # add padding to make room for other decks
        temp_pile[:0] = [None, None]
        temp_pile.extend([None, None])

        # go through all cards
        for card in temp_pile:
            # if placeholder add empty line to output
            if card == None:
                lines.append(empty_card)
            # otherwise add the correct card using its color and number
            else:
                lines.append(render_card(card.color, card.number))

        # print the generated line
        self._print_row(lines)
        # reset for next line
        lines = []

        # now that the first two piles are done, we have to render the four vertically positioned piles
        # as well as the draw pile and canvas

        # this will need four temporary decks so we'll turn temp_pile into an array of temporary piles
        # 0 - com1_hand | 1 - com1_pallete | 2 - com3_pallete | 3 - com3_hand
        temp_pile = [[], [], [], []]

        # start by copying all the respective piles
        temp_pile[0] = self.com1_hand.cards.copy()
        temp_pile[1] = self.com1_pallete.cards.copy()
        temp_pile[2] = self.com3_pallete.cards.copy()
        temp_pile[3] = self.com3_hand.cards.copy()

        # now fill all the piles with placeholders and swap
        # we'll do this on all 4 piles
        for j in range(4):
            # used to determine how many placeholders we need
            i = len(temp_pile[j])

            # continue adding placeholders until there is enough cards
            while i < 7:
                temp_pile[j].append(None)
                i += 1

            # once placeholders are added we can swap the deck
            swap(temp_pile[j])

        # now all piles are ready to render

        # we have 7 rows of cards to render
        for i in range(7):
            # first add the ith card of the first deck
            # if placeholder add empty
            if temp_pile[0][i] == None:
                lines.append(empty_card)
            # check if we should draw red x
            elif not temp_pile[0][i].inplay:
                lines.append(render_card("red", "X"))
            # otherwise add a hidden card since its a computers deck
            else:
                lines.append(render_card("hidden", "?"))

            # next add the ith card of the second deck
            # if placeholder add empty
            if temp_pile[1][i] == None:
                lines.append(empty_card)
            # otherwise add the correct card using it's color and number since it is a visable card
            else:
                lines.append(render_card(temp_pile[1][i].color, temp_pile[1][i].number))

            # now that the first two decks are done, we have to check if this is the row that has the draw pile since it's in the middle
            if not i == 3:
                # if it's not the drawpile just add some placeholder cards to get to the other side
                for j in range(7):
                    lines.append(empty_card)
            else:
                # since this is the draw pile case we have to render the draw pile and canvas in the center
                # it's very similar to the empty case except two of the spots are populated by cards
                
                # start by adding two empty cards
                lines.append(empty_card)
                lines.append(empty_card)

                # now we draw the draw pile
                
                # check to make sure the draw pile isn't empty
                # if there's a card we'll add a hidden card
                if len(self.draw_pile.cards):
                    lines.append(render_card("hidden", "?"))
                # otherwise add an empty card to show that it's empty
                else:
                    lines.append(empty_card)

                # add another empty card to seperate the two decks
                lines.append(empty_card)

                # now draw the card on top of the canvas (there will always be a card on the canvas so no need to check if its empty)
                lines.append(render_card(self.canvas.cards[0].color, self.canvas.cards[0].number))

                # finally draw two more placeholders to get to the next deck
                lines.append(empty_card)
                lines.append(empty_card)

            # now add the other computers pallete
            # if plceholder add empty
            if temp_pile[2][i] == None:
                lines.append(empty_card)
            # otherwise add the correct card with color and number beause it's in pallete
            else:
                lines.append(render_card(temp_pile[2][i].color, temp_pile[2][i].number))

            # lastly the other computers deck
            # if placeholder add empty
            if temp_pile[3][i] == None:
                lines.append(empty_card)
            # check if we should draw red x
            elif not temp_pile[3][i].inplay:
                lines.append(render_card("red", "X"))
            # otherwise add a hidden card because its a hidden deck
            else:
                lines.append(render_card("hidden", "?"))

            # now that the row has been generated we can print it
            self._print_row(lines)

            # reset lines for next row
            lines = []

        # now the vertical decks are done
        # now just print the user deck and pallete using the same method as before excpet all cards are displayed

        # start with player pallete creating a copy of it
        temp_pile = self.player_pallete.cards.copy()

        # used to find how many placeholders we need
        i = len(temp_pile)

        # continue adding placeholders until deck is full
        while i < 7:
            temp_pile.append(None)
            i += 1

        # swap cards to follow priority
        swap(temp_pile)

        # add padding for the vertical decks
        temp_pile[:0] = [None, None]
        temp_pile.extend([None, None])

        # loop through every card
        for card in temp_pile:
            # if placeholder add empty card
            if card == None:
                lines.append(empty_card)
            # otherwise add the correct card with color and number
            else:
                lines.append(render_card(card.color, card.number))

        # finally print the row
        self._print_row(lines)

        # reset lines for next row
        lines = []

        # finally print player hand
        
        # start with player hand creating a copy of it
        temp_pile = self.player_hand.cards.copy()

        # used to find how many placeholders we need
        i = len(temp_pile)

        # continue adding placeholders until deck is full
        while i < 7:
            temp_pile.append(None)
            i += 1

        # i decieded not to swap player hand to ensure cards dont go all over the place when you choose them

        # add padding for the vertical decks
        temp_pile[:0] = [None, None]
        temp_pile.extend([None, None])

        # loop through every card
        for card in temp_pile:
            # if placeholder add empty card
            if card == None:
                lines.append(empty_card)
            elif not card.inplay:
                lines.append(render_card("red", "X"))
            # otherwise add the correct card with color and number
            else:
                lines.append(render_card(card.color, card.number))
        
        # print the row
        self._print_row(lines)

        # finally print indexes for users cards and add to cache 
        print("                 1      2      3      4      5      6      7")
        self.cache += "                 1      2      3      4      5      6      7\n"

    def _print_row(self, lines):
        for i in range(5):
                line = ''
                for j in range(len(lines)):
                    line += lines[j][i]

                # add the line to the cache for easier printing later
                self.cache += line + "\n"
                # use stdout to ensure faster speed to stop scanning effect because of how many lines we are printing
                sys.stdout.write(line + "\n")

    def reprint(self):
        clear()
        # print cache
        sys.stdout.write(self.cache)

        
def swap(cards):
    # swaps cards according to the followng
    # 6 4 2 1 3 5 7
    cards[0], cards[1], cards[2], cards[3], cards[4], cards[5] = cards[5], cards[3], cards[1], cards[0], cards[2], cards[4]

def clear():
    # checks for os and sends appropriate clear command
    if os.name == 'posix':
        os.system("clear")
    else:
        os.system("cls")