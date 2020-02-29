def setAllBits( n, m, i, j ):
    """
    set all bits between i and j in N equal to M
    M becomes a substring of N located at i and starting at j
    Input   N = 100000000000, M = 10101, i = 2, j = 6
    Output: N = 100001010100
    """
    # zero all bits between i and j in N
    mask = (1 << (j+1) -1 ) & ~((1 << (i+1)) - 1)
    n =  (n & (~mask) )
    n |= ( m<<i )
    return n

def countSetBits( n ):
    count = 0
    while( n ):
        n &= n - 1
        count += 1
    return count 

def binary(s):
    return str(s) if s <= 1 else binary(s>>1) + str(s&1)

def reverse16bitNum( x ):
    i = 0
    j = 15
    while i < j:
        if ( (x >> i) & 1 != (x >> j) & 1 ):
            mask = ( 1 << i | 1 << j )
            x ^= mask
        i += 1
        j -= 1
    return x

PRECOMPUTED_REVERSE = [ reverse16bitNum(x) for x in range(64)]
#print binary(setAllBits( 16, 3 , 1, 2 ))
#print countSetBits(5), countSetBits(9), countSetBits(14) 

