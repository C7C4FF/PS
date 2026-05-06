# https://leetcode.com/problems/rotating-the-box/description/?envType=daily-question&envId=2026-05-06
# 돌려서 어디까지 떨어질 수 있는지 파악하는 것보다
# 먼저 오른쪽으로 최대한 밀 수 있는 만큼 밀고 돌려도 됨

# zip(*grid) = 반시계 90도, zip(*grid[::-1]) = 시계 90도

# 가장 놓을 수 있는 끝 쪽을 생각하기. * 이 오면 맨 끝을 장애물 앞으로 최신화하기

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        
        for i in range(m):
            empty = n - 1
            for j in range(n-1, -1, -1):
                if boxGrid[i][j] == '#':
                    boxGrid[i][j] = '.'
                    boxGrid[i][empty] = '#'
                    empty -= 1
                elif boxGrid[i][j] == '*':
                    empty = j - 1
        

        rotated = [list(row) for row in zip(*boxGrid[::-1])]
        return rotated
        

        
'''
    [('#', '#', '#'),
     ('#', '#', '#'),
     ('#', '#', '*'),
     ('.', '*', '.'),
     ('#', '.', '*'),
     ('.', '.', '.')]

     [['#', '#', '#'],
      ['#', '#', '#'],
      ['#', '#', '*'],
      ['.', '*', '.'],
      ['#', '.', '*'],
      ['.', '.', '.']]
'''
