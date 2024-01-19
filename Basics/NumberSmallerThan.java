class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int res[] = new int[nums.length];
        int opr=0;
        for(int i =0;i<nums.length;i++){
            for(int j=0;j<nums.length;j++){
                if(nums[i]>nums[j])
                    opr++;
            }
            res[i]=opr;
            opr=0;
        }
        return res;
    }
}
