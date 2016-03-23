#  input is a dictionary of words
#  first word is a string e.g. cat
#  last word is a string  e.g. dog
#  In every step you can only replace one letter
#  cat -> cot -> cog -> dog
#  Number of steps from firstWord to lastWord is 3
def allPossibleWords( word1 ):
    l = set()
    aToz = 'abcdefghijklmnopqrstuvwxyz'
    for i in range( len( word1 ) ):
        for j in range( len( aToz ) ):
            if i == 0:
                word2 =  aToz[j] + word1[1:] 
            elif i == (len( word1) - 1):
                word2 =  word1[:i] + aToz[j] 
            else:
                word2 = word1[:i]+ aToz[j] + word1[i+1:] 
            l.add( word2 )
    return l

def validWords( d, firstWord=None ):
    allWords = allPossibleWords( firstWord )
    words = list()
    for word in allWords:
        if word in d:
            words.append( word )
    if len(words) > 0:
        return words
    else:
        return None

def wordRecursiveTransform( d, lastWord=None, lookUpPaths=None, 
                            count=0 ):
    count = count + 1
    if len(lookUpPaths) == 0:
        return False, count
    if lastWord in lookUpPaths:
       return True, count
    for word in lookUpPaths:
        if word in d:
            d.remove( word )
    for word in lookUpPaths:
        newLookUpPaths = validWords( d, firstWord=word )
        if newLookUpPaths == None:
            return False, count
        status, cnt = wordRecursiveTransform( d, lastWord=lastWord,
                          lookUpPaths=newLookUpPaths, count=count )
        if status == True:
           return True, cnt
         
    return False, None
    

def wordTransform( d, firstWord=None, lastWord=None ):
    count = 0
    lookUpPaths = validWords( d, firstWord=firstWord )
    status, cnt = wordRecursiveTransform( d, lastWord=lastWord,
        lookUpPaths = lookUpPaths, count=count )
    if status == True:
        print cnt 
    else:
        print 'Path does not exist'
         
catlist = [ 'cot', 'cog', 'dog', 'cap', 'tap', 'lap' ]
peerlist = [ 'rope', 'dope', 'dipe', 'dire', 'dirt', 'felt', 'melt', 'holy' ]

wordTransform( catlist, firstWord='cat', lastWord='dog' )
wordTransform( peerlist, firstWord='rope', lastWord='dope' )
wordTransform( peerlist, firstWord='rope', lastWord='dirt' )
