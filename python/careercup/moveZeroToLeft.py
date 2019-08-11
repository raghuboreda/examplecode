def moveZeroToLeft( a=None ):
    zI = len(a) - 1
    nzI = zI
    while( nzI >= 0 and zI >= 0 ):
        if a[zI] != 0:
            zI = zI - 1
            nzI = nzI - 1
        else:
            if a[nzI] == 0:
                nzI = nzI - 1
            else:
                a[nzI], a[zI] = a[zI], a[nzI]
                # decrement zI
                zI = zI - 1
    return a

def moveZeroToLeft2 ( a=None ):
    zI = len(a) - 1
    nzI = zI
    while( nzI >= 0 ):
        if a[nzI] != 0:
            if a[zI] == 0:
                a[nzI], a[zI] = a[zI], a[nzI]
            while zI > nzI and a[zI] != 0:
                zI -= 1
        else:
            while zI > nzI and a[zI] != 0:
                zI -= 1
        
        nzI -= 1
    return a
        


b = moveZeroToLeft( a = [ 0, 1, 1, 1, 1, 1, 0, 1 ] )
print b
b = moveZeroToLeft( a = [ 0, 1, 1, 1, 1, 1, 0,0, 0, 1, 0,0 ,0,1,1,0 ] )
print b
b = moveZeroToLeft2( a = [ 0, 1, 1, 1, 1, 1, 0,0, 0, 1, 0,0 ,0,1,1,0 ] )
print b
b = moveZeroToLeft2( a = [ 0, 1, 1, 1, 1, 1, 0,0, 0, 1, 0,0 ,0,1,1,0, 98, -123, 33, 0, 0, 55, 0, 78, 98,0 ] )
print b

