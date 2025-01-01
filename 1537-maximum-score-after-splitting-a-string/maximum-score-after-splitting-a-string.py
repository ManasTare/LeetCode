class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for x in range(1,len(s)):
            res = max(res,(s[:x].count('0'))+(s[x:].count('1')))
        return res
        