class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''using dictionary
        dictionary = {}
        for index, element in enumerate(nums):
            if element in dictionary:
                return True
            dictionary[element] = index
        return False
        '''
        
        #another way of using set
        
        mySet = set(nums)
        if len(mySet) < len(nums):
            return True
        return False
    