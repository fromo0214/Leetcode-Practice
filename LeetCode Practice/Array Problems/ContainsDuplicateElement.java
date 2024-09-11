//https://leetcode.com/problems/contains-duplicate/description/

import java.util.*;

public class ContainsDuplicateElement {
    
    public static boolean solution(int[] arr){
        // 2 pointer method using sorting, O (n log n)
        // int l = 0;
        // int r = 1;
        // Arrays.sort(arr);

        // while(r < arr.length){
        //     if(arr[l] == arr[r]){
        //         return true;
        //     }
        //     else{
        //         l = r;
        //     }
        //     r += 1;
        // }

        //using a HashMap and HashSet is better, O(n)
        HashSet<Integer> set = new HashSet<>();
        for(int num : arr){
            if(set.contains(num)){
                return true;
            }
            set.add(num);
        }

        return false;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 1};
        System.out.println(solution(arr));
    }
}
