from collections import deque
class ZigzagIterator( object ):
    def __init__( self, v1, v2 ):
        """
        initialize v1: List[int]
                   v2: List[int]
        """
        self.q1 = deque(v1)
        self.q2 = deque(v2)
        if len(self.q1):
            self.nextCall = 1
        elif len(self.q2):
            self.nextCall = 2
        else:
            self.nextCall = 0

    def next( self ):
        if self.nextCall == 1:
            if len(self.q1):
                v1 = self.q1.popleft()
            if len(self.q2):
                self.nextCall = 2
            elif len(self.q1):
                self.nextCall = 1
            else:
                self.nextCall = 0
        elif self.nextCall == 2:
            if len(self.q2):
                v1 = self.q2.popleft()
            if len(self.q1):
                self.nextCall = 1
            elif len(self.q2):
                self.nextCall = 2
            else:
                self.nextCall = 0
        else:
            # both lists empty
            assert(0)

    def hasNext( self ):
        return ( len(self.q1) + len(self.q2) > 0 )
