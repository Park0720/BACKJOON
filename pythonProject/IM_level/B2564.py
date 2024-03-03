width, height = map(int, input().split())

store = int(input())

position_list = [list(map(int, input().split())) for _ in range(store+1)]

answer = 0

for i in range(store):
    # 같은 위치에 있는 경우
    if position_list[i][0] == position_list[-1][0]:
        answer += abs(position_list[i][1] - position_list[-1][1])

    # 다른 위치에 있는 경우
    elif position_list[-1][0] == 1:
        # 위치가 서로 마주보고 있는 경우, 시계방향과 반시계방향 고려해서 짧은 거리 도출
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
