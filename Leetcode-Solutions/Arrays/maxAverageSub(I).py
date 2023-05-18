class Solution(object):
    def findMaxAverage(self, nums, k):
        maxSum=sum(nums[:k])
        currSum=maxSum
        for i in range(k,len(nums)):
            currSum+=nums[i]-nums[i-k]

            if currSum>maxSum:
                maxSum=currSum
        return maxSum/float(k)
