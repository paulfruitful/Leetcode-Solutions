class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        zero,l=0,0
        for r,n in enumerate(nums):
            zero+=n==0
            if zero > k:
                zero-=nums[l]==0
                
                l+=1
        return r-l+1
