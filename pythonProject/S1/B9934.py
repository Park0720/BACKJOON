K = int(input())

build_list = list(map(int, input().split()))

i = K
cur_point = (2 ** (i-1)) - 1
cur_list = [build_list[cur_point]]
while i >= 0:
    next_list = []
    i -= 1
    point = 2 ** (i-1)
    print(*cur_list)
    if i == -1 or point < 1:
        break
    for cur in cur_list:
        cur_point = build_list.index(cur)
        next_list.append(build_list[cur_point-point])
        next_list.append(build_list[cur_point+point])

    cur_list = next_list
