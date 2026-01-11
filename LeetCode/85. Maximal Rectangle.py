# https://leetcode.com/problems/maximal-rectangle/?envType=daily-question&envId=2026-01-11
# 히스토그램으로 만들기... > 1을 만나면 누적하고, 0을 만나면 없애는 식으로
# 매 줄마다 최대가 될 수 있는 직사각형 넓이 구하기

# 현재 막대의 높이가 스택보다 더 낮으면, 시작점부터 오른쪽으로 넓힌 넓이 구하기
# 마지막에 스택에 남아있는 막대의 넓이 계산

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        lst = [0] * n
        ans = 0

        def get_rectangle(histogram: List[int]) -> int:
            stack = []
            max_size = 0
            
            for i in range(len(histogram)):
                start = i
                height = histogram[i]

                while stack and stack[-1][1] > height:
                    w, h = stack.pop()
                    width = i - w
                    max_size = max(max_size, width * h)
                    start = w

                stack.append((start, height))

            for w, h in stack:
                max_size = max(max_size, (n - w) * h)

            return max_size

        for row in matrix:
            for i in range(n):
                if row[i] == "1":
                    lst[i] += 1
                else:
                    lst[i] = 0
            
            ans = max(ans, get_rectangle(lst))
        
        return ans
