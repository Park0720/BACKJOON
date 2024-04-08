import sys
from collections import deque


def bfs(sr, sc, er, ec, count):
    queue = deque([(sr, sc, count)])
    chess_list[sr][sc] = 1

    while queue:
        cr, cc, count = queue.popleft()
        if (cr, cc) == (er, ec):
            return count
        for k in range(8):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0 <= nr < L and 0 <= nc < L and chess_list[nr][nc] == 0:
                chess_list[nr][nc] = chess_list[cr][cc] + 1
                queue.append((nr, nc, count + 1))


T = int(sys.stdin.readline())

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

for test_case in range(T):
    L = int(sys.stdin.readline())
    chess_list = [[0] * L for _ in range(L)]
    r1, c1 = map(int, sys.stdin.readline().split())
    r2, c2 = map(int, sys.stdin.readline().split())

    answer = bfs(r1, c1, r2, c2, 0)

    print(answer)