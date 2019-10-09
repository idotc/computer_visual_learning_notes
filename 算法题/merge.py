"""
题目:给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
输入：
3
1,2,3,0,0,0
3
2,5,6
输出：
[1,2,2,3,5,6]
"""

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    while m and n:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m = m - 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n = n - 1
    if n:
        nums1[:n] = nums2[:n]

m = int(input())
nums1 = list(map(int, input().split(',')))
n = int(input())
nums2 = list(map(int, input().split(',')))
merge(nums1, m, nums2, n)
print (nums1)