# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/description/
# ex) 1210
# 0 > 1번 등장, 1 > 2번 등장, 2> 1번 등장, 3 > 0 번 등장 = 1210 이므로 True
# ex) 030
# 0 > 2번 등장 1 > 0번 등장, 2 > 0번 등장 = 200 이므로 False

class Solution:
    def digitCount(self, num: str) -> bool:
        cnt = Counter(num)
        ans = ""

        for i in range(len(num)):
            ans += str(cnt[str(f'{i}')])
        
        return True if ans == num else False
