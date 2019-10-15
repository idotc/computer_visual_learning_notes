"""
题目：给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
输入：
False
输出：
true
"""
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.lower()
    temp = []
    for char in s:
        if (char >= 'a' and char <= 'z') or char.isdigit():
            temp.append(char)
    if temp == temp[::-1]:
        return True
    else:
        return

s = input()
print(isPalindrome(s))
