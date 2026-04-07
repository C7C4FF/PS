# https://leetcode.com/problems/minimum-moves-to-capture-the-queen/description/
# 퀸 - 룩 , 퀸 - 비숍 사이에 다른 기물이 존재하는지 확인하기
# 바로 잡을 수 있거나 2번 걸리거나. 둘 중 하나임

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        rook = (a, b, 'r')
        bishop = (c, d, 'b')
        queen = (e, f, 'q')

        if a == e:
            if not (c == a and min(b, f) < d < max(b, f)):
                return 1
                
        if b == f:
            if not (d == b and min(a, e) < c < max(a, e)):
                return 1

        if abs(c-e) == abs(d-f):
            if abs(c-a) == abs(d-b) and abs(e-a) == abs(f-b):
                if (abs(c-e) * abs(b-f)) == (abs(a-e) * abs(d-f)):
                    line = [rook, bishop, queen]
                    line.sort(key=lambda x:x[0])
                    
                    for i in range(3):
                        if line[i][2] == 'r' and (i == 0 or i == 2):
                            return 1
            else:
                return 1
        
        return 2

'''

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        rook = (a, b, 'r')
        bishop = (c, d, 'b')
        queen = (e, f, 'q')

        if a == e:
            if not (c == a and min(b, f) < d < max(b, f)): # 중앙에 비숍이 있는지 확인
                return 1
            else:
                return 2
        if b == f:
            if not (d == b and min(a, e) < c < max(a, e)):
                return 1
            else:
                return 2

        if abs(c-e) == abs(d-f):
            if abs(c-a) == abs(d-b) and abs(e-a) == abs(f-b): # 기울기 부호 확인하기
                if (abs(c-e) * abs(b-f)) == (abs(a-e) * abs(d-f)): # 전부 같은 기울기를 가지고 있다면
                    line = [rook, bishop, queen]
                    line.sort(key=lambda x:x[0])
                    if (line[0][2] == 'b' and line[-1][2] == 'q') or (line[0][2] == 'q' and line[-1][2] == 'b'): # 퀸가 비숍이 처음과 맨 끝이라면 중간에 룩이 들어가 있음
                       return 2 
                    else:
                        return 1
            else:
                return 1
        else:
            return 2

'''

        
