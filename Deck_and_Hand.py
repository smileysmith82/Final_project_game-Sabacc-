import random
import copy

class Card():
    def __init__(self, rank, suit):
        self.rank= int(rank)
        self.suit= suit
        self.selected = False

        if self.suit == 'C':
            self.suit_name = 'Circle'
        elif self.suit == 'S':
            self.suit_name = 'Square'
        elif self.suit == 'T':
            self.suit_name = "Triangle"
            
    def __str__(self):
        if self.rank == 0:
            file_name = "sylops.png"
            return "Sylops"
        elif self.rank > 0:
            file_name = f"g_{self.rank}_{self.suit_name.lower()}.py"
            return f"Green +{self.rank} of {self.suit_name}"
        elif self.rank < 0: 
            file_name = f"r_{self.rank}_{self.suit.lower()}.py"
            return f"Red {self.rank} of {self.suit_name}"
        
class Deck():
    def __init__(self):
        self.deck = []
        self.suits = ["C", "S", "T"]
        for suit in self.suits:
            for rank in range (1,11):
                self.deck.append(Card(rank,suit))
                self.deck.append(Card(-rank,suit))
        for i in range (2):
            self.deck.append(Card(0, ''))
        self.shuffled_deck = []
        
    def print_deck(self):       
        for card in self.shuffled_deck:
            print(card)
            
    def get_deck_length(self):
        return len(self.deck)
    
    def shuffle(self):
        self.shuffled_deck = copy.deepcopy(self.deck)
        random.shuffle(self.shuffled_deck)
        return self.shuffled_deck  
        
class Hand():
    def __init__(self, shuffled_deck, beginning_size = 2):
        self.player1_hand = []
        self.player2_hand = []
        self.draw_pile =shuffled_deck
        self.discard_pile = []
        self.beginning_size = beginning_size
        
    def starting_deal(self,shuffled_deck):
        for i in range(self.beginning_size):
            self.player1_hand.append(self.draw_pile.pop())
            self.player2_hand.append(self.draw_pile.pop())
        self.discard_pile.append(self.draw_pile.pop())
    
    def total_of_hand(self,hand):
        hand_total=0
        for cards in hand:
            hand_total += cards.rank
        return hand_total
    
    def total_player1(self):
        return self.total_of_hand(self.player1_hand)
    def total_player2(self):
        return self.total_of_hand(self.player2_hand)
    
    
class Player_Actions():
    def __init__(self,player1_hand, player2_hand, turn):
        self.player1_hand = player1_hand
        self.player2_hand = player2_hand
        self.player_turn = [Player1, Player2]
        idx = 0
        turn_index = idx % (len(turn)+1)
        turn = player_turn[turn_index]
        
    def draw(self, player1_hand, player2_hand, draw_pile):
        if turn == Player1:
            self.player1_hand.append(self.draw_pile.pop())
        elif turn == Player2:
            self.player2_hand.append(self.draw_pile.pop())
        

    def switch(self, player1_hand, player2_hand, selected_card):
        self.player1_hand.append(self.draw_pile.pop())
        
        if turn == Player1:
            #select_card()
            self.player1_hand.append(self.discard_pile.pop())
            self.discard_pile.append(self.player1_hand.pop(selected_card))
            
        elif turn == Player2:
            #select_card()
            self.player2_hand.append(self.discard_pile.pop())
            self.discard_pile.append(self.player2_hand.pop(selected_card))
        self.idx +=1
        
    def discard_hand(self, player1_hand, player2_hand, turn):
        original1 = len(player1_hand)
        
        original2 = len(player2_hand)
        if turn == Player1:
            for _ in original1:
                discard_pile.append(self.player1_hand.pop())
        elif turn == Player2:
            for _ in original2:
                discard_pile.append(self.player2_hand.pop())

    def fold(self):
    #discard whole hand:
    #end game (if more players, continue without player who folds)
        discard_hand()
        
    
class Dice():
    def __init__(self):
        self.die1 = [1,2,3,4,5,6]
        self.die2 = [1,2,3,4,5,6]
        
    def roll_dice(self, round_counter):
        dice1= random.choice(self.die1)
        dice2= random.choice(self.die2)
        print(dice1)
        print(dice2)
        if dice1 == dice2:
            print("The dice were the same")
            discard_hand()
            for _ in original1:
                draw(player1)
            for _ in original2:
                draw(player2)
                   
        else:
            print("The dice were not the same")
            #end_turn()
            
        round_counter += 1
        
        
def main():
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck.shuffled_deck)
    hand.starting_deal(2)
    player1 = hand.player1_hand
    player2 = hand.player2_hand
    print("Player 1 Hand: ")
    for cards in player1:
        print(cards)
        
    print("\nPlayer 2 Hand: ")
    for cards in player2:
        print(cards)
    print("\nTop of Discard")
    top_of_discard = hand.discard_pile[-1] if hand.discard_pile else None
    print(top_of_discard)
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    #Hover value
    #select card for discard, swap to top card of discard.
    """switch():
    select to switch:
    select card from hand:
    swap selected card with last card added to discard_pile



file_name = color_number_suit
            r_8_t.png
"""
    #
