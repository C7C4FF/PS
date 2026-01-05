# https://leetcode.com/problems/maximum-matrix-sum/?envType=daily-question&envId=2026-01-05

# 음수가 1개만 있으면, 양수로 전환 불가능
# 가장 절댓값이 낮은 수를 음수로 만들어서 반환하기

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        cnt = 0
        abs_sum = 0
        smallest = 10**5

        for i in range(n):
            for j in range(n):
                target = matrix[i][j]
                smallest = min(smallest, abs(matrix[i][j]))

                if target < 0:
                    cnt += 1
                abs_sum += abs(matrix[i][j])

        if cnt % 2 == 0:
            return abs_sum
        else:
            return abs_sum - (smallest * 2)


