M = int(input())
N = int(input())

num_list = []
for i in range(M, N+1):
    num_div_list = []
    for j in range(1, i + 1):
        if i % j == 0:
            num_div_list.append(i)
    if len(num_div_list) == 2:
        num_list.append(i)


if num_list:
    print(sum(num_list))
    print(num_list[0])
else:
    print(-1)