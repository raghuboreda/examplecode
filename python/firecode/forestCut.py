def maximizeWood( a ):
    l = len(a)
    j,k,i = l - 1, l - 2, l-3
    sumJ, sumK = a[j], a[k]
    max = sumJ if sumJ > sumK else sumK

    while i >= 1 :
        sumJ += a[i]
        if sumJ > max:
            max = sumJ
        sumK += a[i-1]
        if sumK > max:
            max = sumK
        i -= 1

    print 'max wood ', max

maximizeWood( [5, 15, 6, 9,7,4] )


