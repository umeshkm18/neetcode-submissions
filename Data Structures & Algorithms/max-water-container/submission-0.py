class Solution:
    def maxArea(self, heights: List[int]):
        maxarea = 0
        l = 0
        r = len(heights)-1
        while l<r:
            currarea = min(heights[l], heights[r]) * (r - l)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
            maxarea = max(maxarea,currarea)
        
        return maxarea
