# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/?envType=daily-question&envId=2026-03-13

# 1x + 2x + 3x + 4x + ... + nx = x * (1 + 2 + 3 + ... + n)
# = x * n(n+1)/2

# 작업자가 한 번 작업할 때마다 1씩 깎음 > 산의 높이가 0이 될 때까지 최소힙 - 우선순위 큐를 활용
# 마지막으로 꺼낸 작업자의 종료시간이 최소 종료 시간임

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        heap = []
        for i in range(len(workerTimes)):
            # 종료시간, 작업에 걸리는 기본 시간, 사용 횟수
            heapq.heappush(heap, (workerTimes[i], workerTimes[i], 1))
        
        ans = 0

        while mountainHeight > 0:
            finish_time, base, cnt = heapq.heappop(heap)

            ans = finish_time
            mountainHeight -= 1

            if mountainHeight > 0:
                next_cnt = cnt + 1 # 사용횟수 1 늘리기
                next_finish_time = base * next_cnt * (next_cnt + 1) // 2 # 다음에 걸리는 시간은 등차수열로 계산
                heapq.heappush(heap, (next_finish_time, base, next_cnt))
            
        return ans
