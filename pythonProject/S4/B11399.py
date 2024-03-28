N = int(input())

time_list = list(map(int, input().split()))

time_list.sort()
_sum = 0
sum_list = [0] * N
for i in range(N):
    _sum += time_list[i]
    sum_list[i] = _sum + sum_list[i-1]

print(sum_list[-1])