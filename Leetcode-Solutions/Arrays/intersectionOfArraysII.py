class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        sortI=sorted(nums1)
        sortII=sorted(nums2)
        i=0
        j=0
        ret=[]

        while i<len(nums1) and j<len(nums2):
            if sortI[i]<sortII[j]:
                i+=1
            elif sortII[j]<sortI[i]:
                j+=1
            else:
                ret.append(sortI[i])
                j+=1
                i+=1
        return ret
