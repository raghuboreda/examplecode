#from itertools import permutations
#s = 'cap'
#p = [''.join(p) for p in permuations(s) ]
#k = set(p)

def permuteString( s, step=0 ):
    if step == len(s):
        return ''.join(s)

    for index in range( step, len(s) ):
        stringCopy = [ c for c in s ]
        if step != index:
            stringCopy[step], stringCopy[index] = stringCopy[index], stringCopy[step]
        permuteString( stringCopy, step+1 )

def permuteIntoList( s, step=0, stringList=None ):
    if step == len(s):
        print ''.join(s)
        dest =  ''.join(s)
        stringList.append( dest )
        return stringList

    if step == 0:
       stringList = list()

    for index in range( step, len(s) ):
        stringCopy = [ c for c in s ]
        if step != index:
            stringCopy[step], stringCopy[index] = stringCopy[index], stringCopy[step]
        permuteIntoList( stringCopy, step+1, stringList=stringList )

    return stringList

permuteString( 'cap' )
s = permuteIntoList( 'less' )
print set(s)
