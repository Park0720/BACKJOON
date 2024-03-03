K = int(input())

field = [[] for _ in range(6)]

for i in range(6):
    direction, width = map(int, input().split())
    field[i].append(direction)
    field[i].append(width)

field_area = 1
take = 1
max_width = 0
max_width_idx, max_height_idx = 0, 0
max_height = 0

for i in range(6):
    if field[i][0] == 1 or field[i][0] == 2:
       if max_width < field[i][1]:
            max_width = field[i][1]
            max_width_idx = i
    else:
        if max_height < field[i][1]:
            max_height = field[i][1]
            max_height_idx = i

field_area = max_width * max_height
sub_width = abs(field[(max_width_idx - 1) % 6][1] - field[(max_width_idx + 1) % 6][1])
sub_height = abs(field[(max_height_idx - 1) % 6][1] - field[(max_height_idx + 1) % 6][1])
take = sub_width * sub_height

print((field_area-take)*K)