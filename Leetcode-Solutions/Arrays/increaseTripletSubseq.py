
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min1=float('inf')
        min2=float('inf')
        i=0
        while i<len(nums):
            if nums[i]<=min1:
                min1=nums[i]
                i+=1
            elif nums[i]<=min2:
                min2=nums[i]
                i+=1
            else:
                return True
            
        return False

