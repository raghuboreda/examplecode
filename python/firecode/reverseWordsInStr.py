def reverseWords(input):
    s = ''
    for word in input.split():
        kw = word[::-1]
        s = s + kw + ' '
    return s[:-1]

print reverseWords('Who am is')

