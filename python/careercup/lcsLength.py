def lcsLength( a, b ):
    m = len(a)
    n = len(b)
    c = [[ 0 for index in range(n+1) ] for index in range(m+1) ]
    for i in range( 1, m+1 ):
        for j in range( 1, n+1 ):
            if a[i-1] == b[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
    return c

def backTrack( c, a, b, i, j ):
    if i == 0 or j == 0:
        return ""
    elif a[i-1] == b[j-1]:
        return backTrack( c, a, b, i-1, j-1 ) + a[i-1]
    else:
        if c[i][j-1] > c[i-1][j]:
            return backTrack( c, a, b, i, j-1 )
        else:
            return backTrack( c, a, b, i-1, j )

a = "abcdebcd"
b = "aacedcbd"
k = lcsLength( a, b )
print backTrack( k, a, b, len(a), len(b) )  

                 
