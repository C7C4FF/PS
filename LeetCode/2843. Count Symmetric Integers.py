# https://leetcode.com/problems/count-symmetric-integers/?envType=daily-question&envId=2025-04-11

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = low
        ans = 0

        while cnt <= high:
            if 0 <= cnt <= 9:
                cnt = 10
                continue
            elif 100 <= cnt <= 999:
                cnt = 1000
                continue

            # 4자리 수의 경우에는 2개씩 잘라서 확인. 2자리 수의 경우에는 11의 배수만 가능
            if cnt // 10 >= 100:
                s = str(cnt)
                if sum(map(int, s[:2])) == sum(map(int, s[2:])):
                    ans += 1
            elif cnt // 10 >= 1:
                if cnt % 11 == 0:
                    ans += 1
            
            cnt += 1


        return ans
            
