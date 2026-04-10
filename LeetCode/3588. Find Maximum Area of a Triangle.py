# https://leetcode.com/problems/find-maximum-area-of-a-triangle/description/
# 정렬해두고 가장 작은 값, 가장 큰 값을 넣어서 비교하기
# 최소최대를 구하지 않고 전부 비교하면 TLE 

class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        ans = 0
        x_map = defaultdict(list)
        y_map = defaultdict(list)
        
        for x, y in coords:
            x_map[x].append(y)
            y_map[y].append(x)

        sorted_x = sorted(x_map.keys())
        sorted_y = sorted(y_map.keys())

        # x축에 평행
        for y, x_lst in y_map.items():
            if len(x_lst) < 2: continue
            
            distance = max(x_lst) - min(x_lst)
            
            height = max(abs(y - sorted_y[0]), abs(y - sorted_y[-1]))
            ans = max(ans, distance * height)

        # y축에 평행
        for x, y_lst in x_map.items():
            if len(y_lst) < 2: continue
            
            distance = max(y_lst) - min(y_lst)
            
            width = max(abs(x - sorted_x[0]), abs(x - sorted_x[-1]))
            ans = max(ans, distance * width)

        return ans if ans > 0 else -1
