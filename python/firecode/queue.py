class Queue( object ):
    def __init__( self ):
        self.enqL = []
        self.deqL = []

    def enqueue( self, item ):
        self.enqL.append( item )

    def dequeue( self ):
        if len(self.deqL) == 0 and len(self.enqL) == 0:
            return None

        if len(self.deqL) > 0:
            item = self.deqL.pop()
            return item
        else:
            while len(self.enqL) > 0:
                item = self.enqL.pop()
                self.deqL.append(item)
            item = self.deqL.pop()
            return item

q = Queue()
q.enqueue( 'Eric' )
q.enqueue( 'Linda' )
q.enqueue( 'peter' )
l = q.dequeue()
print l

from collections import deque
que = deque(['Eric', 'Linda', 'Peter'])
que.append('Myra')
que.append('Cynthia')
l = que.popleft()
print l

                
