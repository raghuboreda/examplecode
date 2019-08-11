from collections import defaultdict
def wordSquares( squares ):
    '''
    squares is list of words = [ 'rose', 'owen', 'seen', 'enna', 'kwik', 'stik' ]
    output should be list of perfect squares
    output = [ ['rose',
                'owen',
                'seen',
                'enne'] ]
    Output should have all perfect word squares that can be made.
    length of every word will be same in the input.
    '''
    maxWordLen = len(squares[0])
    pref = defaultdict( list )
    result = []
    for word in squares:
        for i in range(len(word)):
            pref[word[:i]].append(word)
    print pref
    def helper( wordL ):
        if len(wordL) == maxWordLen:
           result.append( wordL )
           return

        start = ''
        for word in wordL:
            start += word[len(wordL)]

        for word in pref[start]:
            helper( wordL + [word])

    for word in squares:
        helper([word])

    return result

l = wordSquares( [ 'area', 'lead', 'wall', 'lady', 'ball' ] )

print l
