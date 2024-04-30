import random
import Deck_and_Hand
            
            
class AI_Player():
    
    def calculate_total(self, hand):
        total = Deck_and_Hand.total_player2(hand)
        return total

    def check_if_stand(self):
        if self.calculate_total() == 0:
            return True
        else:
            return False

    def check_if_switch(self, discard_top):
        total = self.calculate_total()
        if discard_top is not None:
            for card in self.hand:
                new_total = (total - card.rank)
                if new_total + discard_top.rank <= abs(1):
                    player2_hand.append(discard_pile[-1])
                    discard_pile.pop()
                    dealer_hand.append('down_backside.png')
        pass
