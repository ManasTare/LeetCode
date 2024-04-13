# 142 / 147 testcases passed
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        for x in bank:
            if(x.count("1")==0):
                bank.remove(x)
        res = 0
        for i in range(len(bank)):
            if(i==(len(bank)-1)):
                break
            else:
                res = res + bank[i].count("1")*bank[i+1].count("1")   
        return res
        
