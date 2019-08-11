def csum( input, target ):
    '''
    return True if sum of consecutive numbers should be equal to target
    else False
    '''
    sum = 0
    iL = len(input)
    j = 0
    for i in range(iL):
        if sum == target:
            return True
        sum = sum + input[i]
        if sum > target:
            sum = sum - input[j]
            j = j + 1
    return False

print csum( [5, 8, 9, 10, 12], 13 )
print csum( [5, 8, 9, 10, 12], 22 )
print csum( [5, 8, 9, 10, 12], 19 )
print csum( [5, 8, 9, 10, 12], 55 )
