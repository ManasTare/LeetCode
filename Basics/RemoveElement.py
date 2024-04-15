class Solution: 
    def removeElement(self, nums: List[int], val: int) -> int:
        res = len(nums)
        for x in nums.copy():
            if(x==val):
                res = res - 1
                nums.remove(x)
                nums.append("_")
        return(res)
                
        
