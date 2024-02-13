base_list = [list(map(str, input())) for _ in range(5)]


print(base_list)
for i in range(len(base_list)):
    for j in range(len(base_list[i])):
        print(base_list[j][i], end='')