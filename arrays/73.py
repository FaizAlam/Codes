'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zeroes = [] #(i,j)
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    zeroes.append([i,j])
        
        for row,col in zeroes:
            for i in range(m):
                for j in range(n):
                    if j==col or i==row:
                        matrix[i][j]=0
        
        
        
