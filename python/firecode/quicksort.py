def quicksort( a, s, e ):
    if e <= s or s < 0:
        return
    if e == s + 1:
        if a[s] > a[e]:
            tmp = a[e]
            a[e] = a[s]
            a[s] = tmp
        return
    p = e
    i = s
    print s, e
    while i < p:
        if a[i] <= a[p]:
            i += 1
        else:
            tmp = a[p]
            a[p] = a[i]
            a[i] = a[p-1]
            a[p-1] = tmp
            p -= 1
    quicksort(a,s,p-1 )
    quicksort(a,p,e)
    return

a = [5, 30, 8, 19, 16, 55, 19, 64, 42 ]
quicksort(a, 0, len(a)-1)
print a
a = [45, 88, 9, 15, 6, 25, 89, 64, 45, 23, 53, 58, 67,99,102, 5, 15, 10, 40 ]
quicksort(a, 0, len(a)-1)
print a
import random
b = [ random.randint(0, 100) for i in range(40)]
print b
quicksort(b, 0, len(b)-1)
print b
