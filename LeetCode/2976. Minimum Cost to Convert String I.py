# https://leetcode.com/problems/minimum-cost-to-convert-string-i/?envType=daily-question&envId=2026-01-29
# 플루이드-마샬 알고리즘으로 .. 
# https://leetcode.com/problems/minimum-cost-to-convert-string-i/solutions/7532871/floyd-warshall-algorithm-by-jayantpatel0-h8hv/ 

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10**18
        dist = [[INF]*26 for _ in range(26)]

        for i in range(26):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            a = ord(o) - ord('a')
            b = ord(c) - ord('a')
            if w < dist[a][b]:
                dist[a][b] = w

        for k in range(26):
            for i in range(26):
                if dist[i][k] == INF:
                    continue
                dik = dist[i][k]
                for j in range(26):
                    if dist[k][j] == INF:
                        continue
                    nd = dik + dist[k][j]
                    if nd < dist[i][j]:
                        dist[i][j] = nd

        ans = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            a = ord(s) - ord('a')
            b = ord(t) - ord('a')
            if dist[a][b] == INF:
                return -1
            ans += dist[a][b]
        return ans
