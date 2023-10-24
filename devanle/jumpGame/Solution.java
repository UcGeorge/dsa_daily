package devanle.jumpGame;

class Solution {
    public boolean jumpGame(int[] nums) {
        int highestReach = 0;
        for(int i = 0; i<nums.length-1; i++){
            highestReach = Math.max(highestReach, i+nums[i]);
            if(highestReach >= nums.length-1)
                return true;
            if(nums[highestReach] == 0 && nums[i] ==0 && highestReach == i)
                return false;
        }
        return true;
    }
}
