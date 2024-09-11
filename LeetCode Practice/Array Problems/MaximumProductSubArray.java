import java.util.*;
public class MaximumProductSubArray {

    static int solution(int[] nums){
        //currentprod = 2, index is at 0
        int result = Integer.MIN_VALUE;
        int curMax = 1, curMin = 1;

        for(int n : nums){
            if(n == 0){
                curMax = 1;
                curMin = 1;
                result = Math.max(result, 0);
                continue;
            }
           int temp = curMax;
           curMax = Math.max(Math.max(n, n * curMax), n * curMin);
           curMin = Math.min(Math.min(n, n * temp), n * curMin);
           result = Math.max(result, curMax);
        }
        return result;
    }
    public static void main(String[] args) {
        int[] array1 = {2, 3, -2, 4};
        int[] array2 = {-2, 0, -1};
        int[] array3 = {2, 1, -1, -4};
        int[] array4 = {-2};
        System.out.println(solution(array1));
        System.out.println(solution(array2));
        System.out.println(solution(array3));
        System.out.println(solution(array4));
        
    }
}
