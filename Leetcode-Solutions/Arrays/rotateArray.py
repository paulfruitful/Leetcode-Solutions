class Solution(object):
    def rotate(self, nums, k):
           k = k % len(nums)

           temp = nums[-k:]
    
           for i in range(len(nums) - 1, k - 1, -1):
             nums[i] = nums[i - k]
    
   
           for i in range(k):
             nums[i] = temp[i]
