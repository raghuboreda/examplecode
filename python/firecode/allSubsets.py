import copy
def subsetHelper( input, len ):
    if len == 1:
#       return [].append([].append(input[len-1])
        l = []
        l.append(input[len-1])
        k = []
        k.append(l)
        return k
    resL = subsetHelper( input, len-1 )
    l = copy.deepcopy(resL)
    for item in resL:
       item.append( input[len-1] )
       l.append(item)
    l.append( [input[len-1]] )
    return l

def powersetHelper( input, i, al=None, s=None):
    if al not in s:
        s.append(al)
    if i == len(input):
        return
    bl = copy.deepcopy(al)
    bl.append(input[i])
    powersetHelper( input, i+1, al=bl, s=s )
    powersetHelper( input, i+1, al=al, s=s )

def allSubsets( input ):
    """
    :type input: List[int]
    :rtype: List[List[int]]
    """
    rL = subsetHelper( input, len(input) )
    print rL

def powerSets( input ):
    """
    :type input: List[int]
    :rtype: List[List[int]]
    """
    s = []
    powersetHelper( input, 0, al=[], s=s )
    print s 


allSubsets( [ 2, 3, 4, 5] )
powerSets( [ 6, 7, 8, 9] )


