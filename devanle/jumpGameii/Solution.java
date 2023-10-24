package devanle.jumpGameii;

class Solution {
    public int jump(int[] nums) {
        int result = 0;
        int left = 0;
        int right = 0;
        while(right<nums.length-1){
            int maxJump = 0;
            for(int i = left; i < right+1; i++){
                maxJump = Math.max(maxJump, i+nums[i]);
            }
            left = right+1;
            right = maxJump;
            result++;

        }
        return result;
    }
}
