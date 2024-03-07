N = int(input())
time_list = []
for i in range(N):
    start, end = map(int, input().split())
    time_list.append((start, end))

time_list.sort(key=lambda x: (x[1], x[0]))

count = 1
end_time = time_list[0][1]

for i in range(1, N):
    if end_time <= time_list[i][0]:
        end_time = time_list[i][1]
        count += 1

print(count)
