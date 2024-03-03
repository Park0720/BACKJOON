width, height = map(int, input().split())

store = int(input())

position_list = [list(map(int, input().split())) for _ in range(store+1)]

answer = 0

for i in range(store):
    if position_list[i][0] == position_list[-1][0]:
        answer += abs(position_list[i][1] - position_list[-1][1])

    elif position_list[-1][0] == 1:
        if position_list[i][0] == 2:
            answer += min(height + (width - position_list[-1][1]) + (width - position_list[i][1]), height + position_list[-1][1] + position_list[i][1])

        elif position_list[i][0] == 3:
            answer += position_list[i][1] + position_list[-1][1]

        elif position_list[i][0] == 4:
            answer += position_list[i][1] + (width - position_list[-1][1])

    elif position_list[-1][0] == 2:
        if position_list[i][0] == 1:
            answer += min(height + (width - position_list[-1][1]) + (width - position_list[i][1]), height + position_list[-1][1] + position_list[i][1])

        elif position_list[i][0] == 3:
            answer += (height - position_list[i][1]) + position_list[-1][1]

        elif position_list[i][0] == 4:
            answer += (height - position_list[i][1]) + (width - position_list[-1][1])

    elif position_list[-1][0] == 3:
        if position_list[i][0] == 4:
            answer += min((height - position_list[-1][1]) + (height - position_list[i][1]) + width, position_list[-1][1] + position_list[i][1] + width)

        elif position_list[i][0] == 1:
            answer += position_list[-1][1] + position_list[i][1]

        elif position_list[i][0] == 2:
            answer += (height - position_list[-1][1]) + position_list[i][1]

    elif position_list[-1][0] == 4:
        if position_list[i][0] == 3:
            answer += min((height - position_list[-1][1]) + (height - position_list[i][1]) + width, position_list[-1][1] + position_list[i][1] + width)

        elif position_list[i][0] == 1:
            answer += position_list[-1][1] + (width - position_list[i][1])

        elif position_list[i][0] == 2:
            answer += (width - position_list[i][1]) + (height - position_list[-1][1])

print(answer)
