def score( word ):
    l = 0
    for w in word:
        l += letterScore( w )
    return l

def letterScore( character ):
    if character in 'AEILNORSTU':
        return 1
    if character in 'DG':
        return 2
    if character in 'BCMP':
        return 3
    if character in 'FHVWY':
        return 4
    if character in 'K':
        return 5
    if character in 'JX':
        return 8
    if character in 'QZ':
        return 10 

assert score('FARM') == 9
assert score('ARM') == 5
