
'''
From Leetcode
Difficulty: Easy
Description: Given a 32-bit signed integer, reverse digits of an integer.
'''





class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if(x >= 2**31-1 or x <= -2**31):
            return 0
        
        answer = str(x)
        
        if x >= 0:
            answer = int(answer[::-1])
            if(answer >= 2**31-1 or answer <= -2**31):
                return 0
            return answer
        else:  
            revStrg = answer[1:][::-1]
            answer = int('-' + revStrg)
            if(answer >= 2**31-1 or answer <= -2**31):
                return 0
            return answer