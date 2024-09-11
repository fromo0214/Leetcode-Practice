# Problem 1

# You are given an array A representing heights of students. All the students are asked to stand in rows. The students 
# arrive by one, sequentially (as their heights appear in A). For the i-th student, if there is a row in which all the 
# students are taller than A[i], the student will stand in one of such rows. If there is no such row, the student will 
# create a new row. Your task is to find the minimum number of rows created.

# Write a function that, given a non-empty array A containing N integers, denoting the heights of the students, returns
# the minimum number of rows created.


# For example, given A = [5, 4, 3, 6, 1], the function should return 2.

# Row1 = [5, 4, 3, 1]
# Row2 = [6]
# Since two rows are created, the function should return 2.
# Assume that:
# N is an integer within the range [1..1,000]
# each element of array A is an integer within the range [1..10,000]
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment

def solution(heights):
    # list representing the last student in each row
    end_heights = []

    def binary_search_leftmost(array, target):
        left, right = 0, len(array)

        while left < right:
            mid = (left + right) // 2

            # target is on the left side
            if array[mid] > target:
                right = mid
            else:# array[mid] < target, meaning the target is on the right side 
                left = mid + 1

        # returns the left index
        return left

    for height in heights:
        # represents the index in 'end_heights' where the current height can be placed 
        # holds the index where the current student's height can be inserted into the end heights list
        pos = binary_search_leftmost(end_heights, height)

        # in this condition it checks to see if the index is in range of the length of the list 
        # if true the student can fit into an existing row, and update the existing row 
        if pos < len(end_heights):
            # if a row exists, replace its "end height" with the current height
            end_heights[pos] = height
        else:
            end_heights.append(height)

    return len(end_heights)

# A = [5, 4, 3, 6, 1] 
# A2 = [5, 3, 4, 2 , 1]
# A3 = [5, 3, 4, 6, 2]
# print(solution(A))
# print(solution(A2))
# print(solution(A3))


# Problem 2 (Variation of "Partition Problem")

# There are some processes that need to be executed. Amount of a load that process causes on a server that runs it, 
# is being represented by a single integer. Total load caused on a server is the sum of the loads of all the processes 
# that run on that server. You have at your disposal two servers, on which mentioned processes can be run. Your goal is 
# to distribute given processes between those two servers in the way that, absolute difference of their loads will be minimized.



# Write a function that, given an array A of N integers, of which represents loads caused by successive processes, the 
# function should return the minimum absolute difference of server loads.



# For example, given array A such that:
#   A[0] = 1
#   A[1] = 2
#   A[2] = 3
#   A[3] = 4
#   A[4] = 5
# your function should return 1. We can distribute the processes with loads 1, 2, 4 to the first server and 3, 5 to 
# the second one, so that their total loads will be 7 and 8, respectively, and the difference of their loads will be equal to 1.

# Basically use the sum of the array and try to add up the elements so the difference between sum1 and sum2 is a very small difference and add up to total sum

# A = [1, 2, 3, 4, 5]
# s1, s2 = 7, 8
def solution2(A):
    total_sum = sum(A)
    
    # determine a target we are searching for 
    target = total_sum // 2

    # create a set that can store all the possible sums 
    possible_sums = set()
    # 0 gets added as a base case
    possible_sums.add(0)

    # iterate through the numbers in array
    for num in A:
        new_sums = set()
        # iterate through numbers in set
        for s in possible_sums:
            # add new possible sums by including the current element 
            new_sums.add(s + num)

        # update the possible sums set
        possible_sums.update(new_sums)

    # find the closest sum to the target whether it is less than or equal to the target by using the max function.
    closest_sum = max(s for s in possible_sums if s <= target)

    # calculate the total difference between the two server loads
    difference = abs(total_sum - 2 * closest_sum)

    

    return difference
    




    
A = [1,2 ,3 ,4 ,5]
A2 = [1,2,3,1]
A3 = [10, 20, 15, 5, 25]
A4 = [1, 5, 5, 11]

print(solution2(A3))




