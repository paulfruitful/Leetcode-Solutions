class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        cash=[0]*len(nums)
        cash[0]=nums[0]

        if len(nums)>1:
            cash[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                cash[i]=max(cash[i-1],cash[i-2]+nums[i])
        return cash[len(nums)-1]
