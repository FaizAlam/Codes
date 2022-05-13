'''
4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        
        res = []
        if n<4:
            return res
        
        nums = sorted(nums)
        
        for i in range(n):
            for j in range(i+1,n):
                target2 = target-nums[i]-nums[j]
                l,r=j+1,n-1
                
                while l<r:
                    two_sum = nums[l]+nums[r]

                    if two_sum>target2:
                        r-=1
                    elif two_sum<target2:
                        l+=1
                    
                    else:
                        quad = []
                        quad.append(nums[i])
                        quad.append(nums[j])
                        quad.append(nums[l])
                        quad.append(nums[r])
                        
                        if quad not in res:
                            res.append(quad)
                        
                        l+=1
                        r-=1
                        
        
        return res
                    
                        
            