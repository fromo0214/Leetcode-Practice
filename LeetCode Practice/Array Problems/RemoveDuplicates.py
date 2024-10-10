def removeDuplicates(nums):
    expected_num = []

    for i in range(len(nums)):
        if nums[i] in expected_num:
            continue
        expected_num.append(nums[i])
    k = len(expected_num)
    return k

print(removeDuplicates([1,1,2]))
        