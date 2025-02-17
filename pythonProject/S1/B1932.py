import sys

input = sys.stdin.readline

n = int(input().strip())

triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().strip().split())))
    while len(triangle[_]) < n:
        triangle[_].append(0)

dp = [[0] * n for _ in range(n)]

dp[0][0] = triangle[0][0]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + triangle[i][0]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

print(max(dp[n-1]))