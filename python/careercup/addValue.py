import copy
def reverseL( A ):
    if len(A) == 1:
       return A
    B = copy.copy(A)
    for index, item in enumerate(A):
        B[ len(A)-index-1 ] = item
    return B
 
def sumValue( A, value ):
    """
    0 0 1 + 9 == 0 1 0
    0 8 7 + 9 == 0 9 6
    1 9 7 + 8 == 2 0 5
    2 + 8 == 0 1
    """
    carry = 0
    for i, number in enumerate(A):
        if( value + number >= 10 ):
            rem = (value + number) % 10    
            value = (value + number) / 10
            A[i] = rem
            carry = value
        else:
            rem = number + value
            value = 0
            A[i] = rem
            carry = value
    if( carry > 0):
        A.append(carry)
             
    return A 

def addValue( A, value ):
    """
    0 0 1 + 9 == 0 1 0
    0 8 7 + 9 == 0 9 6
    0 9 7 + 8 == 1 0 5
    """
    B = reverseL(A)
    B = sumValue(B, value)
    C = reverseL(B)
    return C

if __name__ == '__main__':
    assert [ 0, 1, 0] == addValue([ 0, 0, 1], 9)
    assert [ 0, 8, 6] == addValue([ 0, 7, 7], 9)
    assert [ 2, 0, 5] == addValue([ 1, 9, 7], 8)
    assert [ 3, 0, 5] == addValue([ 2, 9, 7], 8)
    assert [ 2, 0, 4] == addValue([ 1, 9, 2], 12)
    assert [ 2, 0, 0] == addValue([ 1, 8, 7], 13)
    assert [ 1, 0, 8] == addValue([ 1, 0, 0], 8)
    assert [1, 0] == addValue([2], 8)
    assert [1, 0, 0] == addValue([3,7], 63)
