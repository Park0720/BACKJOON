import sys
input = sys.stdin.readline

h, w, box = map(int, input().strip().split())
height_list = {n : 0 for n in range(257)}

arr = []
for i in range(h):
    temp = list(map(int, input().strip().split()))
    arr.append(temp)
    for j in temp:
        height_list[j] += 1

height_list = list(height_list.items())

time_list = []
for i in range(257):
    lower = [(key, value) for key, value in height_list if key < i and value != 0]
    upper = [(key, value) for key, value in height_list if key > i and value != 0]
    time, block = 0, 0
    block += box

    for height, count in upper:
        time += 2 * (height-i) * count
        block += (height-i) * count
    for height, count in lower:
        time += (i-height) * count
        block -= (i-height) * count

    if block < 0:
        break
    time_list.append(time)

max_height_idx = [idx for idx, t in enumerate(time_list) if t == min(time_list)]
max_height = max(max_height_idx)
min_time = min(time_list)

print(min_time, max_height)