class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        output=0
        def dfs(gr,row,c):
         if row < 0 or row >=len(gr) or c < 0 or c >= len(gr[0]) or gr[row][c] == 0:
              return 0
         gr[row][c]=0
         area=1 
         area+=dfs(gr,row+1,c)
         area+=dfs(gr,row-1,c)
         area+=dfs(gr,row,c+1)
         area+=dfs(gr,row,c-1)
         return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==1:
                    output=max(output,dfs(grid,i,j))
        return output
