class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        prefixSample = ""

        for checkLength in range(1, len(strs[0])+1):
            sample = set(strs[index][:checkLength]
                         for index in range(len(strs)))
            print(sample)
            if len(sample) == 1:
                prefixSample = str(sample.pop())

        return prefixSample


'''
interesting solution i found on discussion board:
https://leetcode.com/problems/longest-common-prefix/discuss/6911/Simple-Python-solution

the use of zip() and asterisk explained in practice.py

    def longestCommonPrefix(self, strs):
       if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
            
'''
