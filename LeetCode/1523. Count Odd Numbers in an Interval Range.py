# low ~ high 사이의 수 n = high - low
# n개의 수와 시작이 짝수인지 판별하기

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = high - low
        if low % 2 == 0 and n % 2 == 0:
            return n // 2
        else:
            return n // 2 + 1
