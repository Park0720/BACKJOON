import sys

input = sys.stdin.readline

T = int(input().strip())

dp = [0] * 101
dp[0], dp[1], dp[2], dp[3], dp[4], dp[5] = 0, 1, 1, 1, 2, 2

for _ in range(T):
    N = int(input().strip())
    if N > 5:
        for i in range(6, N+1):
            dp[i] = dp[i-5] + dp[i-1]

    print(dp[N])