def printNonComments( fileName=None ):
    """
    read file and print only what's not
    commented out
    comments are c style
    """
    f = open( fileName, 'r' )
    commentContinued = False
    for line in f:
        subIndex = line.find( "/*" )
        if commentContinued == True:
            endIndex = line.find("*/")
            if endIndex != -1:
                print line[endIndex+2:-1]
                commentContinued = False
                continue
            else:
                continue

        if subIndex != -1:
            endIndex = line.find("*/")
            if endIndex != -1:
                print line[:subIndex] + line[endIndex+2:-1]
            else:
                print line[:subIndex]
                commentContinued = True
        else:
            print line[:-1]

printNonComments( fileName='testMe' )
