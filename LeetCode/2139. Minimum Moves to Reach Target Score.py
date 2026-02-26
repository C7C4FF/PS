# https://leetcode.com/problems/minimum-moves-to-reach-target-score/
# target 부터 1로 만들기. maxDoubles이 없으면 그 값만큼 계속 1씩 더해야 하니 절댓값 차만큼 더해주기

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0

        while target != 1:
            if maxDoubles > 0:
                if target % 2 == 0:
                    target //= 2
                    maxDoubles -= 1
                else:
                    target -= 1
            else:
                ans += abs(2 - target)
                target = 1
            
            ans += 1
        
        return ans
