# 완전제곱수인지 판별하기 math.isqrt(x) or int(x**0.5)**2

class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                target = a * a + b * b
                c = int(math.isqrt(target))

                if c * c == target and c <= n:
                    ans += 1
        return ans
