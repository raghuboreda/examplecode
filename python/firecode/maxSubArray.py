def maxProd( input ):
    '''
    return the maximum contiguous subarray product
    eg: [ 3, 5, 2,0,3, 1] => 30
        [ 3, 2, -1, 0, -2] => 6
        [ -2, 0, -1] => 0
    '''
    prod = 1
    iL = len(input)
    maxProd = input[0]
    for i in range(iL):
        prod = prod * input[i]
        if prod > maxProd:
            maxProd = prod
            if input[i] == 0:
                prod = 1
        else:
            if input[i] == 0:
                prod = 1
            elif input[i] < 0:
                prod = input[i]
    return maxProd

assert maxProd( [3, 5, 2, 0, 3 ,1] ) == 30
assert maxProd( [3,  2, -1, 0 ,-2] ) == 6 
assert maxProd( [3,  2, -1, 0 ,-2, -4] ) == 8 

