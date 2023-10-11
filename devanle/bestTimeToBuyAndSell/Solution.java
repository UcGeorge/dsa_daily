package devanle.bestTimeToBuyAndSell;

class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int buy=prices[0];
        int sell = prices[0];
        for(int i = 1; i<prices.length; i++){
            if(prices[i]<buy){
                buy = prices[i];
                sell = 0;
            }
            if(prices[i]>sell&&prices[i]>buy)
                sell = prices[i];
            profit = Math.max(profit, (sell-buy));
        }
        return profit;
    }
}
