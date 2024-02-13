N, M = map(int, input().split())

N_list = [list(map(int, input().split())) for _ in range(N)]

M_list = [list(map(int, input().split())) for _ in range(N)]

answer_list = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        answer_list[i][j] = N_list[i][j] + M_list[i][j]
        print(answer_list[i][j], end=' ')
    print()
