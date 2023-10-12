package devanle.bestTimeToBuyAndSellii;

class Solution {
    public int maxProfit(int[] prices) {
        int currentProfit = 0;
        int buy = Integer.MAX_VALUE;
        int sell = 0;
        for(int i = 0; i<=prices.length-2; i++){
            if(prices[i]<buy){
                buy = prices[i];
                sell = 0;
            }
            if(prices[i+1] < prices[i]){
                sell = prices[i];
                currentProfit+= (sell-buy);
                buy = Integer.MAX_VALUE;
            }if((i+1) == (prices.length-1) && sell == 0){
                sell = prices[i+1];
                currentProfit +=(sell-buy);
            }
        }
        return currentProfit;
    }
}