class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        m = 0
        n = 0
        while  m < len(word1) and n < len(word2):
            res += word1[m]
            res += word2[n]

            m += 1
            n += 1

        if m < len(word1):
            res += word1[m:]

        if n < len(word2):
            res += word2[n:]

        
        return res
        