# https://leetcode.com/problems/jump-game-iii/description/?envType=daily-question&envId=2026-05-17

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        q = deque([start])

        while q:
            i = q.popleft()

            if i < 0 or i >= n:
                continue
            
            if i in visited:
                continue

            if arr[i] == 0:
                return True

            visited.add(i)
            q.append(i + arr[i])
            q.append(i - arr[i])

        return False
