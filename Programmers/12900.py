# https://school.programmers.co.kr/learn/courses/30/lessons/12900
# 2일 때는 2 2x1
# 4일 때는 5 2x(2x1) + 1
# 6일 때는 13 2x(2(2x1) + 1) + 2x1 + 1

# 1일 때는 1
# 3일 때는 3
# 5일 때는 8

# f(n) = 2f(n-2) + f(n-4) + f(n-6) + ... + 1
# f(n-2) = 2f(n-4) + f(n-6) + ... + 1
# f(n-2) - f(n-4) = f(n-4) + f(n-6) + ... + 1
# f(n) = 2f(n-2) + f(n-2) - f(n-4) = 3f(n-2) - f(n-4)

def solution(n):
    dp = [0] * (n + 1)
    
    if n % 2 != 0:
        dp[1] = 1
        if n > 3:
            dp[3] = 3
        
        for i in range(5, n+1, 2):
            dp[i] = (3 * dp[i-2] - dp[i-4]) % 1000000007
            
    else:
        dp[2] = 2
        if n > 2:
            dp[4] = 5

        for i in range(6, n + 1, 2):
            dp[i] = (3 * dp[i-2] - dp[i-4]) % 1000000007

    return dp[n]

