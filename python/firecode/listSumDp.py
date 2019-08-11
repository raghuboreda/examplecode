def sumHelperDP( input, current, total, mem ):
    count = 0
    key = str( total ) + ':' + str(current)
    if key in mem:
        print 'key found', key, mem[key]
        return mem[key]
    if total == 0:
        return 1
    if total < 0 or current < 0:
        return 0
    count = sumHelperDP( input, current-1, total, mem ) + \
            sumHelperDP( input, current-1, total-input[current], mem )
    mem[ key ] = count
    return count

def allSubsetsWithSum( input, target ):
    """
    :type input: List[int]
    : all subsets whose sum is equal to target
    """
    mem = {}
    rL = sumHelperDP( input, len(input)-1, target, mem )
    for key in mem.keys():
        if mem[key] >= 1:
            print key
    print rL


allSubsetsWithSum( [ 2, 3, 4, 5, 7, 9, 8, 6, 10, 11, 12, 13, 14,15,16], 22 )
#allSubsetsWithSum( [ 2, 3, 4, 5 ], 14 )


