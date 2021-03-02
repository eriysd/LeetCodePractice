class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        arrayLength = len(nums)
        unique = 0
        
        if(arrayLength == 0):
            return 0
        
        for index in range(1, arrayLength):
            if nums[index] != nums[unique]:
                unique = unique + 1
                nums[unique] = nums[index]
        
        return  unique + 1
         