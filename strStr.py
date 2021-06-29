# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        # return haystack.find(needle)

        # more non-python way

        for index in range(len(haystack) - len(needle) + 1):
            if haystack[index: index + len(needle)] == needle:
                return index
        return -1
