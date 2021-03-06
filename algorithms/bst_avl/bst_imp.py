class BSTNode(object):

    def __init__(self, parent, k):
        self.key = k
        self.parent = parent
        self.right = None
        self.left = None

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
        if k == self.key:
            return self
        elif k < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(k)
        
    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current
        
    def next_larger(self):
        if self.right is not None:
            return self.right.find_min()
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent

    def insert(self, node):
        if node is None:
            return
        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

    def delete(self):
        if self.right is None or self.left is None:
            if self is self.parent.left:
                self.parent.left = self.right or self.left
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            if self is self.parent.right:
                self.parent.right = self.right or self.left
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:
            s = self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()

    def print_node(self):
        if self is None:
            return
        else:
            if self.left is not None:
                self.left.print_node()
            print(self.key, end=" ")
            if self.right is not None:
                self.right.print_node()

class BST(object):

    def __init__(self, klass=BSTNode):
        self.root = None
        self.klass = klass

    def __str__(self):
        if self.root is None:
            return '<empty tree>'
        return str(self.root)
    
    def find(self, k):
        return self.root and self.root.find(k)

    def min(self):
        return self.root and self.root.find_min()
    
    def insert(self, k):
        node = BSTNode(None, k)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)

    def delete(self, k):
        node = self.find(k)
        if node is None:
            return None
        if node is self.root:
            pseudoroot = BSTNode(None, 0)
            pseudoroot.left = self.root
            self.root.parent = pseudoroot
            deleted = self.root.delete()
            self.root = pseudoroot.left
            if self.root is not None:
                self.root.parent = None
            return deleted
        else:
            return node.delete()

    def next_larger(self, k):
        node = self.find(k)
        return node and node.next_larger()

    def inorder(self):
        if self.root is None:
            print("<empty tree>")
        else:
            return self.root and self.root.print_node()
        print("\n")
            

bst = BST()

n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    bst.insert(arr[i])

print(bst)
print()

bst.inorder()