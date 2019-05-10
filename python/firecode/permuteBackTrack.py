def permuteHelper( strL, chosen):
    # print strL, chosen
    # base case
    if len(strL) == 0:
        s = ''.join(c for c in chosen)
        print '##', s 
        return

    for i in range(len(strL)):
        # choose
        chosen.append(strL[i])
        del strL[i]
        # explore
        permuteHelper( strL, chosen )

        # un-choose
        v = chosen.pop()
        strL.insert(i, v)

def permute( str ):
    permuteHelper(list(str), chosen=[])

#permute( 'mat' )
#permute( 'abcd' )
permute( 'abcde' )
