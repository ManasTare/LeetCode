class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        res = ""
        for x in words:
            res += res.join(x[0])
        if(res==s):
            return True 
