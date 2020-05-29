def reverseWords(input):
    s = ''
    for word in input.split():
        kw = word[::-1]
        s = s + kw + ' '
    return s[:-1]

def reverseWord(input, s=None):
    """
    example of reversing a word using
    recursion
    """
    if len(input) == 1:
        s += input[0]
    else:
        s += reverseWord(input[1:], s=s)
        s += input[0]
    return s

print reverseWords('Who am is')
s = reverseWord('abcd', s='')
s = reverseWord('Who am is', s='')

