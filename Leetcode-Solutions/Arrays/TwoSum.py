class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        differ={}
        for i in range(len(nums)):
            if target-nums[i] in differ:
                return [differ[target-nums[i]],i]
            differ[nums[i]]=i
        return []
