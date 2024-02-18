C, R = map(int, input().split())

K = int(input())

if C * R < K:
    print(0)

arr = [[0] * R for _ in range(C)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

count = 1

i = 0
j = 0
k = 0
while count <= C*R:
    arr[i][j] = count
    count += 1

    if not (0 <= i + di[k] < C and 0 <= j + dj[k] < R):
        k += 1

    elif arr[i+di[k]][j+dj[k]] != 0:
        k += 1

    if k > 3:
        k = 0

    i += di[k]
    j += dj[k]

for i in range(C):
    for j in range(R):
        if arr[i][j] == K:
            print(i+1, j+1)