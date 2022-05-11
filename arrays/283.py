'''
Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0 or len(nums)==1:
            return nums
        
        l,r=0,0
        n = len(nums)
        while(r<n):
            if nums[r]==0:
                r+=1
            else:
                nums[r],nums[l]=nums[l],nums[r]
                l+=1
                r+=1
        
                
        