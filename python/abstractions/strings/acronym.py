def acronym( sentence ):
    words = sentence.split()
    acro = ''
    for i in range(len(words)):
        acro += words[i][0]
        l = words[i].find('-')
        NonAlphaFlag = False
        for c in words[i]:
            if NonAlphaFlag:
                acro += c
                NonAlphaFlag = False
            if not c.isalpha():
                NonAlphaFlag = True
    return acro

print acronym( 'World Health Organization' )
print acronym( 'Self-Contained Underwater Breathing Apparatus' )
print acronym( 'Story-Of-The Day' )
