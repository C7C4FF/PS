# https://leetcode.com/problems/separate-squares-i/?envType=daily-question&envId=2026-01-13

# 이분탐색으로 구하기...
# float으로 이분탐색을 하는 경우에는 반복횟수를 정해주거나, 두 합의 차가 극소하다는 것으로 판단하기
# while abs(lo - hi) >= eps (eps = 1e-5)

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total = 0
        n = len(squares)
        min_y, max_y = 10**9 + 1, -1

        for i in range(n):
            x, y, s = squares[i][0], squares[i][1], squares[i][2]

            min_y = min(min_y, y)
            max_y = max(max_y, y + s)
            total += s ** 2

        def get_area(line) -> int:
            # 기준선보다 아래에 있는 도형들의 넓이 구하는 함수
            area = 0

            for x, y, s in squares:
                h = line - y
                if h <= 0: # 정사각형이 기준선보다 아래
                    pass # area += 0
                elif h >= s: # 정사각형이 기준선보다 위
                    area += s * s
                else: # 정사각형 일부 포함 (높이 h x 가로 s)
                    area += h * s
            
            return area 

        for i in range(60):
            mid = (min_y + max_y) / 2
            if get_area(mid) >= total / 2:
                max_y = mid
            else:
                min_y = mid
            
        return max_y
