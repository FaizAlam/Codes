'''
Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        pres = []
        pres.append(nums[0])
        for i,val in enumerate(nums[1:]):
            pres.append(pres[i]+val)
        '''
        
        n = len(nums)
        mapi = {}
        ans=0
        sum=0
        for i in range(n):
            sum+=nums[i]
            if sum==k:
                ans+=1
            
            if sum-k in mapi:
                ans += mapi[sum-k]
            
            mapi[sum] = mapi.get(sum,0)+1
        
        return ans

        