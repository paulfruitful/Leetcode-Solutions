
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num_dict={}

        res=0

        for i in nums:
            num_dict[i]=num_dict.get(i,0)+1

        for i in nums:
            diff=k-i

            if diff==i:
                if num_dict[i]>=2:
                    num_dict[i]-=2
                    res+=1
            else:
                if num_dict.get(i,0)>0 and num_dict.get(diff,0)>0:
                    res+=1
                    num_dict[i]-=1
                    num_dict[diff]-=1
        return res


