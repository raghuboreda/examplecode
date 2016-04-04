def multiplyValues( a=None ):
    """
    input is [ 2, 3, 1, 4 ]
    output is [ 12, 8, 24, 6 ]
    each field of output has product of all fields on input array 
    except itself.
    Time is O(n)
    Space is O( 2n )
    """
    prod = 1
    leftP = [ 1 for i in a ] 
    rightP = [ 1 for i in a ] 
    output = [ 1 for i in a ] 

    prod = 1
    for index in range(len(a)):
        if( index == 0 ):
            leftP[ index] = 1
            continue
        prod = prod * a[index-1]
        leftP[index] = prod 

    prod = 1
    inputLen = len(a)
    index = inputLen - 1
    while( index >= 0 ):
        if ( index == len(a) - 1 ):
            rightP[index] = 1
            index = index - 1
            continue
        prod = prod * a[index+1]
        rightP[index] = prod 
        index = index - 1

    for index in range(len(a)):
        output[index] = leftP[index] * rightP[index]
    return output 

def multiply2Values( a=None ):
    """
    input is [ 2, 3, 1, 4 ]
    output is [ 12, 8, 24, 6 ]
    each field of output has product of all fields on input array 
    except itself.
    Time is O(n)
    Space is O( n )
    """
    prod = 1
    products = [ 1 for i in a ] 

    prod = 1
    for index in range(len(a)):
        if( index == 0 ):
            products[ index] = 1
            continue
        prod = prod * a[index-1]
        products[index] = prod 

    prod = 1
    inputLen = len(a)
    index = inputLen - 1
    while( index >= 0 ):
        if ( index == len(a) - 1 ):
            index = index - 1
            continue
        prod = prod * a[index+1]
        products[index] = prod * products[index] 
        index = index - 1
    return products 

if __name__ == '__main__':
    assert multiplyValues( a=[2,1,3,4]) == [ 12, 24, 8, 6 ] 
    assert multiplyValues( a=[ 1, 3, 7] ) == [ 21, 7, 3 ] 
    assert multiply2Values( a=[ 1, 3, 7] ) == [ 21, 7, 3 ] 
    assert multiply2Values( a=[2,1,3,4]) == [ 12, 24, 8, 6 ] 
