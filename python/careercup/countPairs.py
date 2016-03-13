def CountPairs( k=1, S=[1] ):
    """
    Given a integer k
    Subset S of set { 0, 1, 2,..., 2^k-1 }
    Return count of pairs (a,b) where a and b are from S
    and a < b and a & b == a
    """
    if len(S) == 1:
       return 0
    # sort S in ascending order
    S.sort()
    count = 0
    for index in range(1, len(S)):
       b = S[index]
       if b > k:
          break
       for j in range(0, index):
           a = S[j]
           if a & b == a:
              print a,b
              count = count + 1
    print count
    return count 

if __name__ == '__main__':
   assert CountPairs() == 0
   assert CountPairs( k=7, S=[2,5,7]) == 2
   assert CountPairs( k=7, S=[2,3,4,5,6,7,8,9,10,11,12]) == 9
   assert CountPairs( k=7, S=[1,2,3,4,5,6,7,8,9,10,11,12]) == 12
    
