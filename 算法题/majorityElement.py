"""
题目：给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
不满足时返回0
输入: 3,2,3
输出: 3
"""

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0: return 0
    count = 0
    temp = nums[0]
    for num in nums:
        if num == temp:
            count += 1
        else:
            count -= 1
            if count == 0:
                count = 1
                temp = num
    #校验是否存在众数，可能存在不满足条件的情况
    count = 0
    for num in nums:
        if num == temp:
            count += 1

    return temp if count > (n // 2) else 0

nums = list(map(int, input().split(',')))
print (majorityElement(nums))