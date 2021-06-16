class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #s.reverse() the simplest solution for python3
        
        length = len(s)
        for i in range(length//2):
            s[i], s[length-1-i] = s[length-1-i], s[i] 

