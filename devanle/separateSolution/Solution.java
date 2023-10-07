package devanle.separateSolution;

import javax.swing.*;
import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        separateDigits(new int[]{33, 2, 311111, 23, 44, 2, 3, 90});
    }
    public static int[] separateDigits(int[] nums) {
        List<Integer> chars = new ArrayList<>();
        for(int i : nums){
            int leth = (""+i).length();
            while(leth != 0){
                int power = (int) Math.pow(10, leth-1);
                int current = i/power;
                chars.add(current);
            }
        }
        System.out.println(chars);
        int[] theNums = new int[chars.size()];
        for(int i = 0; i<chars.size(); i++){
            theNums[i] = chars.get(i);
        }
        return theNums;
    }
}