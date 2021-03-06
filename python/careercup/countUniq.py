def countUniq( a ):
    """
    a = [ 8, 8, 8, 9, 9, 11, 15, 16, 16, 16 ]
    output :
        8 : 3
        9 : 2
       11 : 1
       15 : 1
       16 : 3
    """
    countD = dict()
    if a[0] != a[len(a) - 1]:
        countU( a, countDict= countD )
    else:
        countD[a[0]] = len(a)
    for k,v in countD.items():
        print k, ':', v
    return

def countU ( a1, countDict=None ):
    print a1
    if len(a1) == 1:
        if a1[0] in countDict:
            countDict[a1[0]] += 1 
            return
        else:
            countDict[a1[0]] = 1 
            return
       
    if a1[0] != a1[len(a1) - 1]:
        countU( a1[:len(a1)/2], countDict=countDict ) 
        countU( a1[len(a1)/2:], countDict=countDict ) 
    else:
        if a1[0] in countDict:
            countDict[ a1[0] ] += len(a1)
        else:
            countDict[ a1[0] ] = len(a1)
    return

def countUniqChar( a ):
    c = [ 0 for i in range(256) ]
    j = 0
    rc = 0
    while( j < len(a) ):
        c[ord(a[j])] = c[ord(a[j])] + 1
        j = j + 1
    for i in range(256):
        if c[i] > 1:
            rc = 1
            break
    if rc:
        print a, ' is not Unique'
        return
    print a, ' is Unique'
    

if __name__ == '__main__':
    countUniq( [5,5,5,5,6] )
    countUniq( a=[ 8, 8, 8, 9, 9, 11, 15, 16, 16, 16 ] )
    countUniqChar( a='whoisthat' )
    countUniqChar( a="I'm Unique" )
