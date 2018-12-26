'''
From: Leetcode
Difficulty: Easy
Description: You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
             Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
'''


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = list(J)
        stones = list(S)
        
        answer = 0
        for x in range(len(jewels)):
            for y in range(len(stones)):
                if jewels[x] in stones[y]:
                     answer += 1
        return answer