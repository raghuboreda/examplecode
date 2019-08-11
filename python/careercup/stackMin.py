class StackMin( object ):
    def __init__( self, size ):
        self.a = list()
        self.size = size
        self.minimum = (1<<31)

    def pop( self ):
        if len(self.a):
           b = self.a.pop()
           if b[0] == self.minimum:
               if len(self.a):
                   self.minimum = self.a[len(self.a)-1][1]
               else:
                   self.minimum = (1<<31)
           return b[0]
        return -1

    def push( self, value ):
        if value < self.minimum:
            self.minimum = value
        self.a.append((value, self.minimum))

    def min( self ):
        if len(self.a):
            return self.minimum

y = StackMin( 25 )
y.push(10)
y.push(15)
y.push(9)
y.push(4)
y.push(18)
print 'Minimum is ', y.min()
print y.pop()
print y.pop()
print 'Minimum is ', y.min()
