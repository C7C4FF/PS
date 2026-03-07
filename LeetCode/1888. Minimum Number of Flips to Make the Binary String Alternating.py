# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/?envType=daily-question&envId=2026-03-07
# 사이클 > 그대로 이어붙여서 슬라이딩 윈도우로 처리
# alternating 한 값을 만들어서 다르면 1, 같으면 0 으로 얼마나 차이나는지 확인
# 하나씩 뒤로 미루면서 최솟값 확인. 뒤로 미루는 것만으로 0 이 나온다면 타입1 연산으로만 가능하기에 0 반환

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        cycle_s = s + s
        n_cycle = len(cycle_s)

        zero = ("01" * (n + 1))[:2 * n]
        one = ("10" * (n + 1))[:2 * n]

        d_0 = [0 if cycle_s[i] == zero[i] else 1 for i in range(n_cycle)]
        d_1 = [0 if cycle_s[i] == one[i] else 1 for i in range(n_cycle)]
        sum_0 = sum(d_0[:n])
        sum_1 = sum(d_1[:n])
        min_d = n

        if sum_0 == 0 or sum_1 == 0:
            return 0

        for i in range(n, n_cycle):
            min_d = min(min_d, sum_0, sum_1)

            sum_0 += d_0[i] - d_0[i - n]
            sum_1 += d_1[i] - d_1[i - n]

            if min_d == 0:
                return 0

        return min_d

'''
# TLE ..

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        cycle_s = s + s
        n_cycle = len(cycle_s)

        zero = "0"
        one = "1"

        for i in range(1, n_cycle):
            if zero[-1] == "0":
                zero += "1"
                one += "0"
            else:
                zero += "0"
                one += "1"
        
        if s == one or s == zero:
            return 0

        binary_s = int(cycle_s, 2)
        binary_0, binary_1 = int(zero, 2), int(one, 2)
        mask = (1 << n) - 1

        diff_0 = binary_s ^ binary_0
        diff_1 = binary_s ^ binary_1
        min_dist = n

        for _ in range(n):
            dist_0 = (diff_0 & mask).bit_count()
            dist_1 = (diff_1 & mask).bit_count()

            min_dist = min(min_dist, dist_0, dist_1)

            diff_0 >>= 1
            diff_1 >>= 1
            
            if min_dist == 0:
                return 0
        
        return min_dist
'''
        
        
        
