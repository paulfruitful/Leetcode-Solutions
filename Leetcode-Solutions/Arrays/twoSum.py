class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        right=len(numbers)-1
        while left<right:
            sum=numbers[left]+numbers[right]
            if sum==target:
                return [left+1,right+1]
            elif target>sum:
                left+=1
            else:
                right-=1
#Or
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
       
