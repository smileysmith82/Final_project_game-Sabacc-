import math
import random
import Deck_and_Hand
            
            
class AI_Player():
    
    def calculate_total(self, hand):
        total = hand.total_player2()
        return total

            
    def make_move(self, player_actions):
        if self.calculate_total(player_actions.hand) == 0:
            player_actions.stand()        
        else:
            for card in player_actions.player2_hand:
                new_total = (player_actions.hand.total_player2() - card.rank)
                if new_total + player_actions.hand.top_of_discard.rank == 0:
                    player_actions.player2_hand.append(player_actions.hand.discard_pile.pop())
                    player_actions.hand.discard_pile.append(card)
                    player_actions.hand.update_discard()
                    player_actions.next_turn()
            player_actions.draw()
