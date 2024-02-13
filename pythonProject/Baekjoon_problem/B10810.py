N, M = map(int, input().split())
lst = [0] * N
for ball in range(M):
    i, j, k = map(int, input().split())
    for basket in range(i-1, j):
        lst[basket] = k
for i in lst:
    print(i, end=' ')