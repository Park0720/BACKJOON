import sys
sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline


def dfs(start):
    global order_count
    visited[start] = True
    order[start] = order_count  # 현재 노드의 방문 순서 저장
    order_count += 1  # 다음 노드를 위해 순서 1 증가
    for w in adjl[start]:
        if not visited[w]:
            dfs(w)


N, M, V = map(int, input().split())

adjl = [[] for _ in range(N+1)]
# 방문 순서를 저장할 배열 추가
order = [0] * (N+1)
order_count = 1  # 방문 순서 카운트를 위한 변수


for _ in range(M):
    start, end = map(int, input().split())
    adjl[start].append(end)
    adjl[end].append(start)

for i in range(1, N+1):
    adjl[i].sort()

visited = [False] * (N+1)

dfs(V)

# 모든 노드의 방문 순서 출력
for i in range(1, N+1):
    print(order[i])
