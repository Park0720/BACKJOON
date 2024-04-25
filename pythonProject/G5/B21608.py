import sys

N = int(sys.stdin.readline())

students = [list(map(int, sys.stdin.readline().split())) for _ in range(N*N)]
already_seat = [[0] * N for _ in range(N)]
# 각 학생이 좋아하는 학생들만 담을 배열
check_list = [[] for _ in range(N*N)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for student in students:
    me = student[0]
    likes = student[1:]
    check_list[me-1] = likes
    # 앉을 수 있는 자리 리스트
    possible_seat = []
    for i in range(N):
        for j in range(N):
            # 해당 자리가 비어있으면
            if not already_seat[i][j]:
                # 조건 1번과 조건 2번 체크할 변수
                empty = 0
                like_friend = 0
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        # 4방향 탐색해서 옆자리가 빈 경우
                        if not already_seat[ni][nj]:
                            empty += 1
                        # 4방향 탐색해서 좋아하는 친구가 있는 경우
                        if already_seat[ni][nj] in likes:
                            like_friend += 1
                # 앉을 수 있는 자리 리스트에 각각 좋아하는 친구 수, 빈 자리 수, x좌표 y좌표 담기
                possible_seat.append((like_friend, empty, i, j))
    # 다 담은 후 조건 1, 2, 3의 순서대로 자리에 앉을 수 있도록 정렬
    possible_seat.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    _, _, a, b = possible_seat[0]
    already_seat[a][b] = me

answer = 0

# 만족도 조사
for i in range(N):
    for j in range(N):
        me = already_seat[i][j] - 1
        count = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                # 4방향 탐색해서 좋아하는 친구가 있으면 카운트 증가
                if already_seat[ni][nj] in check_list[me]:
                    count += 1
        if count:
            answer += 10 ** (count-1)

print(answer)