import random
import itertools
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
redCards = [i+j for i in '123456789TJQKA' for j in 'SC']
blackCards = [i+j for i in '123456789TJQKA' for j in 'HD']

def deal(hand):
    if '?B' in hand and '?R' in hand:
        indexB = hand.index('?B')
        indexR = hand.index('?R')
        for bcard in blackCards:
            hand[indexB] = bcard
            for rcard in redCards:
                hand[indexR] = rcard
                print hand
    elif '?B' in hand:
        indexB = hand.index('?B')
        for bcard in blackCards:
            hand[indexB] = bcard
            print hand
    elif '?R' in hand:
        indexR = hand.index('?R')
        for rcard in redCards:
            hand[indexR] = rcard
            print hand


deal("5T 8H ?R ?B JC".split())
deal("5T 8H ?R JC JD".split())
