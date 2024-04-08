import sys


def dfs(x, y, count):
    global answer
    stack = []
    stack.append((x, count))
    visited[x] = 1
    now, count = stack.pop()
    if now == y:
        answer = count
    for w in adjl[now]:
        if visited[w]:
            continue
        visited[w] = 1
        dfs(w, y, count+1)


N = int(sys.stdin.readline())
per1, per2 = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

adjl = [[] for _ in range(N+1)]
visited = [0] * (N+1)
answer = -1

for _ in range(M):
    c, p = map(int, sys.stdin.readline().split())
    adjl[c].append(p)
    adjl[p].append(c)

dfs(per1, per2, 0)

print(answer)