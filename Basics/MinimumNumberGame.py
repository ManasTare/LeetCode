class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        ind=0
        temp=0
        for x in nums:
            if ind > len(nums)-1:
                break
            temp=nums[ind]
            nums[ind]=nums[ind+1]
            nums[ind+1]=temp
            ind = ind + 2
        return nums
