def twoSum(nums, target):

    
    dict = {}

    for i in range(len(nums)):
        difference = target - nums[i]
        print(difference)
        if difference in dict:
            return [dict.get(target - nums[i]), i] 
        else:
            dict[nums[i]] = i
    return []

A = [2,7,11,15]

print(twoSum(A, 9))

def max_product_subarray(array):
    currSum = 0
    maxSum = array[0]

    for i in range(len(array)):
        if array[i] == 0:
            currSum = 0

        if array[i] < 0 and currSum < 0:
            currSum *= array[i]

        currSum*=array[i]
        maxSum = max(maxSum,currSum)

    return maxSum
        
A = [2, 3, -2, 4]
print(max_product_subarray(A))
