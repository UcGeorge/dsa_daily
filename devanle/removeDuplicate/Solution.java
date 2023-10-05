package devanle.removeDuplicate;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int removeDuplicates(int[] nums) {
        int index = 0;
        List<Integer> lists = new ArrayList<>();
        for(int i=0; i<nums.length; i++){
            if(!(lists.contains(nums[i]))){
                nums[index] = nums[i];
                lists.add(nums[index]);
                index++;
            }
        }
        return lists.size();
    }

    //best solution
    public int removeDuplicatesFasterSolution(int[] nums) {
        int index = 1;
        for(int i=1; i<nums.length; i++){
            if(nums[i] != nums[i-1]){
                nums[index] = nums[i];
                index++;
            }
        }
        return index;
    }
}
