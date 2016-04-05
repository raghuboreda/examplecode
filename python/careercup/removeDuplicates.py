def removeDups( a ):
    """
    a = [ 'cat', 'dog', 'fish', 'cat' ]
    removeDups(a) == [ 'cat', 'dog', 'fish' ]
    """
    b = dict()
    c = list()
    for item in a:
        if item not in b:
            b[item] = True
            c.append( item )
    return c

if __name__ == '__main__':
   assert removeDups( [ 'cat', 'dog', 'fish', 'cat' ]) == [ 'cat', 'dog', 'fish' ]
   assert removeDups( [ 'dog', 'dog', 'fish', 'cat' ]) == [ 'dog', 'fish', 'cat' ]
   assert removeDups( [ 'dog', 'dog', 'dog', 'cat' ]) != [ 'cat', 'dog' ]
   assert removeDups( [ 'dog', 'dog', 'dog', 'cat' ]) == [ 'dog', 'cat' ]
