# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/description/?envType=daily-question&envId=2026-03-09
# 모든 길이가 limit 이상의 subarray 에는 0과 1이 포함되어야 한다 
# > 동일한 숫자가 limit 이상 나타날 수 없다

# zero 개만큼 0을 세우고, 1을 배치하기 > 1은 zero+1 개의 위치에 존재할 수 있음
# 전체 경우에서 초과하는 경우를 배제하기

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        ans = 0

        def combi(n: int, k: int, limit: int) -> int:
            '''
            n개의 수를 k 공간에 넣기. 각 공간에는 1부터 limit 개의 수가 존재 가능
            '''
            if k <= 0 or n < k:
                return 0

            res = 0
            prep = n - k # 하나씩 깔아둠
            
            for i in range(k + 1):
                # i = 0 > 전체, 홀수일 때는 빼고, 짝수일 때는 더해줘서 보정
                left = prep - i * limit
                if left < 0:
                    break
                
                # 경우의 수 = limit보다 초과해서 더 들어갈 수 i개 선택, 남은 수를 k 공간에 분배
                possible_outcome = math.comb(k, i) * math.comb(left + k - 1, k - 1)
                
                if i % 2 == 0:
                    res += possible_outcome
                else:
                    res -= possible_outcome

            return res % MOD

        for k in range(1, zero + 1):
            zeros_cases = combi(zero, k, limit)
            if zeros_cases == 0:
                continue

            ans += zeros_cases * combi(one, k-1, limit)
            ans += zeros_cases * combi(one, k, limit) * 2 # 010101 .. 101010 이라 *2
            ans += zeros_cases * combi(one, k+1, limit)

        return ans % MOD
