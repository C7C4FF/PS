# https://leetcode.com/problems/robot-return-to-origin/description/?envType=daily-question&envId=2026-04-05
# UDLR 이 몇 번씩 들어갔는지 확인 > 계산

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt = Counter(moves)
        vertical, horizontal = 0, 0

        for k, v in cnt.items():
            if k == "L":
                horizontal -= v
            elif k == "R":
                horizontal += v
            elif k == "D":
                vertical -= v
            elif k == "U":
                vertical += v
        
        return True if (vertical == 0 and horizontal == 0) else False
