# https://leetcode.com/problems/search-a-2d-matrix/

# Time Complexity O(m * n)
def searchMatrix(matrix, target):
    if not matrix:
        return False
    
    def binary_search(nums, target):

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2
            if nums[mid] == target:
                return True

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1


        return False
    
    for nums in matrix:
        if binary_search(nums, target):
            return True
        
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]    
matrix2 = [[1]]
target = 5
print(searchMatrix(matrix, target))
print(searchMatrix(matrix2, 1))





    