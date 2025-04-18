class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i , x in enumerate(nums):
            if target - x in seen:
                return [i , nums.index(target-x)]
            seen.add(x)
        