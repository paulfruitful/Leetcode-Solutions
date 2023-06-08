class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        n1=set(nums1)
        n2=set(nums2)
        answer=[[i for i in n1 if i not in nums2],[i for i in n2 if i not in nums1]]
        return answer
