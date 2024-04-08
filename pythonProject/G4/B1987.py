import sys


def dfs(sr, sc, count):
    global answer
    answer = max(answer, count)

    for k in range(4):
        nr = sr + dr[k]
        nc = sc + dc[k]
        if 0 <= nr < R and 0 <= nc < C and base_list[nr][nc] not in visited:
            visited.add(base_list[nr][nc])
            dfs(nr, nc, count+1)
            visited.remove(base_list[nr][nc])


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
R, C = map(int, sys.stdin.readline().split())
base_list = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
visited = set(base_list[0][0])
answer = 0

dfs(0, 0, 1)
print(answer)