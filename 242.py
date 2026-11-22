class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = 0
        for i in t:
            if i in s:
                n += 1
        if n == len(t):
            return True
        return False
