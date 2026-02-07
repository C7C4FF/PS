# https://leetcode.com/problems/counting-bits/description/
# 어차피 0은 0, dp로 구하기
# i의 1의 개수는 제곱이 될 때마다 가능한 수가 1개씩 늘고, 그 뒤부터는 1씩 증가

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            
            ans[i] = ans[i - offset] + 1
        
        return ans
