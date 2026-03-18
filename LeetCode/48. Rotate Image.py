# https://leetcode.com/problems/rotate-image/

# 90도 시계방향 회전 > 전치 후 각 행을 좌우반전
# 90도 반시계 방향 회전 > list(zip(*matrix))[::-1] 전치 후 위아래 뒤집기
# in-place 로 편집하기 위해서는 [:] 로 원래 가리키는 그 변수를 할당하기

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = list(zip(*matrix))

        for i in range(len(matrix)):
            target = matrix.pop(0)
            matrix.append(list(target)[::-1])
