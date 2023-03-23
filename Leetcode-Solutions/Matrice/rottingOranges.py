class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        fresh = 0
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j,0))
        
        minutes = 0
        while queue:
            i,j,minutes = queue.pop(0)
            if i-1 >= 0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                fresh -= 1
                queue.append((i-1,j,minutes+1))
            if i+1 < len(grid) and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                fresh -= 1
                queue.append((i+1,j,minutes+1))
            if j-1 >= 0 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                fresh -= 1
                queue.append((i,j-1,minutes+1))
            if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                fresh -= 1
                queue.append((i,j+1,minutes+1))
        
        return -1 if fresh > 0 else minutes
