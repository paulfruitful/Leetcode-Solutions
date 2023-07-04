class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        totalPairs=0
        
        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r]==[grid[j][c] for j in range(len(grid))]:
                    totalPairs+=1
        return totalPairs
