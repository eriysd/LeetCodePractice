# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.assign(nums, 0, len(nums))

    def assign(self, nums, lower, upper):
        # this takes care of assigning only 1 side of the node when
        # tracing back up the recursion
        # because mid = 0 when starting to trace back

        if lower == upper:
            return None

        mid = (lower + upper) // 2

        ans = TreeNode(nums[mid])
        ans.left = self.assign(nums, lower, mid)
        ans.right = self.assign(nums, mid+1, upper)

        return ans
