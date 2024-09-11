# # You begin with an array filled with N zeros and you want to obtain an array A. In one move, you can choose 
# # an arbitrary interval and increase all the elements within that interval by 1. For example, you can transform 
# # [0, 0, 0, 0, 0] into [0, 1, 1, 1, 0] in 
# # # a single move. However, you need three moves to obtain [1, 0, 1, 2, 2]. One possible sequence of 
# # moves is: [0, 0, 0, 0, 0] → [0, 0, 1, 1, 1] → [0, 0, 1, 2, 2] → [1, 0, 1, 2, 2],  where → denotes a single move.
# # What is the minimum number of moves needed to obtain A, starting from a zero-filled array?
# # Write a function: int solution(vector<int> &A); that, given an array A of length N, returns as an integer 
# # the minimum number of moves needed to transform a zero-filled array into A.
# #  Examples:
# # Given A = [2, 1, 3], the function should return 4. For example, the following sequence of moves leads to the 
# # solution: [0, 0, 0] → [1, 1, 1] → [2, 1, 1] → [2, 1, 2] → [2, 1, 3].
# # Given A = [2, 2, 0, 0, 1], the function should return 3. 
# # The following sequence of moves leads to the solution: [0, 0, 0, 0, 0] → [1, 1, 0, 0, 0] → [2, 2, 0, 0, 0] → [2, 2, 0, 0, 1].
# # Given A = [5, 4, 2, 4, 1], the function should return 7. One possible optimal sequence of moves is:
# #  [0, 0, 0, 0, 0] → [1, 1, 1, 1, 1] → [2, 2, 2, 2, 1] → [3, 3, 2, 2, 1] → [4, 4, 2, 2, 1] → [5, 4, 2, 2, 1] → 
# # [5, 4, 2, 3, 1] → [5, 4, 2, 4, 1].
# # Write an efficient algorithm for the following assumptions:
# # N is an integer within the range [1..100,000];
# # each element of array A is an integer within the range [0..1,000,000,000];
# # we guarantee that the answer will not exceed 1,000,000,000. 



# def solution(A):
#     moves = 0

#     # handle cases where array is empty 
#     if not A:
#         return moves
    
#     for i in range(len(A)):
#         if i == 0:
#             # for the first element just add its value 
#             moves += A[i]
#         else:
            
#             # adds the difference between current and previous elements, if positive 
#             moves += max(0, A[i] - A[i - 1])

# #     return moves

     


# # A = [2, 1,3]
# # A2 = [5, 4, 2, 4, 1]
# # A3= [2, 2, 0, 0, 1]
# # print(solution(A))
# # print(solution(A2))
# # print(solution(A3))


# # https://leetcode.com/problems/climbing-stairs/description/?envType=company&envId=google&favoriteSlug=google-thirty-days
# # def climbing_stairs(n):
# # #You are climbing a staircase. It takes n steps to reach the top.

# # #Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# #     one, two = 1 , 1


# #     for i in range(n - 1):
# #         # adding the 2 previous values 
# #         temp = one
# #         one = one + two
# #         two = temp


# #     return one




# # print(climbing_stairs(3))
# # https://leetcode.com/problems/add-two-numbers/?envType=company&envId=google&favoriteSlug=google-thirty-days
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# def addTwoNumbers(l1, l2):

#     dummy = ListNode()

#     curr = dummy 

#     # create a carry value in case we get a sum > 9
#     carry = 0


#     while l1 or l2 or carry:
#         v1 = l1.val if l1 else 0
#         v2 = l2.val if l2 else 0

#         # calculate new value
#         val = v1 + v2 + carry
#         carry = val // 10
#         val = val % 10
#         # we use mod to get the ones place 
#         curr.next = ListNode(val)

#         # update pointers
#         curr = curr.next
#         l1 = l1.next if l1 else None
#         l2 = l2.next if l2 else None


#     return dummy.next






        

#     # def reverse_linked_list(head):

    

    


#     # return 



# # head1 = ListNode(2)
# # head1.next = ListNode(4)
# # head1.next.next = ListNode(3)
# # head2 = ListNode(5)
# # head2.next = ListNode(6)
# # head2.next.next = ListNode(4)

# # print(addTwoNumbers(head1, head2))



# https://leetcode.com/problems/number-of-same-end-substrings/description/?envType=company&envId=google&favoriteSlug=google-thirty-days
# def sameEndSubstringCount(s, queries):
#     ans = []
#     count = 0
#     array = []
#     left, right = 0, 1

#     while right != len(s):
#         if s[left] not in array and s[left]:
#             array.append(s[left])
#             count += 1

#         if s[right] not in array and s[right]:
#             array.append[s[right]]
#             count += 1

#         left += 1
#         right += 1
#         ans.append(count)

#     return ans

# s = "abcd"
# queries = [[0,3]]

# print(sameEndSubstringCount(s, queries))
        
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=company&envId=google&favoriteSlug=google-thirty-days
# def lengthOfLongestSubstring(s):
#     sett = set()

#     if not s:
#         return 0

#     l = 0

#     max_len = 0
    
#     for r in range(len(s)):
#         while s[r] in sett:
#             sett.remove(s[l]) 
#             l += 1
#         sett.add(s[r])
#         max_len = max(max_len, len(sett))
    

#     return max_len



# s = "abcabcbb"
# s1 = "au"
# s2 = "aa"
# print(lengthOfLongestSubstring(s))
# print(lengthOfLongestSubstring(s1))
# print(lengthOfLongestSubstring(s2))

# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
from collections import defaultdict


def lengthOfLongestSubstringKDistinct(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    # using this you do not need to initialize the key and values to the dictionary check line 214
    dict = defaultdict(int)
    l = 0
    res = 0

    for r,c in enumerate(s):
        # you can just add the value of the frequency right away
        dict[c] += 1

        while len(dict) > k:
            dict[s[l]] -= 1

            if dict[s[l]] == 0:
                del dict[s[l]]
            l += 1
        
        res = max(res, r - l + 1)
      

    return res

s = "eceba"
k = 2
print(lengthOfLongestSubstringKDistinct(s, k))
        
        


    
            


    





     


    



