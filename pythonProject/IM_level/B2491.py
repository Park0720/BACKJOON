N = int(input())

num_list = list(map(int, input().split()))

max_count = 1
min_count = 1

max_counts = []
min_counts = []

max_counts.append(max_count)
min_counts.append(min_count)

for i in range(N-1):
    if num_list[i+1] >= num_list[i]:
        max_count += 1

    elif num_list[i+1] < num_list[i]:
        max_counts.append(max_count)
        max_count = 1

    if num_list[i+1] <= num_list[i]:
        min_count += 1

    elif num_list[i+1] > num_list[i]:
        min_counts.append(min_count)
        min_count = 1

    if i == N - 2:
        max_counts.append(max_count)
        min_counts.append(min_count)

if max(max_counts) > max(min_counts):
    print(max(max_counts))
else:
    print(max(min_counts))