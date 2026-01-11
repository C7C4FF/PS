# https://leetcode.com/problems/largest-rectangle-in-histogram/
# 스택에 저장 > 현재 높이가 스택에 저장된 것보다 낮다면 뽑아서 사이즈 갱신, 시작 인덱스를 수정

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_size = 0
        
        for i in range(len(heights)):
            start = i
            height = heights[i]

            while stack and stack[-1][1] > height:
                w, h = stack.pop()
                width = i - w
                max_size = max(max_size, width * h)
                start = w
                
            stack.append((start, height))

        for w, h in stack:
            max_size = max(max_size, (n - w) * h)

        return max_size
