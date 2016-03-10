import random
import itertools

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
redCards = [ i+j for i in '23456789TJQKA' for j in 'HD']
blackCards = [ i+j for i in '23456789TJQKA' for j in 'SC']

def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand"
    return max(itertools.combinations(hand,5), key=hand_rank)
    
def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections"
    max_hand_rank = (0,0)
    if '?B' in hand and '?R' in hand:
        indexB = hand.index('?B')
        indexR = hand.index('?R')
        for bcard in blackCards:
            hand[indexB] = bcard
            for rcard in redCards:
                hand[indexR] = rcard
                bh = best_hand(hand)
                best_rank = hand_rank(bh)
                if best_rank > max_hand_rank:
                    best_possible_hand = bh
                    max_hand_rank = best_rank
        return best_possible_hand
    elif '?B' in hand:
        indexB = hand.index('?B')
        for bcard in blackCards:
            hand[indexB] = bcard
            bh = best_hand(hand)
            #print hand, bh
            best_rank = hand_rank(bh)
            if best_rank > max_hand_rank:
                best_possible_hand = bh
                max_hand_rank = best_rank
        return best_possible_hand
    elif '?R' in hand:
        indexR = hand.index('?R')
        for rcard in redCards:
            hand[indexR] = rcard
            bh = best_hand(hand)
            best_rank = hand_rank(bh)
            if best_rank > max_hand_rank:
                best_possible_hand = bh
                max_hand_rank = best_rank
        return best_possible_hand
    else:
        return best_hand(hand)
    return None
            
def test_best_wild_hand():
    #print (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split())))
    assert( sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split())) 
    == ['7C', '8C', '9C', 'JC', 'TC'])
    
    assert( sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
        == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert( sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
        == ['7C', '7D', '7H', '7S', 'JD'])
    return "test_best_wild_hand passes"

def card_ranks(hand):
    " returns ORDERED list of ranks in a hand"
    ranks = [ '--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    if (ranks == [14, 5 , 4 , 3 , 2]):
        ranks = [5, 4, 3, 2, 1]
    return ranks

def straight(ranks):
    " returns TRUE if the hand is straight "
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) ==5

def flush(hand):
    " returns True if hand is flush "
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def kind(number, ranks):
    " returns first rank that hand has exactly n of"
    for r in ranks:
        if ranks.count(r) == number: return r
    return None

def two_pair(ranks):
    """ if there are two pair, return the two ranks as a tuple: 
     (highest, lowest);  otherwise return None"""
    two_pair_count = 0
    two_pair = []
    for r in ranks:
        if ranks.count(r) == 2:
            if r not in two_pair:
                two_pair.append(r)
                two_pair_count += 1
    if (two_pair_count == 2):
        return (two_pair[0], two_pair[1])
    else:
        return None

#                     rank   tuple
# straight flush       8     (8,max(ranks) )
# four of a kind       7     (7, #4, remaining card)
# full house           6     (6, #3, #2)
# flush                5     (5, ranks ) 
# straight             4     (4, max(ranks) )
# three                3     (3, #3, [remaining cards])
# two pairs            2     (2, [ #2H, #2L], remaining card) 
# one pair             1     (1, #2, [remaining cards])
# highest card         0     ([all cards])

def hand_rank(hand):
    " Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand): # straight flush
        return ( 8, max(ranks)) # 2 3 4 5 6
    elif kind(4, ranks): # four of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks): # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand): # flush 
        return (5, ranks)
    elif straight(ranks): # straight 
        return (4, max(ranks))
    elif kind(3, ranks): # 3 of a kind 
        return (3, kind(3,ranks), ranks)
    elif two_pair(ranks): # 2 pairs 
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks): # 1 pair 
        return (1, kind(2,ranks), ranks)
    else: # 1 pair 
        return (0, ranks)
    return None
    
print test_best_wild_hand()
