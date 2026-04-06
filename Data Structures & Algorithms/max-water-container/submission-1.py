class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i, h in enumerate(heights):
            if i != 0 and h <= heights[i - 1]:
                continue
            j = len(heights) - 1
            while j > i:
                if j != len(heights) - 1 and heights[j] <= heights[j + 1]:
                    j-=1
                w = j - i
                area = w * min(h, heights[j])
                if area > max_area:
                    max_area = area
                j-=1
        return max_area