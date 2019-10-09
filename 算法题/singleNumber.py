"""
题目：给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
输入: 2,2,1
输出: 1
"""

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = 0
    for num in nums:
        result ^= num
    return result

nums = list(map(int, input().split(',')))
print (singleNumber(nums))