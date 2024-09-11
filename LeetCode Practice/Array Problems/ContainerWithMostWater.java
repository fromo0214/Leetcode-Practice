import java.util.*;
//https://www.youtube.com/watch?v=UuiTKBwPgAo
//https://leetcode.com/problems/container-with-most-water/description/

public class ContainerWithMostWater {
    
    public static int solution(int[] nums){
        int res = 0;
        int l = 0, r = nums.length - 1;

        while(l < r){
            int area = ((r - l) * Math.min(nums[l], nums[r]));
            res = Math.max(res, area);

            if(nums[l] < nums[r]){
                l++;
            }
            else{
                r--;
            }
    }
        return res;
}
    public static void main(String[] args) {
        int[] nums = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        System.out.println(solution(nums));
    }
}
