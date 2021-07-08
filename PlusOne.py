class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        length = len(digits)
        element = digits.pop() + 1
        if element//10 > 1:
            digits.append(digits.pop()+1)
            digits.append(element%10)
        else:
            digits.append(element)
        return digits
        '''

        # solution
        index = len(digits) - 1
        while index >= 0:
            if digits[index] is not 9:
                digits[index] += 1
                return digits
            else:
                digits[index] = 0
                index -= 1
        # when every term was 9
        return [1] + digits
