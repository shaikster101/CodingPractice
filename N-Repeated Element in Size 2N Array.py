'''
From: Leetcode
Difficulty: Easy
Description: In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
'''


class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        N = len(A)/2
        answer = 0
        for x in range(len(A)):
            temp = A.count(A[x])
            if(temp == N):
                answer = A[x]
                break
        return answer