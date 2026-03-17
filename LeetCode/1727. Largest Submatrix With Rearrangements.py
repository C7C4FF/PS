# https://leetcode.com/problems/largest-submatrix-with-rearrangements/?envType=daily-question&envId=2026-03-17

# 84번처럼 row 히스토그램이 아니라 반대로 column 히스토그램 쌓기
# 히스토그램 쌓기 > 내림차순 정렬
# 왼쪽에 있는 기둥은 항상 현재보다 높음 > 가로 = j+1, 세로 = sorted_lst[j] 가 성립함
# 가로가 길어지면서 세로가 점점 낮아져도, 내림차순 정렬이기에 그만큼의 높이는 있음

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        ans = 0
        lst = [0] * n

        for row in matrix:
            for i in range(n):
                if row[i] == 1:
                    lst[i] += 1
                else:
                    lst[i] = 0

            sorted_lst = sorted(lst, reverse=True)
        
            for j in range(n):
                if sorted_lst[j] == 0:
                    break
                else:
                    ans = max(ans, (j+1) * sorted_lst[j])

        return ans
