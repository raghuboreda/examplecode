class Solution(object):
    def totalHammingDistance(self, input):
        b = dict()
        hd = dict()
        def maxLen( x ):
            for i_ in range(32, -1, -1):
                if (x & (1<<i_)) > 0:
                    return i_
        def h1Dist( x, y ):
            p = x^y
            l = maxLen(p)
            count = 0
            for i_ in range(l+1):
                if p & (1<<i_) > 0:
                    count += 1
            return count

        def hDist( x , y, maxL ):
            count = 0
            for i_ in range(maxL+1):
                if ( (x & (1<<i_)) != (y & (1<<i_)) ):
                    count += 1
            print x, y, count, maxL
            return count

        aL = len(input)
        for i in range(aL):
            b[i] = maxLen( input[i] )

        sum1 = 0
        for i in range(aL-1):
            for j in range(i+1, aL):
                if input[i] > input[j]:
                    mL = b[i]
                    if (input[i], input[j]) in hd:
                        sum1 += hd[(input[i], input[j])]
                    else:
                        sum = hDist( input[i], input[j], mL ) 
                        hd[ (input[i], input[j]) ] = sum
                        sum1 += sum
                        
                else:
                    mL = b[j]
                    sum1 += hDist( input[j], input[i], mL ) 
        sum2 = 0
        for i in range(aL-1):
            for j in range(i+1, aL):
                sum2 += h1Dist( input[i], input[j] )
        return sum1, sum2

sol = Solution()
s1,s2 = sol.totalHammingDistance( [4, 14, 2 ] )
print s1, s2
