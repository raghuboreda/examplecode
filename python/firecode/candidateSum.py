rList = []
import copy
def sumHelperDP( input, len, total, mem, 
        rL=None ):
    rLx = []
    if rL != None:
        rLx = copy.deepcopy(rL)
    else:
        rLx = rL
    count = 0

    key = str( total ) + ':' + str(len)
    if key in mem:
        print 'key found'
        return mem[key]
    if total < 0:
        return 0
    if total == 0:
        rList.append( rLx )
        return 1
    if len == 0:
        return 0

    if total == input[len-1]:
        rLx.append(input[len-1])
        rList.append( rLx )
        return 1

    if input[len-1] > total:
        print '3', rLx,  len-1, total
        count = sumHelperDP( input, len-1, total, mem, rL=rLx )
    else:
        print '1', rLx, len-1, total
        count = sumHelperDP( input, len-1, total, mem, rL=rLx ) 
        rLx.append(input[len-1])
        print '2', rLx, len-1, total

        count += sumHelperDP( input, len-1, total-input[len-1], 
                     mem, rL=rLx )
    mem[ key ] = count
    return count

def combinationSum( candidates, target ):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    mem = {}
    rL = sumHelperDP( candidates, len(candidates), target, mem,
            rL=[] )
    print rL, rList

combinationSum( [ 2, 3, 4], 7 )
rList = []
combinationSum( [ 2, 3, 4, 5], 9 )


