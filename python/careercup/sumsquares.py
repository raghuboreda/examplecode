from math import sqrt, ceil
def sumSquares( c ):
    """
    10 = 3^2 + 1^2
    find number of ways which c
    can be written as combination of two squares
    """
    x = int(ceil(sqrt(c)))
    i = 0
    while( i <= x ):
        sqsum = i**2 + x**2
        if sqsum == c:
            print i, x
            i = i + 1
            x = x - 1
        elif sqsum > c:
            x = x - 1
        else:
            i = i + 1

def twoSum( c ):
    x = int(ceil(sqrt(c)))
    l = [ y*y for y in range(x+1) ]
    i = 0
    j = len(l) - 1
    while( i <= j ):
        sum = l[i] + l[j] 
        if sum == c:
            print i, j
            i = i + 1
            j = j - 1
        elif sum > c:
            j = j - 1
        else:
            i = i + 1

sumSquares( 20 )
twoSum( 20 )
twoSum( 100 )
sumSquares( 100 )
sumSquares( 1000 )
