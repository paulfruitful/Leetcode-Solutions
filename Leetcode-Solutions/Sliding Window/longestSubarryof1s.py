class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret=l=0
        zero=1
        for r in range(len(nums)):
            if not nums[r]:
                zero-=1
            while zero<0 and l<=r:
                if not nums[l]:
                    zero+=1
                l+=1
            ret=max(ret,r-l)
        return ret

                
