/**
 * MaximumSubArray
 * https://leetcode.com/problems/maximum-subarray/description/
 */
public class MaximumSubArray {

    static int solution(int[] nums){
        //here we have maxsub initialized as the first element in the array in this case -2
        int maxSub = nums[0];
        int currentSum = 0;

        for(int i = 0; i < nums.length; i++){
            if(currentSum < 0){
                currentSum = 0;
            }
            currentSum += nums[i];
            //the math.max compares the amount from maxsum and currentsum and whichever one is larger it initializes it to the larger value
            maxSub = Math.max(maxSub, currentSum);
        }

        return maxSub;
    }
    
    public static void main(String[] args) {
        int[] array = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println(solution(array));
    }
}