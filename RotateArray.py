class Solution:
    
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start = start + 1
            end = end - 1
            
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length
        
        self.reverse(nums, 0, length - 1)
        self.reverse(nums, k, length - 1)
        self.reverse(nums, 0, k - 1)