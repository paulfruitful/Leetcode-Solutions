
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        Set=set()
        ret=False
        for i in nums:
            if i in Set:
                ret=True
                break
            Set.add(i)
        return ret
#Another Solution Down Below


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums))!=len(nums):
            return True
        return False

