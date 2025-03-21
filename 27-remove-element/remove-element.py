class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)

        for x in nums.copy():
            if x == val:
                k -= 1
                nums.remove(x)
                nums.append('_')

        return k

        