# LLL.. (R/S) OOOOOOO (L/S).. RRR
# 양 끝에 있는 L과 R들은 충돌하지 않음
# lstrip, rstrip ..  자르고 안에 S를 빼서 카운팅

class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        n = len(directions)

        left = 0
        while left < n and directions[left] == 'L':
            left += 1
        
        right = n - 1
        while right >= 0 and directions[right] == 'R':
            right -= 1

        for i in range(left, right+1):
            if directions[i] != 'S':
                ans += 1
        
        return ans
