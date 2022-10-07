class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxA = 0
        while (l<r):
            A = (r-l)*min(height[l],height[r])
            maxA = max(maxA,A)
            if (height[l]>height[r]):
                r-=1
            else:
                l+=1
            
        return maxA
        