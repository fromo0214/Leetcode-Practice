//TwoSum problem 
public class TwoPointersPractice 
{
    //Most basic way to solve two sum
    public static int twoSumSlow(int[] array, int targetValue){
        for(int i = 0;i < array.length; i++){
            for(int j = 0; j < array.length; j++){
                if(array[i] + array[j] == targetValue){
                    return 1;
                }
            }
        }
        return -1;
    }    

    //Two pointer method
    public static boolean twoSumFast(int[] array, int targetValue){
        int pointer1 = 0;
        int pointer2 = array.length - 1;

        while(pointer1 < pointer2){
        int sum = array[pointer1] + array[pointer2];
        if(sum == targetValue){
            return true;

        }else if (sum < targetValue){
            pointer1++;
        }else{
            pointer2--;
        }
        }
        return false;
    }

    //Two pointer method if the array is not in numerical order ex. {1,42,2,4,9,20,3}
    public static int[] twoSumBetter(int[] nums, int target){
        int pointer1= 0;
        int pointer2 = nums.length - 1;
        int[] ans = new int[2];

        
        while(pointer1 < pointer2){
        int sum = nums[pointer1] + nums[pointer2];
        if(sum == target){
            ans[0] = pointer1;
            ans[1] = pointer2;
            return ans;
        }else if(sum != target && pointer1 != pointer2 - 1){
            pointer2--;
            continue;
        }else{
            pointer1++;
            pointer2 = nums.length - 1;
        }

        }
        return ans;
    }

    public static void main(String[] args) {
        int [] array = {1,3,4,5,6,7,8,9,20};
        int[] nonOrderArr = {1,42,2,4,9,0,3};
        int targetValue = 43;

        System.out.println(twoSumBetter(nonOrderArr, targetValue));
        // System.out.println(twoSumFast(array, targetValue));
        // if(twoSumFast(array,targetValue)){
        //     System.out.println(targetValue +" is not a sum in the given array.");
        // }
        // else {
        //     System.out.println(targetValue + " is not a sum given in the array");
        // }


        // if(twoSumSlow(array,targetValue) == 1){
        //     System.out.println(targetValue +" is found in the array.");
        // }
        // else if(twoSumSlow(array, targetValue)==-1){
        //     System.out.println(targetValue + " is not found in the array");
        // }

    }
}
