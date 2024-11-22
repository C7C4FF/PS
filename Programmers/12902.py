# https://school.programmers.co.kr/learn/courses/30/lessons/12902

def solution(n):
    if n % 2 != 0:
        return 0

    dp = [0] * (n + 1)
    dp[2] = 3
    if n > 2:
        dp[4] = 11

    for i in range(6, n + 1, 2):
        dp[i] = (4 * dp[i-2] - dp[i-4]) % 1000000007

    return dp[n]

# 2일 때는 3  3x1
# 4일 때는 11 3x(3x1) + 2
# 6일 때는 41 3 x (3 x (3x1) + 2) + 2 x (3x1) + 2
# 8일 때는 153 3 x (3 x (3 x (3x1) + 2) + 3x3) + 2 x (3x(3x1) + 2) + 2

# f(n) = 3 x f(n-2) + 2 x f(n-4) + 2 x f(n-6) + ... + 2
# 2f(n-4) + 2f(n-6) + ... + 2 = f(n-2) - f(n-4)
# f(n) = 3f(n-2) + f(n-2) - f(n-4) = 4f(n-2) - f(n-4)
