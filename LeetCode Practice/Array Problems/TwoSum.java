//https://leetcode.com/problems/two-sum/

import java.util.*;

public class TwoSum {
    public static int[] solution(int[] arr, int target){
        HashMap<Integer, Integer> map = new HashMap<>();
        int n = arr.length;
        for(int i = 0; i < n; i++){
            int difference = target - arr[i];

            if(map.containsKey(difference)){
                return new int[]{map.get(difference), i};
            }
            map.put(arr[i], i);
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        int arr[] = {2,1,5,3};
        int target = 4;


    }
}
