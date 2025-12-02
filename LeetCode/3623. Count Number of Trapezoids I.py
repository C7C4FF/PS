# 사다리꼴의 넓이 구하기
# y 좌표에 몇 개 있는지 구하고, 각 y에서 만들 수 있는 수평 변 개수 구하기 > 사다리꼴 만들기

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        ans = 0
        mod = 10**9 + 7
        total_sum = 0

        y_cnt = defaultdict(int)
        for x, y in points:
            y_cnt[y] += 1
        
        for cnt in y_cnt.values():
            edge = cnt * (cnt - 1) // 2
            ans = (ans + edge * total_sum) % mod
            total_sum = (total_sum + edge) % mod

        return ans
'''
TLE
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        ans = 0
        mod = 10**9 + 7

        y_cnt = defaultdict(int)
        for x, y in points:
            y_cnt[y] += 1
        
        sides = []
        for cnt in y_cnt.values():
            if cnt >= 2:
                side = cnt * (cnt - 1) // 2
                sides.append(side)
        
        n = len(sides)
        for i in range(n):
            for j in range(i + 1, n):
                ans = (ans + sides[i] * sides[j]) % mod

        return ans
'''
