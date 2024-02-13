base_list = [list(map(int, input().split())) for _ in range(9)]

_max = 0
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if base_list[i][j] >= _max:
            _max = base_list[i][j]
            x, y = i, j
print(_max)
print(x + 1, y + 1)