# https://leetcode.com/problems/jump-game-iv/description/?envType=daily-question&envId=2026-05-18

# editorial ..
# 양방향 BFS -> 항상 크기가 더 작은 집합을 기준으로 탐색
# 1. 값이 같은 다른 인덱스로 이동하기. -> 다 탐색한 이후에 그 값의 리스트를 비우기 (중복 탐색 방지)
# 2. 이전 인덱스 혹은 다음 인덱스로 이동

class Solution:
    def minJumps(self, arr) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = set([0])
        visited = {0, n-1}
        step = 0

        other = set([n-1])

        while curs:

            if len(curs) > len(other):
                curs, other = other, curs
            nex = set()

            
            for node in curs:
                for child in graph[arr[node]]:
                    if child in other:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        nex.add(child)

                graph[arr[node]].clear()

                for child in [node-1, node+1]:
                    if child in other:
                        return step + 1
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.add(child)

            curs = nex
            step += 1

        return -1
