# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/?envType=daily-question&envId=2026-02-27

# 총 연산 m: 홀수번 뒤집히는 0의 개수와 홀/짝이 같음

# m이 홀수일 때
# 0 > m번만큼 뒤집힐 수 있음, 1 > 최대 m-1 만큼 뒤집힐 수 있음
# (m * k) <= zeros * m + ones * (m-1)
# (m * k) <= (zeros + ones [n]) * m - ones
# m >= ones // (n-k)

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        ones = s.count('1')
        zeros = n - ones

        # 모두 1인 경우
        if zeros == 0:
            return 0

        # k가 s의 길이와 같고, 전부 0인 경우 > 1회 필요
        if n == k and zeros == n:
            return 1
        
        # .. 전부 0이 아닌 경우는 불가능
        if n == k and zeros != n:
            return -1

        # k가 짝수인데, 남은 0이 홀수이면 불가능
        if k % 2 == 0 and zeros % 2 != 0:
            return -1
        
        # m >= ones // (n-k)
        cnt = math.ceil(zeros / k)
        odd = max(cnt, math.ceil(ones / (n - k)))
        if odd % 2 == 0:
            odd += 1

        # m >= zeros // (n-k)
        even = max(cnt, math.ceil(zeros / (n - k)))
        if even % 2 != 0:
            even += 1

        
        if k % 2 == 0:
            return min(odd, even)
        else:
            return odd if zeros % 2 != 0 else even
