# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/

# this probelm uses the Bredth First Search Algorithm
# deque is used to keep track of each level
# and more deque elements are appended as their parent is poppedleft
# Note, pop is assigned to node variable to be used after popped


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []

            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                ans.append(level)

        return ans
