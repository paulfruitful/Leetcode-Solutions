class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c!=(len(mat)*len(mat[0])):
            return mat

        flat=[]
        mat2=[]
        for i in mat:
            for j in i:
                flat.append(j)
        for i in range(r):
            mat2.append(flat[i*c:(i*c)+c])
        return mat2

        
