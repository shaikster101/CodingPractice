'''
From: Leetcode
Difficulty: Easy
Description: Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
'''
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i] = A[i][::-1]
            for j in range(len(A[i])):
                if A[i][j] == 0:
                    A[i][j] = 1
                elif A[i][j] == 1:
                    A[i][j] = 0
        return A