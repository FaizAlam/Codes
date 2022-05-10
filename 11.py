'''
Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1
        
        '''
        water = min(right most tallest ,left most tallest) * (index diff)
        
        '''
        max_water = 0
        
        while l<r:
            
            water = min(height[l],height[r])*(r-l)
            max_water = max(water,max_water)
            
            if height[l]>height[r]:
                r-=1
            
            elif height[l]==height[r]:
                if min(height[r-1],height[l])*(r-l-1)> min(height[r],height[l-1])*(r-l-1):
                    r-=1
                else:
                    l+=1
            
            else:
                l+=1
                
        return max_water
                
            
            
            