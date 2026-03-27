# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/description/?envType=daily-question&envId=2026-03-27

# 짝수 > 오른쪽으로 시프트, 홀수 > 왼쪽으로 시프트

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        
        shift = k % n # 이동할 칸 구하기

        for i in range(m):
            if i % 2 == 0:
                matrix[i] = mat[i][shift:] + mat[i][:shift]
            else:
                matrix[i] = mat[i][-shift:] + mat[i][:-shift]

        if matrix == mat:
            return True
        else:
            return False
