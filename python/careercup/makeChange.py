def bestChange( denom, s=None ):
    """
    give a infinite number of quarters, dimes , nickels and pennies
    write code to calculate way to represent n cents
    with least number of quarters, dimes and pennies
    """
    if denom > 25:
        s = 'quarters = %d ' % denom/25
        bestChange( denom%25, s=s )
    elif denom > 10:
        s += 'dimes = %d ' % denom/10
        bestChange( denom%10, s=s )
    elif denom > 5:
        s += 'nickels = %d ' % denom/5
        bestChange( denom%5, s=s )
    else:
        s += 'pennies = %d ' %  denom
        print s

def makeChange( denom, s=None ):
    """
    give a infinite number of quarters, dimes , nickels and pennies
    write code to calculate number of ways of representing n cents
    """
