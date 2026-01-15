# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/description/?envType=daily-question&envId=2026-01-15
# 가장 넓이가 큰 정사각형 구하기
# bar를 n개 없애면 길이는 n+1이 됨

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def max_size(bars: List[int]) -> int:
            bars.sort()

            best = 1
            cur = 1

            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1: # 오름차순 정렬, 현재막대 == 이전 막대 + 1 이라면 연속 
                    cur += 1
                else:
                    cur = 1

                b_max = max(b_max, b_cur)
            
            return b_max
        
        h = max_size(hBars) # 세로선 없애는 갯수
        v = max_size(vBars) # 가로선 없애는 갯수

        side = min(h, v) + 1

        return side ** 2
