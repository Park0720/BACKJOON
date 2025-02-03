import sys

T = int(sys.stdin.readline().strip())

arr = []

for test_case in range(T):
    cnt = [0, 0]
    N = int(sys.stdin.readline().strip())
    arr.append(N)

n = max(arr)
dp0 = [0] * (n+2)
dp1 = [0] * (n+2)
dp0[0] = 1
dp1[1] = 1

for i in range(2, n+1):
    dp0[i] = dp0[i-1] + dp0[i-2]
    dp1[i] = dp1[i-1] + dp1[i-2]

for k in arr:
    print(dp0[k], dp1[k])
