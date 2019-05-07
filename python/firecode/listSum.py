import copy
def sumHelper( input, len, total ):
    count = 0
    if total < 0:
        return 0
    if total == 0:
        return 1
    if len == 0:
        return 0

    if total == input[len-1]:
        return 1

    if input[len-1] > total:
        count += sumHelper( input, len-1, total )
    else:
        count += sumHelper( input, len-1, total ) + \
                sumHelper( input, len-1, total-input[len-1] )
    return count

def allSubsetsWithSum( input, target ):
    """
    :type input: List[int]
    : all subsets whose sum is equal to target
    """
    rL = sumHelper( input, len(input), target )
    print rL


allSubsetsWithSum( [ 2, 3, 4, 5], 14 )


