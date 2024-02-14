from itertools import combinations

N, M = map(int, input().split())

num_list = list(map(int, input().split()))

target_list = list(combinations(num_list, 3))

_max = 0
for val in target_list:
    val = list(val)
    if sum(val) > M:
        continue
    if _max < sum(val):
        _max = sum(val)
print(_max)