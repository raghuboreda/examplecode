import itertools
def recurseStr( str, l ):
    for index in range( len(str) ):
        k = []
        str1 = str[0:index+1]
        str2 = str[index+1:]
        k.append(  str1 )
        recurseStr( str2, k )
        l.append(k)


def makeString( str ):
    l = []
    d = { '1': [ 'A', 'B', 'C' ],
          '2': [ 'D', 'E' ],
          '12' : ['X'],
          '3': ['P','Q'] }
    r = itertools.product( d['1'], d['2'] )
    for (x, y) in list(r):
        l.append( x+y )
    r = itertools.product( l, d['3'] )
    l = []
    for (x, y) in list(r):
        l.append( x+y )
    r = itertools.product( d['12'], d['3'] )
    for (x, y) in list(r):
        l.append( x+y )
    print l


makeString( '123' )


