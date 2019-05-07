def sumHelperDP( input, len, total, mem ):
    count = 0
    key = str( total ) + ':' + str(len)
    if key in mem:
        print 'key found'
        return mem[key]
    if total < 0:
        return 0
    if total == 0:
        return 1
    if len == 0:
        return 0

    if total == input[len-1]:
        return 1

    if input[len-1] > total:
        count = sumHelperDP( input, len-1, total, mem )
    else:
        count = sumHelperDP( input, len-1, total, mem ) + \
                sumHelperDP( input, len-1, total-input[len-1], mem )
    mem[ key ] = count
    return count

def allSubsetsWithSum( input, target ):
    """
    :type input: List[int]
    : all subsets whose sum is equal to target
    """
    mem = {}
    rL = sumHelperDP( input, len(input), target, mem )
    for key in mem.keys():
        if mem[key] == 1:
            print key
    print rL


allSubsetsWithSum( [ 2, 3, 4, 5, 7, 9, 8], 22 )


