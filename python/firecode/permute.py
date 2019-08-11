import itertools
s = 'abc'
k = [ c for c in s ] 
l = []
for (x,y,z ) in itertools.permutations(k):
    l.append( x+y+z )
print l


