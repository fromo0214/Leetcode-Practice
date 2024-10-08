package Sorting_Algorithms;

/*  Merge sort = recursively divide array in 2, sort, recombine
 * run-time complexity = O(n log n)
 * Space complexity = O(n)
 */
public class MergeSortTest {
    public static void main(String[] args) {
        int array[] = {3,7,8,5,4,2,6,1,9};

        mergeSort(array);

        for(int i = 0; i < array.length; i++){
            System.out.print(array[i] + " ");
        }

    }

    private static void mergeSort(int[] array) {
        int length = array.length;
        //if length is 1 the array no longer needs to be divided 
        if(length <= 1){ //base case
            return;
        }
        int middle = length / 2;
        int[] leftArray = new int[middle];
        int[] rightArray = new int[length - middle];

        int i = 0; //left array 
        int j = 0; //right array

        for(; i < length; i++){
            if( i < middle){
                leftArray[i] = array[i];
            }else{
                rightArray[j] = array[i];
                j++;
            }
        }
        mergeSort(leftArray);
        mergeSort(rightArray);
        merge(leftArray, rightArray, array);
    }

    //O(n1+n2) time because we are merging 2 sorted arrays
    private static void merge(int[] leftArray, int[] rightArray, int[] array){
        int leftSize = array.length / 2;
        int rightSize = array.length - leftSize;
        int i = 0, l = 0, r =0; //indices

        //check the conditions for merging
        while(l < leftSize && r < rightSize){
            if(leftArray[l] < rightArray[r]){
                array[i] = leftArray[l];
                i++;
                l++;
            }
            else{
                array[i] = rightArray[r];
                i++;
                r++;
            }
        }
        while(l < leftSize){
            array[i] = leftArray[l];
            i++;
            l++;
        }
        while(r < rightSize){
            array[i] = rightArray[r];
            i++;
            r++;
        }
    }
}
