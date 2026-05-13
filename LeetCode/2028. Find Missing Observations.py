# https://leetcode.com/problems/find-missing-observations/description/
# 주사위의 눈이 1~6 사이어야 함. 눈이 6인데 나머지가 있으면 눈이 6을 초과하기 때문에 [] 반환

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)

        total_number = m + n

        total = mean * total_number
        shortage = total - sum(rolls)

        dice, res = divmod(shortage, n)

        if dice < 1 or dice > 6 or (dice == 6 and res > 0):
            return []
        else:
            ans = [dice] * n
            for i in range(res):
                ans[i] += 1
        
        return ans
