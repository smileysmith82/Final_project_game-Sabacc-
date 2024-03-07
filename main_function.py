import pygame
import random
import copy


class Card():
    def __init__(self,rank,suit):
        self.rank= int(rank)
        self.suit= suit
        self.selected = False


        if self.suit == 'C':
            self.suit_name = 'circle'
        elif self.suit == 'S':
            self.suit_name = 'square'
        elif self.suit == 'T':
            self.suit_name = "triangle"
            
    def __str__(self):
        
        if self.rank == 0:
            return("Sylops")
        elif self.rank > 0:
            return f"Green +{self.rank}"
        elif self.rank < 0:
            return f"Red {self.rank}"
        


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
        self._shuffled_deck = []
        
    def print_deck(self):       
        for card in self._shuffled_deck:
            print(card)
            
    def get_deck_length(self):
        return len(self.deck)
    
    
    def shuffle(self):
        self._shuffled_deck = copy.deepcopy(self.deck)
        random.shuffle(self._shuffled_deck)
        return self._shuffled_deck
        
        
class Hand():
    def __init__(self, beginning_size = 2):
        player1_hand = []
        player2_hand = []
        draw_pile =self._shuffled_deck
        discard_pile = []
    def deal():
        pass

    def draw():
        pass

    def discard():
        pass
        
        
            
deck = Deck()
deck.shuffle()
deck.print_deck()

#print(f"Length of Deck:", deck.get_deck_length())



