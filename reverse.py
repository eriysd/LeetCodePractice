class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            value = -1 * int(str(x)[:0:-1])
        else:
            value =  int(str(x)[::-1])

        if value < 2**31-1 and value > -2**31:
            return value
        else:
            return 0