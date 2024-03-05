import pygame
import random
import copy


class Card():
    def __init__(self,rank,suit):
        self.rank=0
        self.suit= ''
        self.selected = False


        if self.suit == 'C':
            self.suit = 'circle'
        elif self.suit = 'S':
            self.suit = 'square'
        elif self.suit == 'T':
            self.suit= "triangle"
    


class Deck():
    def __init__(self):
        self.Deck = []
