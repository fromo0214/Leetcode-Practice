import java.util.*;
/**
 * ProductOfArrayExceptSelf
 * https://leetcode.com/problems/product-of-array-except-self/description/
 */
public class ProductOfArrayExceptSelf {
    static int[] solution(int[] nums){
        int[] res = new int[nums.length];

        res[0] = 1;

        for(int i = 1; i < nums.length; i++){
            res[i] = res[i - 1] * nums[i - 1];
        }
    
        int right = 1;
        
        //here we are multipying elements from the right and adding to the new array
        for(int i = nums.length - 1; i >= 0; i--){
            res[i] *= right;
            right *= nums[i];
        }

        // for(int i = 0; i < res.length; i++){
        //     System.out.print(res[i] + ", ");
        // }

        return res;

    }
    public static void main(String[] args) {
        int[] array = {1,2,3,4};
        solution(array);
        
    }
}
