# https://leetcode.com/problems/max-points-on-a-line/description/

# 점들이 한 직선 위에 있다 > 기울기가 모두 같다: y2-y1 / x2-x1 = y3-y2 / x3-x2
# 직선, 대각선, 같은 위치의 점을 고려하기 > 근데 기울기가 같아도 그게 같은 직선이라는 보장은 없음 > y절편까지 구하기

# 기울기, y절편 구하기 > float의 부동소수점 문제로 오차가 발생함
# 기울기 검증 > y2-y1 * x3-x2 = y3-y2 * x2-x1 

# 기준을 잡고, 모든 점을 순회하면서 같은 직선 위에 있는지 체크함


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 1
        lines = set()

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]

                cnt = 0

                for k in range(len(points)):
                    x3, y3 = points[k]

                    if (y2-y1) * (x3-x2) == (y3-y2) * (x2-x1):
                        cnt += 1

                ans = max(ans, cnt)
        
        return ans

            
'''
            if (x2-x1) == 0:
                slope = float('inf')
                x_std = x1
                
                lines.add((slope, x_std))
            else:
                slope = (y2-y1) / (x2-x1)
                y_intercept = y2 - (slope * x2)
            
                lines.add((slope, y_intercept))
'''
