#incomplete!!! I got the hang of it but couldn't solve it...
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/

class Solution:
    def myAtoi(self, s: str) -> int:
        s.strip()
        isNegative = s.startswith('-')
        
        if s.startswith('-') or s.startswith('+'):
            s = s[1:]
        
        index = 0
        
        for elem in s:
            while(elem.isnum):
                index += 1
                
        value = int(s[:index])
        
        if value > 2**31-1:
            return 2**31-1
        elif value < -2**31:
            return -2**31
        else:
            return value
        