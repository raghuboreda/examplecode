def spiral( matrix ):
    '''
    spiral through a 2D matrix
    input is [ [ 1, 2, 3], [4, 5, 6], [7, 8, 9] ]
    output is [ 1, 2, 3, 6, 9, 8, 7, 4, 5 ]
    [ [ 1, 2, 3, 4]                  
      [ 5, 6, 7, 8]
      [ 9, 10, 11, 12]
      [13, 14, 15, 16]
    ]

    => [ 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10 ]
    '''
    rL = len(matrix)
    cL = len(matrix[0])
    outL = []
    iterNum = 1
    spiralCnt = 0
    while iterNum <= ( rL * cL ):
        if iterNum > (2 * rL + 2*cL - 4 ):
            spiralCnt = 1
        rs = 0 + spiralCnt
        re = rL - spiralCnt
        cs = 0 + spiralCnt
        ce = cL - spiralCnt
        if ( rs < re and cs < ce ):
            tmpL = manipulation( rs, re, cs, ce )
        else:
            tmpL = [ (rs, cs) ]
        for (rI, cI) in tmpL:
            #print rI, cI
            outL.append( matrix[rI][cI] )
        iterNum = iterNum + len(tmpL) 
        print iterNum
    return outL

def manipulation( rowStart, rowEnd, colStart, colEnd ):
    scL = []
    for j in range( colStart, colEnd ):
        scL.append( (rowStart, j) )
    for j in range( rowStart+1, rowEnd ):
        scL.append( (j, colEnd-1) )
    for j in range( colEnd-1-1, colStart-1, -1 ):
        scL.append( ( rowEnd-1, j) )
    for j in range( rowEnd-2, rowStart, -1 ):
        scL.append( ( j, colStart) )
    return scL

print spiral( [[1,2,3], [4, 5, 6], [7,8,9]] )
print spiral( [[1,2,3,10], [4, 5, 6,11], [7,8,9,12]] )
print spiral( [[1,2,3,10]] )



