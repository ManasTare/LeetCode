class Solution {
    public int[] getConcatenation(int[] nums) {
        int res[] =new int[nums.length*2];
        for(int i =0; i<2;i++){
            for(int j=0;j<nums.length;j++){
                if(i==1){
                    res[j+nums.length]=nums[j];}
                res[j]=nums[j];
            }
        }
        return res;
    }
}
