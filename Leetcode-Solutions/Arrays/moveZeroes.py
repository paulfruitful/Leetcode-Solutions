class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        try:
            index=nums.index(0)
        except ValueError:
            return
        no_zeros=[i for i in nums if i!=0]
        zeros=[0] * (len(nums)-len(no_zeros))
        nums[:]=no_zeros+zeros
      
