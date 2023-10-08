package devanle.majorityElement;

public class Solution {
    //first solution, very slow
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> maps = new HashMap<>();
        int currentMax = nums[0];
        for(int i : nums){
            maps.put(i, maps.getOrDefault(i, 0)+1);
            if(maps.get(i)>maps.get(currentMax))
                currentMax = i;
        }
        return currentMax;
    }
}
