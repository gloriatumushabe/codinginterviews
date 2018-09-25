
import unittest
class Tree:
    def __init__(self, val,  left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

    def isBalanced(self, root):
        if root is None:
            return True
        else:
            return self.isBalanced(root.right) and self.isBalanced(root.left) and abs(self.height(root.left) - self.height(root.right)) <= 1

    def height(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

class Test(unittest.TestCase):
    def test(self):
        tree = Tree(314, Tree(6, None, Tree(2, None, Tree(3))), Tree(6, Tree(2, Tree(3))))
        self.assertFalse(tree.isBalanced(tree))

if __name__ == '__main__':
    unittest.main()




