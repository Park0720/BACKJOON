num_list = list(map(int, input().split()))

_sum = 0
for i in range(len(num_list)):
    _sum += num_list[i]**2

print(_sum % 10)