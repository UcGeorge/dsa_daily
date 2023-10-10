package devanle.rotateArray;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public void rotate(int[] nums, int k) {
        Map<Integer, Integer> maps = new HashMap<>();
        for(int i = 0; i<nums.length; i++){
            int position=(i+k)%nums.length;
            maps.put(position, nums[i]);
        }
        for(int i = 0; i<nums.length; i++){
            nums[i] = maps.get(i);
        }
    }
}
