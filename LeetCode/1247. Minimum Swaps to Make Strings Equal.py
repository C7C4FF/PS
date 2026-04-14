# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/description/
# xx yy > 1번 스왑, xy yx > 2번 스왑
# 4 6 이 나왔다면 1번 스왑하는 같은 모양으로 2개, 3개 가능 > 2 + 3 = 5
# 3 5 라면 1번 스왑하는 짝으로 1개, 2개 > 3 , 2번 스왑하는 짝으로 1개씩 해서 1 + 2 + 2 = 5

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        ans = 0
        n = len(s1)

        xy = 0
        yx = 0

        if n == 1:
            return 0 if s1 == s2 else -1
        
        for i in range(n):
            if s1[i] == 'x' and s2[i] == 'y':
                xy += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                yx += 1
        
        if (xy + yx) % 2 != 0:
            return -1

        q1, r1 = divmod(xy, 2)
        q2, r2 = divmod(yx, 2)

        ans = q1 + q2 + r1 + r2

        return ans
