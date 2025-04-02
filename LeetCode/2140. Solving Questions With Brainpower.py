# https://leetcode.com/problems/solving-questions-with-brainpower/?envType=daily-question&envId=2025-04-01
# 최대 포인트를 반환하라 했으니 완전탐색을 해야할 것 같음
# 한 문제를 풀면, brainpower 만큼 다음 문제들을 못 품

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        cache = {}

        def dfs(i):
            # i 가 범위를 넘어가면 0
            if i >= n:
                return 0

            # 이미 i를 진행했다면
            if i in cache:
                return cache[i]

            point, brainpower = questions[i]

            skip = dfs(i + 1)
            ongoing = point + dfs(i + brainpower + 1)

            cache[i] = max(skip, ongoing)

            return cache[i]

        return dfs(0)
