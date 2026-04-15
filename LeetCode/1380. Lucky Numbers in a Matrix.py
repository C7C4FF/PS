# https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/
# 두 리스트의 공통된 값 찾기 > 교집합으로 찾을 수 있음

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        minimum = []
        maximum = []

        for lst in matrix:
            minimum.append(min(lst))
        
        for lst in list(zip(*matrix)):
            maximum.append(max(lst))
        
        return list(set(minimum) & set(maximum))
