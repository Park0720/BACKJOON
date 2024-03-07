import sys
input = sys.stdin.readline

N = int(input())

num_list = []
for _ in range(N):
    num_list.append(int(input()))

num_list.sort()

num_dict = {}
for i in num_list:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1

count = []
max_count = max(num_dict.values())

for i in num_dict:
    if max_count == num_dict[i]:
        count.append(i)


print(int(round(sum(num_list)/N, 0)))
print(num_list[N//2])
if len(count) > 1:
    print(count[1])
else:
    print(count[0])
print(abs(num_list[0] - num_list[-1]))