//High Time Complexity needs improvement
class Solution {
    public int singleNumber(int[] nums) {
        int k =0;
        for(int i=0;i<nums.length;i++){
            int match = 0;
            for(int j=0;j<nums.length;j++){
                if(nums[i]==nums[j]){
                    match++;
                }
            }
            if(match==1){
                k=nums[i];
            }
        }
        return k;
    }
}
