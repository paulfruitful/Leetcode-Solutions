class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sums=0
        maxSum=nums[0]
        for r in range(len(nums)):
            if sums<0:
                sums=0
            sums+=nums[r]
            maxSum=max(maxSum,sums)
        return maxSum
