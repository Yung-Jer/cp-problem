class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []
        res = 0
        
        for i, v in enumerate(height):
            while stack and v > height[stack[-1]]:
                mid_idx = stack.pop()
                if not stack:
                    break
                left_idx = stack[-1]
                right_idx = i
                if height[mid_idx] == height[left_idx]:
                    continue
                height_val = min(height[right_idx], height[left_idx]) - height[mid_idx]
                res += height_val * (right_idx - left_idx - 1)
            stack.append(i)
        return res