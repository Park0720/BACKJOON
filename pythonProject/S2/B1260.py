def dfs(start):
    visited[start] = 1
    print(start, end=' ')
    for w in adjl[start]:
        if visited[w] == 0:
            dfs(w)


def bfs(G, v, n):
    visited = [0] * (n + 1)
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        print(t, end=' ')
        for i in G[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1


N, M, V = map(int, input().split())
adjl = [[] for _ in range(N+1)]

for _ in range(1, M+1):
    start, end = map(int, input().split())
    adjl[start].append(end)
    adjl[end].append(start)

for _ in range(1, N+1):
    adjl[_].sort()

visited = [0] * (N+1)

dfs(V)
print()
bfs(adjl, V, N)