import random
import copy


class Card():
    def __init__(self,rank,suit):
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
            return("Sylops")
        elif self.rank > 0:
            return f"Green +{self.rank} of {self.suit_name}"
        elif self.rank < 0:
            return f"Red {self.rank} of {self.suit_name}"
        


class Deck():
    def __init__(self):
        self.deck = []
        self.suits = ["C","S","T"]
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
    
    def deal():
        pass

    def draw():
        pass

    def discard():
        pass
    
class Dice():
    def __init__(self):
        self.die1 = [1,2,3,4,5,6]
        self.die2 = [1,2,3,4,5,6]
        
    def roll_dice(self):
        are_same = False
        dice1= random.choice(self.die1)
        dice2= random.choice(self.die2)
        print(dice1)
        print(dice2)
        if dice1 == dice2:
            print("The dice were the same")
            #pass #Redeal the hands
        else:
            print("The dice were not the same")
            #pass #go to the next player's  turn
        
        
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
