class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = {}
        
        for index, value in enumerate(nums):
            if (target - value in dictionary):
                return [dictionary[target - value], index]
            dictionary[value] = index

