# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode, floor=float("-inf"), ceiling=float("inf")) -> bool:
        if not root:
            return True
        if root.val <= floor or root.val >= ceiling:
            return False

        # BST has different upper limit and lower limit for left and right node
        # for left root becomes the next ceiling
        # for right root becomes the next floor
        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)
