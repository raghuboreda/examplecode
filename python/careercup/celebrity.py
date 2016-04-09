# celebrity is a person who knows no one but himself.
# All people know celebrity
# find a celebrity in a given list of N people
# time complexity O(n)

peopleIKnow = {
   0 : [1, 2],
   1 : [2],
   2 : [],
   3 : [2,0],
   4 : [2,0]
}

def knows( i , j ):
    """
    returns True if i knows j
            False if i does not j
    """
    if j in peopleIKnow[i]:
        return True
    else:
        return False

def findCelebrity( a ):
    n = len(a)
    i = 0
    j = 1
    notCelebrity = dict()
    while( i < n and j < n ):
        if( knows( i, j ) ) == True:
            # i knows j
            # i is not a celebrity 
            notCelebrity[i] = True
            i = i + 1
            if i == j:
               j = j + 1
        else:
            # i does not knows j
            # j is not a celebrity
            notCelebrity[j] = True
            j = j + 1

    index = 0
    for index in range(n):
        if a[index] not in notCelebrity:
            break
    
    celebrityDoesNotExit = False
    for k in range(n):
        if k == index:
            continue
        if( knows( k, index ) == False ):
            celebrityDoesNotExit = True
            break
    if celebrityDoesNotExit == False:
        print a[index], 'is Celebrity!! Yay!!'
            
findCelebrity( [ 0, 1, 2, 3, 4] )
