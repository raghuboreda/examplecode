#
# Hopper, Kay, Liskov, Perlis and Ritchie live on different floors of a five-
# floor apartment building.
#
# Hopper does not live on the top floor.
# Kay does not live on the bottom floor.
# Liskov does not live on either top or bottom floor.
# Perlis lives on a higher floor than does Kay.
# Ritchie does not live on a floor adjacent to Liskov's.
# Liskov does not live on a floor adjacent to Kay's.

# Where do people live.

import itertools

def floorPuzzle():
    """
    returns a list of five floor numbers denoting the floor of
    Hopper, Kay, Liskov, Perlis, Ritchie
    """
    for x in itertools.permutations('12345'):
       (Hopper, Kay, Liskov, Perlis, Ritchie) = x
       if Hopper == '5' or \
          Liskov == '5' or Liskov == '1' or \
          Kay == '1':
           continue
       if int(Kay) > int(Perlis):
           continue
       if abs(int(Ritchie) - int(Liskov)) == 1:
           continue
       if abs(int(Liskov) - int(Kay)) == 1:
           continue
       return [ Hopper, Kay, Liskov, Perlis, Ritchie]

l = floorPuzzle()
print l
