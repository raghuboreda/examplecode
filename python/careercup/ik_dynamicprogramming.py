def get_maximum_profit(price):
    """
    Rod cutting problem
    What cut's give maximum profit.
    :param price: price for 1 inch, 2 inch, 3 inch cuts
    :return: maximum profit
    """
    # What is the recurrence equation
    # T(n) = max ( T(n-1) + P(1), T(n-2) + P(2), etc )
    profit = [0]*(len(price)+1)
    n = len(price)
    for i in range(1, n+1):
        profit[i] = max([profit[i-1-j] + price[j] for j in range(i)])
    return profit[n]

def num_ways_to_make_change( coins, amount):
    """
    number of ways to make change using coins in coin array to make up amount
    :param coins: array of denominations of coins
    :param amount: amount to make change
    :return: Number of ways to describe the amount
    """
    # What is the recurrence equation
    # T(n) = Sum of all the ways coins can be expressed to get the sum n
    # T(n) = T(n-c') + T(n')
    # If coin denominations are 1, 3, 5
    # Use 1, 2, 3 to make up 11, T(0) = 1                           1, 3, 5 --> 6
    # 1 -> 1 way ( 1 )
    # 2 -> 1 Way  ( [1,1] )
    # 3 -> 2 Ways ( [1,1,1],,[3] )
    # 4 -> 2 Ways ( [1,1,1,1], [3,1] )
    # 5 -> 3 Ways ( [1,1,1,1,1], [1,1,3], [5])
    # 6  ->  4 Ways ( 6 1s, 2 3s, 3 1s 3, [5,1] )
    # 7 ->   4 Ways ( 7 1s, [3,3,1], [3, 1,1,1,1], [5, 2] )
    # 8 ->   5 Ways ( 8 1s, [3,3,2], [3,1,1,1,1,1], [5,2,1], [5,3] )
    # coins 1, 3, 5
    # idx   0  1 2 3 4 5 6 7 8   coin
    # dp_   1  1 1 1 1 1 1 1 1   ( 1 )
    #       1  1 1 2 2 2 3 3 3   ( 3 )
    #       1  1 1 2 2 3 4 4 5   ( 5 )
    dp_ = [0]*(amount+1)
    dp_[0] = 1
    for c in coins:
        for i in range(c, amount+1):
            dp_[i] += dp_[i-c]
    return dp_[amount]

#print(num_ways_to_make_change([1,3,5], 12))

def combination_sum_ways(arr, target):
    """
    Given a array with distinct integers, output all possible selection of integers so that their sum is
    equal to target
    :param arr: array of distinct positive integers
    :param target: integer
    :return: Number of ways to make the target
    """
    # use DP to find number of ways to make up target sum 1, 2...target
    # number of ways to make target from arr of length n -1
    # T(n) = sum of ways to make 1 + sum of ways to make target (n-1) etc
    # sort the input array
    arr.sort()
    # arr 2, 3, 5 target 8
    # idx   0  1 2 3 4 5 6 7 8   target 8
    # dp_   1  0 1 0 1 0 1 0 1   ( 2 )
    #       1  0 1 1 1 1 2 1 2   ( 3 )
    #       1  0 1 1 1 2 2 2 3   ( 5 )
    dp_ = [0] * (target + 1)
    dp_[0] = 1
    for c in arr:
        for i in range(c, target + 1):
            dp_[i] += dp_[i - c]
    return dp_[target]

def combination_sum(arr, target):
    """
    Given a array with distinct integers, output all possible selection of integers so that their sum is
    equal to target
    :param arr: array of distinct positive integers
    :param target: integer
    :return: list of integers which make up the target
    """
    # use DP to find number of ways to make up target sum 1, 2...target
    # number of ways to make target from arr of length n -1
    # T(n) = sum of ways to make 1 + sum of ways to make target (n-1) etc
    # sort the input array
    arr.sort()
    # arr 2, 3, 5 target 8
    # idx   0  1 2 3 4 5 6 7 8   target 8
    # dp_   1  0 1 0 1 0 1 0 1   ( 2 )
    #       1  0 1 1 1 1 2 1 2   ( 3 )
    #       1  0 1 1 1 2 2 2 3   ( 5 )
    dp_ = [[] for _ in range(target+1)]

    for c in arr:
        for i in range(c, target + 1):
            if i == c:
                dp_[i].append([c])
            else:
                for blist in dp_[i-c]:
                    dp_[i].append(blist + [c])

    return dp_[target]
print(combination_sum([2,3,5], 12))

def longest_palindrome_sequence(s):
    # recurrence equation
    # P(i,j) is defined as palindrome of Sequence Si...Sj
    # base case:
    #     1 length palindromes P(i,j) = True if i == j
    #     2 length palindromes P(i,j) = True if Si == Si+1 else False
    # recursive case
    #     3 length palindromes are dependent on 2 length palindromes and so on.
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for c1 in range(2, n+1):
        for i in range(n-c1+1):
            j = i + c1 - 1
            if s[i] == s[j] and c1 == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])

    return dp[0][n-1]

# find the largest sub square matrix with all 1's
# input:
# 1, 0, 1, 0
# 0  1, 1, 1
# 1  0, 1, 1
# output: 2
# dp(i,j) = dp(i-1,j-1) + 1 if matrix[i-1][j] == 1, matrix[i][j-1] == 1 and matrix[i][j]=1
# base case
# dp(0,j) = matrix[0][j] for j in range(len(matrix[0]))
# dp(i,0) = matrix[i][0] for i in range(len(matrix))
#print(longest_palindrome_sequence("abcddcbjefmalayalam"))
def find_largest_sub_square_matrix( matrix ):
    rmax = len(matrix)
    cmax = len(matrix[0])
    for i in range(1, rmax):
        for j in range(1, cmax):
            if matrix[i][j] == 1:
                matrix[i][j] = 1 + min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1])

    max_value = 0
    for i in range(rmax):
        for j in range(cmax):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
    return max_value

