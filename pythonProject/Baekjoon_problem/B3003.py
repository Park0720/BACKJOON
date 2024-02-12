chess_have_list = list(map(int, input().split()))
chess_list = [1, 1, 2, 2, 2, 8]

answer_list = []
for i in range(len(chess_list)):
    answer_list.append(chess_list[i] - chess_have_list[i])


print(*answer_list)