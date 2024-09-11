//https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

public class BestTimeToBuyAndSellStock {
    public static int solution(int[] prices){
        int l = 0; //left is buying
        int r = 1; //right is selling
        int maxProfit = 0; 

        while(r < prices.length){
            //profitable ?
            if(prices[l] < prices[r]){
               int profit = prices[r] - prices[l];
               maxProfit = Math.max(maxProfit, profit);
            }
            else{
                l = r;
            }
            r += 1;
        }
        return maxProfit;
    }

    public static void main(String[] args) {
        int prices[] = {7, 1, 5, 3, 6 , 4};

        System.out.println(solution(prices));
    }
    
}
