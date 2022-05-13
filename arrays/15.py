'''
3 sum 

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        if n<3:
            return ans
        
        nums = sorted(nums)
        for i in range(n-2):
            l = i+1
            r = n-1
            
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                
                if total==0:
                    if ([nums[i],nums[l],nums[r]]) not in ans:
                        ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                
                elif total>0:
                    r-=1
                
                else:
                    l+=1
        return ans
        
        