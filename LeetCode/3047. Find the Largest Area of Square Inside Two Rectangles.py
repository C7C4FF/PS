# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/description/
# left < right and bottom < top 폭과 높이가 전부 양수여야만 사각형이 나올 수 있음

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        side = 0
        n = len(bottomLeft)

        for i in range(n):
            for j in range(i+1, n):
                left = max(bottomLeft[i][0], bottomLeft[j][0])
                right = min(topRight[i][0], topRight[j][0])
                bottom = max(bottomLeft[i][1], bottomLeft[j][1])
                top = min(topRight[i][1], topRight[j][1])

                if left < right and bottom < top:
                    s = min(right - left, top - bottom)
                    side = max(side, s)

        return side * side
