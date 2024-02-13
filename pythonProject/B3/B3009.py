x_count = [0] * 1001
y_count = [0] * 1001
for i in range(3):
    x, y = map(int, input().split())
    x_count[x] += 1
    y_count[y] += 1

a, b = 0, 0
for i in range(1001):
    if x_count[i] == 1:
        a = i
    if y_count[i] == 1:
        b = i

print(a, b)