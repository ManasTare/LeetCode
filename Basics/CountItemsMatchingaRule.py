class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        ind = 2
        if ruleKey == "type":
            ind = 0
        elif ruleKey == "color":
            ind = 1
        for x in items:
            if ruleValue == x[ind] :
                count+=1
        return count
