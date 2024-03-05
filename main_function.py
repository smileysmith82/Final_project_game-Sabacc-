import pygame
import random
import copy


class Card():
    def __init__(self,rank,suit):
        self.rank= rank
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
            print("Sylops")
        else:
            return f"{self.rank} of {self.suit}"
    


class Deck():
    def __init__(self):
        self.deck = []
        self.suits = ["C","S","T"]
        for suit in self.suits:
            for rank in range (1,11):
                self.deck.append(Card(rank,suit))
        for i in range (2):
            self.deck.append(Card(0, ''))
    def print_deck(self):
        for card in self.deck:
            print(card)
            
deck = Deck()
deck.print_deck()        


