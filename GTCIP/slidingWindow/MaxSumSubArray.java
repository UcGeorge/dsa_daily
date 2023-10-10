package GTCIP.slidingWindow;

public class MaxSumSubArray {
    public static void main(String[] args) {
        System.out.println(solution(new int[]{2, 1, -1, 1, 3}, 3));
    }
    public static int solution(int[] nums, int k) {
        int max = 0;
        int startWindow = 0;
        int sum = 0;
        for (int endWindow = 0; endWindow < nums.length; endWindow++) {
            sum += nums[endWindow];
            if(endWindow>=(k-1)){
                max = Math.max(sum, max);
                sum -= nums[startWindow];
                startWindow++;
            }
        }
        return max;
    }
}
