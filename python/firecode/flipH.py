def flipH(l=None):
    rC = len(l)
    cC = len(l[0])
    for rI in range( rC/2 ):
        for cI in range( cC ):
            print rC, cC
            temp = l[rI][cI]
            l[rI][cI] = l[rC-1-rI][cI]
            l[rC-1-rI][cI] = temp
    print l

def flipHH(l=None):
    rC = len(l)
    for rI in range( rC/2 ):
        temp = l[rI]
        l[rI]=l[rC-1-rI]
        l[rC-1-rI] = temp
    print l

flipH(l=[[1,1,1],[2,2,2],[3,3,3]])
flipHH(l=[[1,0,1],[1,0,1]])
flipHH(l=[[7,0,1],[1,0,1],[9,1,8]])
