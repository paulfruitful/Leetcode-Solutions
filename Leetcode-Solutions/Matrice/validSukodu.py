class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        chars=[]
        for i in range(9):
          for j in range(9):
            node=board[i][j]
            if node != '.':
              chars+=[(i,node),(node,j),(i//3,j//3,node)]
        return len(chars)==len(set(chars))
