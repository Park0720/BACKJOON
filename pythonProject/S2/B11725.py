from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        now = queue.popleft()
        for v in adjl[now]:
            if visited[v]:
                continue
            answer[v] = now
            visited[v] = 1
            queue.append(v)


N = int(input())

adjl = [[0]] + [[] for _ in range(N)]
visited = [0] * (N+1)
answer = [0] * (N+1)


for i in range(1, N):
    input_list = list(map(int, input().split()))
    adjl[input_list[0]].append(input_list[1])
    adjl[input_list[1]].append(input_list[0])

bfs(1)

for i in range(2, N+1):
    print(answer[i])