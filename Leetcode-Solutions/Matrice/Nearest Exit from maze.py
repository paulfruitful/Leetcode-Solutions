class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        cols = len(maze[0])
        rows = len(maze)
        
        def traverser(r, c, currSteps):
            if (r >= rows or r < 0 or c >= cols or c < 0 or maze[r][c] == '+'):
                return float('inf')  
            if (r != entrance[0] or c != entrance[1]) and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                return currSteps 
            
            maze[r][c] = '+' 
            steps = [
                traverser(r + 1, c, currSteps + 1),
                traverser(r - 1, c, currSteps + 1),
                traverser(r, c + 1, currSteps + 1),
                traverser(r, c - 1, currSteps + 1)
            ]
            
            maze[r][c] = '.'
            
            return min(steps) 
        
        result = traverser(entrance[0], entrance[1], 0)
        
        return -1 if result == float('inf') else result
