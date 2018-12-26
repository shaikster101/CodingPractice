'''
From: Leetcode
Difficulty: Easy
Description: Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
'''


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0):
            return False
        else:
            mirror = str(x)[::-1]
            if str(x) == mirror:
                return True
            else:
                return False