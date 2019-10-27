import numpy as np 

class Deck:
    """
    At the start of the game, Round 1, the 24 island cards are shuffled. 
    Three cards are placed face up besides the game board. 
    The remaining island cards are placed face down into a draw pile next to the three face-up cards. 
    """

    def __init__(self): 
        """
        Calls the shuffle method on the deck of island cards.
        Returns a shuffled list as the draw pile, face down. 
        The three cards at the top of the draw pile are pulled out to be face up. 
        """
        self.island_cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]        
        self.draw_pile = self.shuffle(self.island_cards)
        self.face_up = []
        for i in range(3): 
            self.face_up.append(self.draw_from_pile(self.draw_pile))

    def shuffle(self, cards):
        """
        Method to shuffle the deck of cards. 
        """
        shuffled_cards = np.zeros_like(cards)
        shuffled_cards[:] = cards[:]
        np.random.shuffle(shuffled_cards) 
        return list(shuffled_cards)

    def draw_from_pile(self, cards):
        """
        Method to draw last card from list (or draw pile in this case).
        """
        card_up = cards.pop(0)
        return card_up

    def __str__(self):
        draw_pile_string = ""
        face_up_string = ""
        for i in self.draw_pile:
            draw_pile_string += " " + str(i)
        for i in self.face_up: 
            face_up_string += " " + str(i)
        current_state = "Draw pile:{} Face up cards:{}".format(draw_pile_string, face_up_string)
        return current_state

if __name__ == "__main__":
    
    deck = Deck()
    print(deck)

        


