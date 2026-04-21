# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/?envType=daily-question&envId=2026-04-21
# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/solutions/8020715/beats-100-easy-basic-swap-and-dfs-by-m20-b7dg/?envType=daily-question&envId=2026-04-21
# Union-find 로 서로 바꿀 수 있는 인덱스의 그룹 만들기
# 해당 인덱스가 속한 그룹에 현재 있는 source[i] 모으기, 어떤 숫자가 들어있는지 Counter 로 딕셔너리로 만들기
# 일치한다면 > 가져왔다고 치고 수를 하나 줄이기. 일치히지 않는다면 만들 수 없으므로 해밍거리를 1 늘리기

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def unite(a, b):
            parent[find(a)] = find(b)
        
        for a, b in allowedSwaps:
            unite(a, b)

        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(source[i])
        groups = {root: Counter(vals) for root, vals in groups.items()}

        hamming_dist = 0
        for i in range(n):
            root = find(i)
            freq = groups[root]
            if freq[target[i]] > 0:
                freq[target[i]] -= 1
            else:
                hamming_dist += 1

        return hamming_dist
