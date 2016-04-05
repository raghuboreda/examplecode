#!/usr/bin/env python

class BTNode(object):
    """A node in the vanilla Binary tree."""
    
    def __init__(self, parent, k, index=1):
        """Creates a node.
            parent: The node's parent.
            k: key of the node.
        """
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None
        self.index = index
  
    def _str(self):
        """Internal method for ASCII art."""
        label = str(self.key)
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self.left._str()
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right._str()
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and self.parent is not None and \
           self is self.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.': label = ' ' + label[1:]
        if label[-1] == '.': label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle-2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
          [left_line + ' ' * (width - left_width - right_width) + right_line
           for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width
    def __str__(self):
        return '\n'.join(self._str()[0])

    def find(self, k):
        """Finds and returns the node with key k from the subtree rooted at this 
        node.
        k: The key of the node we want to find.
        
        Returns:
            The node with key k.
        """
        if k == self.key:
            return self
        elif self.left != None:
            return self.left.find(k)
        elif self.right != None:
            return self.right.find(k)
        else:
            return None

    def insertNode(self, node):
        """ insert it in the binary tree """
        l = self.left
        r = self.right
        if l == None:
           node.parent = self
           self.left = node
           return True
        elif r == None:
           node.parent = self
           self.right = node
           return True
        else:
           return False

    def insert( self, node ):
        if node.index < 4:
           self.insertNode( node )
        elif node.index > 3 and node.index < 8:
           nodesToTry = [ self.left, self.right ]
           for insertN in nodesToTry:
               if insertN.insertNode( node ):
                   break
        elif node.index > 7 and node.index < 16:
           l = self.left
           r = self.right
           nodesToTry = [ l.left, l.right, r.left, r.right ]
           for insertN in nodesToTry:
               if insertN.insertNode( node ):
                   break
                    
class BT(object):
    """A binary search tree."""
    def __init__(self, klass = BTNode):
        """Creates an empty BST.
            klass (optional): The class of the node in the BST. Default to 
                BSTNode.
        """
        self.root = None
        self.klass = klass
        self.lastIndex = 1
        
    def __str__(self):
        if self.root is None: return '<empty tree>'
        return str(self.root)

    def find(self, k):
        """Finds and returns the node with key k from the subtree rooted at this 
        node.
        
        Args:
            k: The key of the node we want to find.
        
        Returns:
            The node with key k or None if the tree is empty.
        """
        return self.root and self.root.find(k)
                
    def insert(self, k):
        """Inserts a node with key k into the subtree rooted at this node.
        
        Args:
            k: The key of the node to be inserted.
            
        Returns:
            The node inserted.
        """
        node = self.klass(None, k, index=self.lastIndex)
        self.lastIndex = self.lastIndex+1
        if self.root is None:
            # The root's parent is None.
            self.root = node
        else:
            self.root.insert(node)
        return node
            
    def delete(self, k):
        """Deletes and returns a node with key k if it exists from the BST.
        
        Args:
            k: The key of the node that we want to delete.
            
        Returns:
            The deleted node with key k.
        """
        node = self.find(k)
        if node is None:
            return None
        if node is self.root:
            pseudoroot = self.klass(None, 0)
            pseudoroot.left = self.root
            self.root.parent = pseudoroot
            deleted = self.root.delete()
            self.root = pseudoroot.left
            if self.root is not None:
                self.root.parent = None
            return deleted
        else:
            return node.delete()   
        
def test(args=None, BTtype=BT):
    import random, sys
    if not args:
        args = sys.argv[1:]
    if not args:
        print 'usage: %s <number-of-random-items | item item item ...>' % \
              sys.argv[0]
        sys.exit()
    elif len(args) == 1:
        items = (random.randrange(100) for i in xrange(int(args[0])))
    else:
        items = [int(i) for i in args]

    tree = BTtype()
    print tree
    for item in items:
        tree.insert(item)
        print
        print tree

if __name__ == '__main__': test()
