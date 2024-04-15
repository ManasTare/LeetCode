class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.split(" ")
        for x in range(len(res)):
            if(res[-1]==''):
                res.pop()
        return(len(str(res[-1])))
