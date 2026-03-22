# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/?envType=daily-question&envId=2026-03-22

# zip(*matrix) > 반시계 90도 회전 = Transpose 전치
# 시계빵향으로 회전하기 위해서는 뒤집어줘야 함

# 이중 리스트가 아니라, 도중에 튜플로 바뀌기 때문에 target 안의 row들도 튜플로 바꿔주기

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(len(target)):
            target[i] = tuple(target[i])
        
        for _ in range(4):
            mat = list(zip(*mat[::-1]))

            if mat == target:
                return True
        
        return False
