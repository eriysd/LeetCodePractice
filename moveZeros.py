class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        
        for index in range(len(nums)):
            if nums[index] is not 0:
                nums[index], nums[j] = nums[j], nums[index]
                j += 1
        
        ''' 
        #my first attemp, ran out of time
        
        npoped = 0
        index = 0
        
        while len(nums) > 0:
            for num in nums:
                if num is 0:
                    nums.pop(index)
                    npoped += 1
                index += 1
        
        for num in range(npoped):
            nums.append(0)
        
        return nums
        '''