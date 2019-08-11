
def pigLatin():
    print 'This program translates English to Pig Latin.'
    line = raw_input('Enter English text:')
    translation = lineToPigLatin( line )
    print translation
    return 0

def lineToPigLatin( line ):
    '''
    translates each word in the line to Pig Latin. leaving all other 
    characters unchanged. 
    '''
    words = line.split()
    s = ''
    for word in words:
        plWord = wordToPigLatin(word)
        s += plWord
        s += ' '
    return s

def wordToPigLatin( word ):
    '''
    1. If word contains no vowels return original word unchanged.
    2. If word begins with a consonant, extract the set of consants
       up to first vowel. move that set of consonants to end of
       word and add 'ay'.
    3. If word begins with vowel, add "way" to end of word.
    '''
    if isVowel( word[0] ):
        return word + "way"
    l = findFirstVowel( word )
    if l == -1:
        return word
    return word[l:]+word[:l] + "ay"

def isVowel ( character ):
    if character in 'aAeEiIoOuU':
        return True
    return False

def findFirstVowel( word ):
    for i,c in enumerate(word):
        if isVowel( c ):
            return i
    return -1

pigLatin()
