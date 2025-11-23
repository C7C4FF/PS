# https://leetcode.com/problems/maximum-average-pass-ratio/?envType=daily-question&envId=2025-09-01

# [pass, total], extraStudents => 어디가도 무조건 통과
# extraStudents: 델타 (학생을 넣었을 때 변화) 가 가장 큰 쪽으로 넣는 게 좋음
# 소수점 5번째 자리까지만 출력

# Fraction 으로 분자 분모를 살리고 계산하면 TLE ..

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []

        for p, t in classes:
            delta = (t - p) / (t * (t + 1))
            heapq.heappush(heap, (-delta, p, t))

        for _ in range(extraStudents):
            d, p, t = heapq.heappop(heap)
            if d == 0.0: # 개선할 수 없다면
                heappush(heap, (d, p, t))
                break
            p += 1
            t += 1
            new_delta = (t - p) / (t * (t + 1))
            heappush(heap, (-new_delta, p, t))

        # 최종 평균 (정확 계산 뒤 float 변환)
        total = 0.0
        for _, p, t in heap:
            total += p / t
        return total / len(classes)
