def sumHelper( input, current, total ):
    count = 0
    if total == 0:
        return 1
    if total < 0 or current < 0:
        return 0

    count += sumHelper( input, current-1, total ) + \
             sumHelper( input, current-1, total-input[current] )
    return count

def allSubsetsWithSum( input, target ):
    """
    :type input: List[int]
    : all subsets whose sum is equal to target
    """
    rL = sumHelper( input, len(input)-1, target )
    print rL


allSubsetsWithSum( [ 2, 3, 4, 5], 14 )
allSubsetsWithSum( [ 2, 3, 8, 4, 5], 14 )
allSubsetsWithSum( [ 2, 3, 8, 4, 5, 9, 7, 6, 10], 16 )


