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
                zI = zI - 1
    return a

b = moveZeroToLeft( a = [ 1, 2, 0, 3, 6, 0, -5 ] )
print b
b = moveZeroToLeft( a = [ 1, 2, 0, 0, 0, 0, -5, 10 ] )
print b
b = moveZeroToLeft( a = [ 1, 0, 0,  2, 0, 0, 3, 0, 0, -5, 10 ] )
print b
b = moveZeroToLeft( a = [ 1, 0, 2,  0, 5, 0, 7, 0, 8, 0, 10 ] )
print b

