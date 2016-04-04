def negBinary( number ):
    """
    return number base -2
    as binary string
    remember 11/-2 = -6 and not -5
    remember 11%-2 = -1 and not -5
    remember -5/-2 = 2 
    remember -5%-2 = -1 and not 1
    a = -rc + d
    a = -rc + r + d -r
    a = -r( c + 1 ) + d + r
    so add 1 to quotient and base to remainder
    -5 = -2 * 2 + ( -1 )
         -2 * 2 + ( -1 ) + 2  - 2
         -2 * (2 + 1 ) + ( -1 ) + 2
      = -6 - 1 + 2
      = -5
    """
    l = list()
    while( number != 0 ):
        rem = number % -2
        number = number/ -2
        if( rem < 0 ):
            rem += 2
            number += 1
        l.append(rem)
    l.reverse()
    s = ''.join( '0' if l[i] == 0 else '1' for i in range(len(l)) )
    return s

def convert( number, base=2 ):
    """
    return number base b 
    as binary string
    """
    l = list()
    while( number != 0 ):
        rem = number % base
        number = number/ base
        l.append(rem)
    l.reverse()
    if base == 2:
       s = ''.join( '0' if l[i] == 0 else '1' for i in range(len(l)) )
    else:
       s = ''
       for i in l:
           s += str(i)

    return s

if __name__ == '__main__':
    assert negBinary( 8 ) == '11000'
    assert negBinary( 16 ) == '10000'
    assert negBinary( 32 ) == '1100000'
    assert negBinary( 9 ) == '11001'
    assert negBinary( 10 ) == '11110'
    assert negBinary( 11 ) == '11111'
    assert negBinary( 12 ) == '11100'
    assert negBinary( 13 ) == '11101'
    assert negBinary( 14 ) == '10010'
    assert negBinary( 15 ) == '10011'
    assert convert( 1 ) == '1'
    assert convert( 2 ) == '10'
    assert convert( 3 ) == '11'
    assert convert( 5 ) == '101'
    assert convert( 10 ) == '1010'
    assert convert( 11 ) == '1011'
    assert convert( 12 ) == '1100'
    assert convert( 13 ) == '1101'
    assert convert( 14 ) == '1110'
    assert convert( 15 ) == '1111'
    assert convert( 101, base=10 ) == '101'
    assert convert( 2453, base=10 ) == '2453'
    assert convert( 3643, base=10 ) == '3643'
    assert convert( 528, base=10 ) == '528'
