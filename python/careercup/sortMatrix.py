matrix = [ [ 20, 35, 40, 60 ],
           [ 8, 15, 20, 38 ],
           [ 12, 18, 30, 70 ],
           [ 24, 38, 45, 65 ],
         ]

def sortMatrix( m ):
    a = m[0]
    b = m[1]
    i = j = k = 0
    c = [ 0 for index in range( len(a) + len(b)) ]
    while( k < len(a) + len(b) ):
        if( a[i] < b[j] ):
            c[k] = a[i]
            i = i + 1
        else:
            c[k] = b[j]
            j = j + 1
        k = k + 1
        if( i == len(a) and j < len(b) ):
            while( j < len(b) ):
                c[k] = b[j]
                k = k + 1
                j = j + 1
            break
        if( j == len(b) and i < len(a) ):
            while( i < len(a) ):
                c[k] = a[i]
                k = k + 1
                i = i + 1
            break
    m[0] = c
    del m[1]

sortMatrix( m=matrix )
