class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        oldColor=image[sr][sc]

        if oldColor==color:
            return image
        def depthFirst(img,r,c):
            if r<0 or r>=len(img) or c<0 or c>=len(img[0]) or img[r][c]!=oldColor:
                return 
            img[r][c]=color
            depthFirst(img,r-1,c)
            depthFirst(img,r+1,c)
            depthFirst(img,r,c-1)
            depthFirst(img,r,c+1)
            
        
        depthFirst(image,sr,sc)
        return image
