import random
import copy

class Card():
    def __init__(self, rank, suit):
        self.rank= int(rank)
        self.suit= suit


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
        self.top_of_discard = None
        
        
    def starting_deal(self,shuffled_deck):
        for i in range(self.beginning_size):
            self.player1_hand.append(self.draw_pile.pop())
            self.player2_hand.append(self.draw_pile.pop())
        self.discard_pile.append(self.draw_pile.pop())
        self.update_discard()
    
    def update_discard(self):
        if self.discard_pile:
            self.top_of_discard= self.discard_pile[-1]
        else:
            self.top_of_discard = None
            
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
    def __init__(self, player1_hand, player2_hand, hand):
        self.player1_hand = player1_hand
        self.player2_hand = player2_hand
        self.hand = hand
        self.player_turn = ["Player1", "Player2"]
        self.current_player = "Player1"
        self.num_players = len(self.player_turn)
        self.idx = 0
        self.dice = Dice(self,hand)
        
    def next_turn(self):
        self.idx += 1
        self.current_player = self.player_turn[self.idx % self.num_players]
        
    def draw(self):
        if self.current_player == "Player1":
            self.player1_hand.append(self.hand.draw_pile.pop())
            self.next_turn()
            
        elif self.current_player == "Player2":
            self.player2_hand.append(self.hand.draw_pile.pop())
            self.dice.roll_dice()
        

    def switch(self, player1_hand, player2_hand, selected_card):
        self.player1_hand.append(self.draw_pile.pop())
        
        if self.current_player == "Player1":
            if selected_card_index is not None and len(discard_pile) > 0 and 0 <= selected_card_index < len(player_hand):
                selected_card = player_hand[selected_card_index]
                player_hand[selected_card_index] = discard_pile.pop()
                discard_pile.append(selected_card)            
            self.next_turn()
            
        elif self.current_player == "Player2":
            opponent_ai.switch()
            self.dice.roll_dice()
        
    def stand():
        if self.current_player == "Player1":
            self.next_turn()
        elif self.current_player == "Player2":
            self.Dice.roll_dice()
        
    def discard_hand(self):
        original1 = len(self.player1_hand)
        original2 = len(self.player2_hand)
        if self.current_player == "Player1":
            for _ in range(original1):
                self.hand.discard_pile.append(self.player1_hand.pop())
            self.hand.update_discard()
        elif self.current_player == 'Player2':
            for _ in range(original2):
                self.hand.discard_pile.append(self.player2_hand.pop())
            self.hand.update_discard()
                
    def fold(self):
        self.discard_hand()
        self.stand()
    
class Dice():
    def __init__(self, player_actions, hand):
        self.die1 = [1,2,3,4,5,6]
        self.die2 = [1,2,3,4,5,6]
        self.round_counter = 1
        self.idx = 0
        self.player_actions = player_actions
        self.turn = player_actions
        self.hand = hand

        
    def roll_dice(self):
        dice1 = random.choice(self.die1)
        dice2 = random.choice(self.die2)
        if dice1 == dice2:
            print("The dice were the same")
            original1 = len(self.player_actions.hand.player1_hand)
            original2 = len(self.player_actions.hand.player2_hand)
            self.player_actions.discard_hand()
            self.player_actions.next_turn()
            self.player_actions.discard_hand()# Should now be player 1's turn

            for _ in range(original1):
                self.player_actions.draw()
            self.player_actions.next_turn()
            for _ in range(original2):
                self.player_actions.draw()
            self.player_actions.next_turn()
        else:
            print("The dice were not the same")
            self.idx += 1
        self.round_counter += 1

        
def main():
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck.shuffled_deck)
    hand.starting_deal(2)
    player1 = hand.player1_hand
    player2 = hand.player2_hand
    turn = "Player1"
    print("Player 1 Hand: ")
    for cards in player1:
        print(cards)
        
    print("\nPlayer 2 Hand: ")
    for cards in player2:
        print(cards)
    print("\nTop of Discard")
    hand.update_discard()
    print(hand.top_of_discard)
    player_actions = Player_Actions(player1, player2, hand)  # Create an instance of Player_Actions

    dice = Dice(player_actions, hand)
    dice.roll_dice()      
    for cards in player1:
        print(cards)
if __name__ == "__main__":
    main()


