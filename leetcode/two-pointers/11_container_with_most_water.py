def maxArea(self, height: List[int]) -> int:
    max_area = 0
    l, r = 0, len(height) - 1

    while l < r:
        x = r-l
        y = min(height[l], height[r])
        area = x * y
        max_area = max(max_area, area)
        
        if height[l] > height[r]:
            r -= 1
        elif height[l] < height[r]: 
            l += 1
        else:
            l += 1
            r -= 1

    return max_area