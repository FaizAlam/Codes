'''
Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

'''

class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        
        n = len(mat)
        m = len(mat[0])
        left,top,bottom,right = 0,0,n-1,m-1
        dir = 0
        res = []
        
        while left<=right and top<=bottom:
            
            if dir==0:  #left
                for i in range(left,right+1):
                    res.append(mat[top][i])
                top+=1
            
            elif dir==1:
                for i in range(top,bottom+1):
                    res.append(mat[i][right])
                right-=1
            
            elif dir==2:
                for i in range(right,left-1,-1):
                    res.append(mat[bottom][i])
                bottom-=1
            
            elif dir==3:
                for i in range(bottom,top-1,-1):
                    res.append(mat[i][left])
                left+=1
            
            dir = (dir+1)%4
        
        return res
                