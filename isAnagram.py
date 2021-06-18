class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # return sorted(s) == sorted(t) the easiest!
        
        d1, d2 = {}, {}
        
        for cha in s:
            d1[cha] = d1.get(cha, 0) + 1
        for cha in t:
            d2[cha] = d2.get(cha, 0) + 1
        return d1 == d2