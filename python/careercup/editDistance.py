# slap -> slp ( remove one letter )
# slap -> slape ( add one letter )
# slap -> slip ( edit one letter )

def compareWords( bigWord, smallWord ):
    if len( bigWord ) > len(smallWord) + 1:
        return False
    indexS = 0
    count = 0
    for indexB in range( len(bigWord) ):
        if indexS == len(smallWord) - 1:
            break
        if bigWord[indexB] != smallWord[indexS]:
            count = count + 1
        else:
            indexS = indexS + 1
    if count > 1:
        return False
    return True

def isOneDistance( word1, word2 ):
    if len(word1) == len(word2):
        # only one letter is different
        count = 0
        for index in range( len(word1) ):
            if word1[ index ] != word2[ index ]:
                count = count + 1
        if count > 1:
            return False
        return True
    elif len(word1) > len(word2):
        return compareWords( word1, word2 )
    else:
        return compareWords( word2, word1 )



if __name__ == '__main__':
    assert(isOneDistance( 'abc', 'adc' ) ) == True
    assert(isOneDistance( 'abc', 'ade' ) ) == False
    assert(isOneDistance( 'slip', 'slp' ) ) == True
    assert(isOneDistance( 'slap', 'slape' ) ) == True
    assert(isOneDistance( 'slipp', 'slp' ) ) == False
    assert(isOneDistance( 'slip', 'pls' ) ) == False
    assert(isOneDistance( 'slip', 'pils' ) ) == False
    assert(isOneDistance( 'slip', 'lip' ) ) == True
