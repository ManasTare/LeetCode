class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        var = 0
        for opr in operations:
            if(opr=="X++" or opr=="++X"):
                var = var + 1
            if(opr=="X--" or opr=="--X"):
                var = var - 1
        return var