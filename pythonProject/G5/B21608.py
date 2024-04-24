import sys

N = int(sys.stdin.readline())

students = [list(map(int, sys.stdin.readline().split())) for _ in range(N*N)]
already_seat = [[0] * N for _ in range(N)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for student in students:
    me = student[0]
    likes = student[1:]
    possible_seat = []
    for i in range(N):
        for j in range(N):
            if not already_seat[i][j]:
                empty = 0
                like_friend = 0
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        if not already_seat[ni][nj]:
                            empty += 1
                        if already_seat[ni][nj] in likes:
                            like_friend += 1
                possible_seat.append((like_friend, empty, i, j))
    possible_seat.sort(key=lambda k: (-k[0], -k[1], k[2], k[3]))
    _, _, x, y = possible_seat[0]
    already_seat[x][y] = me


for i in range(N):
    for j in range(N):
        count = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if already_seat[ni][nj] in likes:
                    count += 1
        print(count)