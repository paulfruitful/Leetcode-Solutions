
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        res=False
        for i in matrix:
            if target in i:
                res=True
        return res

