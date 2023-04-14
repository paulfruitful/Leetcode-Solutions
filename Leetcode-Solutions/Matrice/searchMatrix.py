
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def dfs(r,c,matrix,target):
           if r>(len(matrix)-1) or c>(len(matrix[0])-1):
               return False
           if matrix[r][c]==target:
               return True
           return dfs(r+1,c,matrix,target) or dfs(r,c+1,matrix,target)
        return dfs(0,0,matrix,target)
