def dfs(start):
    global count
    visited[start] = 1
    count += 1
    for w in adjl[start]:
        if visited[w] == 0:
            dfs(w)

N = int(input())
M = int(input())

adjl = [[] for _ in range(N+1)]

for _ in range(1, M+1):
    start, end = map(int, input().split())
    adjl[start].append(end)
    adjl[end].append(start)

for _ in range(1, N+1):
    adjl[_].sort()

visited = [0] * (N+1)
count = 0
dfs(1)
print(count-1)
