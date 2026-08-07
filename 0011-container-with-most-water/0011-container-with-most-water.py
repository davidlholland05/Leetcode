class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right =  len(height)-1
        out = 0

        while left < right:
            wall = min(height[left],height[right])
            out = max(out, (right-left) * wall)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return out