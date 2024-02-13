N, M = map(int, input().split())
lst = [0] * N
for ball in range(N):
    lst[ball] = ball + 1
for ball in range(M):
    i, j = map(int, input().split())
    lst[i-1], lst[j-1] = lst[j-1], lst[i-1]
for i in lst:
    print(i, end=' ')