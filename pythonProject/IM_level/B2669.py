base_list = [[0] * 100 for _ in range(100)]

for i in range(1, 5):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            base_list[j][k] = 1

count = 0
for i in range(len(base_list)):
    for j in range(len(base_list[i])):
        if base_list[i][j] == 1:
            count += 1

print(count)