import math
import random
import Deck_and_Hand
            
            
class AI_Player():
    
    def calculate_total(self, hand):
        total = Deck_and_Hand.total_player2(hand)
        return total

    def make_move(self, discard_top, draw_pile):
        if self.calculate_total() == 0:
            Deck_and_Hand.stand()
            
        elif discard_top is not None:
            for card in self.hand:
                new_total = (total - card.rank)
                if new_total + discard_top.rank <= abs(1):
                    player2_hand.append(discard_pile[-1])
                    discard_pile.pop()
                    dealer_hand.append('down_backside.png')
                    
        else:
            Deck_and_Hand.draw()
