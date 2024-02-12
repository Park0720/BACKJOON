N = int(input())
base_list = [[0] * 100 for _ in range(100)]

for i in range(N):
    x1, y1 = map(int, input().split())
    for j in range(x1, x1+10):
        for k in range(y1, y1+10):
            base_list[j][k] = 1

count = 0
for i in range(100):
    for j in range(100):
        if base_list[i][j] == 1:
            count += 1

print(count)