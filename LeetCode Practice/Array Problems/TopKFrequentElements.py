# https://leetcode.com/problems/top-k-frequent-elements/
# https://www.youtube.com/watch?v=YPTqKIgVk-k&ab_channel=NeetCode

#Time O(n)
def topKFrequentElements(nums, k):

    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        # here we add the frequency using the key method, if it does not exist in the map
        # then add a default value of 0
        count[n] = count.get(n, 0) + 1

    # count is index 
    for num, countt in count.items():
        freq[countt].append(num)

    res = []

    for i in range(len(freq) - 1, -1,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

    

nums1 = [1,1,1,2,2,3]
nums2 = [1]
k1 = 1
k2 = 2
print(topKFrequentElements(nums1, k2))
print(topKFrequentElements(nums2, k1))