class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = []
        for x in nums.copy():
            if x in seen:
                nums.remove(x)
            else:
                seen.append(x)
        return len(nums)
        