# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # ----------------
    # recursive method
    # ----------------
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSym(root.left, root.right)

    def isSym(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            return self.isSym(left.right, right.left) and self.isSym(left.left, right.right)
        return False

    # ----------------
    # iterative way
    # ----------------

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root.left, root.right)]

        while stack:
            left, right = stack.pop()

            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))

        return True
