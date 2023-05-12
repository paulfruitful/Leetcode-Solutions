class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area=0
        l=0
        r=len(height)-1

        while l<r:
            width=r-l
            container_height=min(height[l],height[r])
            area=width*container_height
            max_area=max(max_area,area)
            
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area
