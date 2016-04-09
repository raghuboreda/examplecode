graph = {0: [1,5],
         1: [0,2,3],
         2: [1,4],
         3: [1,4,5],
         4: [2,3,5],
         5: [0,3,4],
}

def dfsIter( graphD=None, root=None ):
    visited = [] 
    stack = [ root, ] 
    while stack:
        node = stack.pop()
 
        if node not in visited:
            visited.append( node )
            stack.extend( [ x for x in graphD[node] if x not in visited] )

    return visited       

def dfsRecursive( graphD=None, root=None, visited=None ):
    if visited is None:
        visited = [] 
    if root in visited:
        return
    visited.append(root)

    for node in [ x for x in graphD[root] if x not in visited]:
         dfsRecursive( graphD, root=node, visited=visited )

    return visited       

def bfsIter( graphD=None, root=None ):
    visited = []
    stack = [ root, ]
    while len(stack):
        toVisit = []
        for node in stack:
            if node not in visited:
                visited.append( node )
                toVisit.extend( [x for x in graphD[node] if x not in visited] )
        stack = toVisit
    return visited

v = bfsIter ( graphD=graph, root=0 )
print v
