# Need to initialise player and pull three cards from the deck. 
# Etc.

class Hand: 
    """
    A hand of playing cards: 
    At the beginning of the game, each player is dealt three cards. 
    At the end of his/her turn, the player draws one card. If the player's hand already contains five cards, the player is not allowed to draw another card.
    The player may abstain from drawing a card, unless the player before him/her abstained from drawing a card.
    If the player immediately before has abstained from drawing a card and the player's had contains five cards, the player must play or discard at least one card in order to draw a card at the end of his/her turn.
    """

    def __init__(self):
        self.cards()

    def __str__(self):
        if self.cards: 
            rep = ""
            for card in self.cards: 
                rep += str(card) + " "
            else: 
                rep = "<empty>"
            return rep

    def clear(self):
        self.cards = []
    
    def pick_card(self, position):