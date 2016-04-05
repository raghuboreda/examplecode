class Node( object ):
    def __init__( self, key ):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def insert( self, nodeL, nodeR ):
        if self.left is None and self.right is None:
            self.left = nodeL
            nodeL.parent = self
            self.right = nodeR 
            nodeR.parent = self
        elif nodeL.key == 'D':
            self.left.insert( nodeL, nodeR )
        elif nodeL.key == 'F':
            self.right.insert( nodeL, nodeR )

class Tree( object ):
    def __init__( self, klass=Node ):
        self.root = None
        self.klass = klass

    def insert( self, keyLeft=None, keyRight=None ):
        if keyLeft is not None:
            nodeLeft = self.klass( keyLeft )
        if keyRight is not None:
            nodeRight = self.klass( keyRight )

        if self.root is None:
            self.root = nodeLeft
            return
        else:
            self.root.insert( nodeLeft, nodeRight )
        return
  
def bfsWalk( tree ):
    toVisit = [ tree.root ]
    while( len(toVisit) ):
        nextVisitNodes = []
        for node in toVisit:
            print node.key,
            if node.left is not None:
               nextVisitNodes.append( node.left )
            if node.right is not None:
               nextVisitNodes.append( node.right )
        toVisit = nextVisitNodes
    print 'BFS Walk done '

def dfsNodeWalk( node, visitedNodes=None ):
    if node in visitedNodes:
        return
    else:
        visitedNodes[ node ] = True
    print node.key
    if node.left:
       dfsNodeWalk( node.left, visitedNodes=visitedNodes )
    if node.right:
       dfsNodeWalk( node.right, visitedNodes=visitedNodes )

def dfsWalk( tree ):
    root = tree.root
    visitedNodes = dict()
    dfsNodeWalk( root, visitedNodes = visitedNodes )
    

tree = Tree()
tree.insert( keyLeft='A' )
tree.insert( keyLeft='B', keyRight='C' )
tree.insert( keyLeft='D', keyRight='E' )
tree.insert( keyLeft='F', keyRight='G' )

bfsWalk( tree )
dfsWalk( tree )
  
