# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/?envType=daily-question&envId=2026-05-12
# 차이를 기준으로 정렬 > 최소 - 실제 소모: 내게 남아있는 최소 에너지.
# 에너지 요구량이 클 수록 먼저 해결하기 > 오름차순 정렬 후 역순으로
# max(이전까지 필요한 에너지 + 현재 작업 소모량, 현재 작업 최소 요구량)

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:x[1] - x[0])

        ans = 0
        for task in tasks:
            ans = max(ans + task[0], task[1])

        return ans
