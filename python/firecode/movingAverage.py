from collections import deque
class MovingAverage( object ):
    def __init__( self, size ):
        self.size = size
        self.asum = 0
        self.q = deque()


    def next( self, val):
        if len(self.q) < self.size:
            self.asum += val
            self.q.append(val)
            average = self.asum/(1.0*len(self.q))
        else:
            v = self.q.popleft()
            self.asum -= v
            self.asum += val
            self.q.append(val)
            average = self.asum/(1.0*self.size)
        return average


