from itertools import combinations

small_list = []
for _ in range(9):
    small_list.append(int(input()))

hundred_list = list(combinations(small_list, 7))

for val in hundred_list:
    val = list(val)
    val.sort()
    if sum(val) == 100:
        print(*val, sep='\n')
        break