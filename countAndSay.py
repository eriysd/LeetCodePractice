# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/
import itertools


class Solution:
    def countAndSay(self, n: int) -> str:

        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit for digit,
                        group in itertools.groupby(s))
        return s
